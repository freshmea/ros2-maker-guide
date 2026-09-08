import math

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState


class JointWave(Node):
    def __init__(self):
        super().__init__('ch24_joint_wave')
        self.publisher = self.create_publisher(
            JointState, 'joint_states', 10
        )
        self.start_time = self.get_clock().now()
        self.timer = self.create_timer(0.05, self.publish_joint)

    def publish_joint(self):
        now = self.get_clock().now()
        elapsed = (now - self.start_time).nanoseconds * 1e-9
        position = 0.8 * math.sin(0.5 * elapsed)
        velocity = 0.4 * math.cos(0.5 * elapsed)

        msg = JointState()
        msg.header.stamp = now.to_msg()
        msg.name = ['base_to_arm']
        msg.position = [position]
        msg.velocity = [velocity]
        # effort는 측정하지 않았으므로 빈 배열로 둔다.
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = JointWave()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
