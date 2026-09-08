import rclpy
from rclpy.node import Node
from std_msgs.msg import String


def main(args=None):
    rclpy.init(args=args)
    node = Node('message_pub')

    # Topic 이름, 메시지 형식, 보관 깊이를 지정해 발행 통로를 만든다.
    publisher = node.create_publisher(String, 'message', 10)
    count = 0

    def timer_callback():
        nonlocal count

        # String 메시지의 data 필드에 이번 순번을 포함한 문자열을 넣는다.
        msg = String()
        msg.data = f'Hello ROS2: {count}'

        # 로그는 화면 확인이고 publish는 Topic으로 보내는 실제 동작이다.
        publisher.publish(msg)
        print(f'Published: {msg.data}')
        count += 1

    # 1초마다 콜백을 실행할 Timer를 등록한다.
    timer = node.create_timer(1.0, timer_callback)

    try:
        # 등록한 Timer 콜백이 반복 실행되도록 이벤트를 처리한다.
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # 사용한 ROS2 자원을 정리해 정상 종료한다.
        node.destroy_timer(timer)
        node.destroy_node()
        if rclpy.ok():
            rclpy.try_shutdown()


if __name__ == '__main__':
    main()
