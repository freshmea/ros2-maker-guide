import rclpy
from rclpy.node import Node


def main(args=None):
    # ROS2 CLI에서 전달한 인수를 해석할 수 있도록 기본 Context를 초기화한다.
    rclpy.init(args=args)

    # 파일명과 분리된 Runtime Node 이름을 명시적으로 정한다.
    node = Node('simple_node')
    print('simple_node started')

    try:
        # 종료 요청을 받을 때까지 Executor가 이 Node의 작업을 기다리게 한다.
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # 통신 자원은 Context를 종료하기 전에 Node부터 해제한다.
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
