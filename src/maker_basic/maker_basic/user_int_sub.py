import rclpy
from rclpy.node import Node
from user_interface.msg import UserInt


class UserIntSubscriber(Node):
    def __init__(self):
        super().__init__('user_int_sub')
        self.subscription = self.create_subscription(
            UserInt, 'user_numbers', self.message_callback, 10
        )

    def message_callback(self, msg: UserInt):
        values = (msg.user_int, msg.user_int2, msg.user_int3)
        self.get_logger().info(
            f'frame={msg.header.frame_id}, values={values}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = UserIntSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
