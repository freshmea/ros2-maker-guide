import math
import time

import rclpy
from geometry_msgs.msg import TwistStamped
from rclpy.clock import Clock, ClockType
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from rclpy.signals import SignalHandlerOptions
from sensor_msgs.msg import LaserScan


def sector(scan, center_deg, width_deg):
    values = []
    center = math.radians(center_deg)
    half = math.radians(width_deg / 2)
    for index, distance in enumerate(scan.ranges):
        angle = scan.angle_min + index * scan.angle_increment
        error = math.atan2(math.sin(angle - center), math.cos(angle - center))
        if abs(error) > half:
            continue
        if math.isfinite(distance) and scan.range_min <= distance <= scan.range_max:
            values.append(distance)
        elif distance == math.inf:
            values.append(scan.range_max)
    return min(values) if len(values) >= 3 else None


def decide(scan, target=0.45):
    front = sector(scan, 0, 50)
    right = sector(scan, -90, 6)
    diagonal = sector(scan, -45, 6)
    if None in (front, right, diagonal):
        return 0.0, 0.0, 'INVALID_SCAN'
    if min(front, right, diagonal) < 0.22:
        return 0.0, 0.0, 'TOO_CLOSE'
    if front < 0.55:
        return 0.0, 0.5, 'TURN_LEFT'
    if right > 0.9:
        return 0.04, -0.3, 'FIND_RIGHT_WALL'
    # 오른쪽 90도·45도 거리로 벽과의 기울기를 근사한다.
    alpha = math.atan2(
        diagonal * math.cos(math.pi / 4) - right,
        diagonal * math.sin(math.pi / 4),
    )
    angular = 1.2 * (target - right) - 0.8 * alpha
    angular = max(-0.5, min(0.5, angular))
    return 0.08, angular, 'FOLLOW'


class WallFollow(Node):
    def __init__(self):
        super().__init__('wall_follow')
        self.publisher = self.create_publisher(TwistStamped, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan, 'scan', self.on_scan, qos_profile_sensor_data
        )
        self.scan = None
        self.received_at = None
        self.started_at = time.monotonic()
        self.last_state = None
        # /clock이 멈춰도 수신 중단을 감시하도록 실제 시간 Timer를 쓴다.
        self.timer_clock = Clock(clock_type=ClockType.STEADY_TIME)
        self.timer = self.create_timer(0.1, self.control, clock=self.timer_clock)

    def on_scan(self, scan):
        self.scan = scan
        self.received_at = time.monotonic()

    def send(self, linear, angular):
        command = TwistStamped()
        command.header.stamp = self.get_clock().now().to_msg()
        command.header.frame_id = 'base_footprint'
        command.twist.linear.x = linear
        command.twist.angular.z = angular
        self.publisher.publish(command)

    def control(self):
        now = time.monotonic()
        if now - self.started_at >= 120.0:
            linear, angular, state = 0.0, 0.0, 'TIME_LIMIT'
        elif self.received_at is None or now - self.received_at > 1.0:
            linear, angular, state = 0.0, 0.0, 'WAIT_SCAN'
        else:
            stamp = self.scan.header.stamp
            age = self.get_clock().now().nanoseconds * 1e-9 - (
                stamp.sec + stamp.nanosec * 1e-9
            )
            if age < -0.1 or age > 1.0:
                linear, angular, state = 0.0, 0.0, 'STALE_SCAN'
            else:
                linear, angular, state = decide(self.scan)
        self.send(linear, angular)
        if state != self.last_state:
            self.get_logger().info(state)
            self.last_state = state


def main(args=None):
    rclpy.init(args=args, signal_handler_options=SignalHandlerOptions.NO)
    node = WallFollow()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # 정상 종료 시 정지 명령을 여러 번 보내고 자원을 정리한다.
        for _ in range(5):
            node.send(0.0, 0.0)
            time.sleep(0.05)
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
