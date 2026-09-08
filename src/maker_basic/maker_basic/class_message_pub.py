import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ClassPublisher(Node):
    def __init__(self):
        # 부모 Node를 먼저 초기화해 ROS 그래프에 참여할 준비를 한다.
        super().__init__('class_message_pub')

        # Callback과 상태가 함께 사용할 Publisher를 멤버로 보관한다.
        self.publisher = self.create_publisher(String, 'message', 10)
        self.count = 0

        # Timer 객체를 보관해 Node가 살아 있는 동안 주기 이벤트를 유지한다.
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # 현재 객체의 count를 사용해 매번 다른 메시지를 만든다.
        msg = String()
        msg.data = f'Class message: {self.count}'

        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = ClassPublisher()

    try:
        # Executor가 Timer 이벤트를 기다리고 준비된 Callback을 실행한다.
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # Node를 먼저 정리하고 마지막에 rclpy Context를 종료한다.
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
