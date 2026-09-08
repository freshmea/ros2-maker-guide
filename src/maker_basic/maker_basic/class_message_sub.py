import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ClassSubscriber(Node):
    def __init__(self):
        # 수신 Node의 이름을 정하고 부모 Node 기능을 초기화한다.
        super().__init__('class_message_sub')

        # Subscription을 멤버로 보관해 데이터 통로와 Callback을 유지한다.
        self.subscription = self.create_subscription(
            String,
            'message',
            self.message_callback,
            10,
        )

    def message_callback(self, msg: String):
        # Executor가 전달한 메시지의 data 필드를 수신 결과로 기록한다.
        self.get_logger().info(f'Received: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = ClassSubscriber()

    try:
        # 새 메시지가 도착할 때까지 기다리고 Subscription Callback을 실행한다.
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
