import rclpy
from rclpy.node import Node
from user_interface.msg import UserInt


class UserIntPublisher(Node):
    def __init__(self):
        super().__init__('user_int_pub')
        self.publisher = self.create_publisher(UserInt, 'user_numbers', 10)
        self.timer = self.create_timer(1.0, self.publish_message)
        self.count = 0

    def publish_message(self):
        msg = UserInt()

        # 생성 시점과 세 정수 값을 하나의 데이터 계약으로 보낸다.
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'maker_lab'
        msg.user_int = self.count
        msg.user_int2 = self.count + 10
        msg.user_int3 = self.count + 20
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {self.count}')
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = UserIntPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
