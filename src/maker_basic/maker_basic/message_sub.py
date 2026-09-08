import rclpy
from rclpy.node import Node
from std_msgs.msg import String


def main(args=None):
    rclpy.init(args=args)
    node = Node('message_sub')

    def message_callback(msg: String):
        # 수신한 String 메시지의 data 필드를 사람이 확인할 수 있게 기록한다.
        node.get_logger().info(f'Received: {msg.data}')

    # 새 메시지가 도착할 때 실행할 콜백을 message Topic에 연결한다.
    subscription = node.create_subscription(
        String,
        'message',
        message_callback,
        10,
    )

    try:
        # 수신 이벤트가 생기면 등록한 콜백을 실행하도록 기다린다.
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # 구독과 Node를 정리한 뒤 rclpy를 종료한다.
        node.destroy_subscription(subscription)
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
