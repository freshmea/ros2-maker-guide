import threading
import time

import rclpy
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from user_interface.srv import AddAndOdd


class ThreadedAddServer(Node):
    def __init__(self):
        super().__init__('threaded_add_server')
        self.callback_group = ReentrantCallbackGroup()
        self.lock = threading.Lock()
        self.completed_count = 0

        self.service = self.create_service(
            AddAndOdd,
            'slow_add_and_odd',
            self.add_callback,
            callback_group=self.callback_group,
        )
        self.timer = self.create_timer(
            1.0,
            self.status_callback,
            callback_group=self.callback_group,
        )

    def add_callback(self, request, response):
        self.get_logger().info('긴 계산을 시작한다.')

        # 긴 작업을 재현하되 공유 상태는 잠그지 않은 채 기다린다.
        time.sleep(5.0)
        response.sum = request.inta + request.intb
        response.odd = 'odd' if response.sum % 2 else 'even'

        # 읽기-수정-쓰기를 하나의 임계 구역으로 보호한다.
        with self.lock:
            self.completed_count += 1

        self.get_logger().info('긴 계산을 완료했다.')
        return response

    def status_callback(self):
        with self.lock:
            count = self.completed_count
        self.get_logger().info(f'완료 요청 수: {count}')


def main(args=None):
    rclpy.init(args=args)
    node = ThreadedAddServer()
    executor = MultiThreadedExecutor(num_threads=4)
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        executor.shutdown()
        node.destroy_node()
        rclpy.try_shutdown()
