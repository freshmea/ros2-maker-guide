import rclpy
from rclpy.node import Node
from user_interface.srv import AddAndOdd


class AddClient(Node):
    def __init__(self):
        super().__init__("add_client")
        self.client = self.create_client(AddAndOdd, "add_and_odd")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service를 기다리는 중이다.')
        self.create_timer(3, self.send_request)
        self.create_timer(1, self.update)
        self.count = 0


    def send_request(self):
        self.get_logger().info(f"서버에 요청함{self.count}")

        request = AddAndOdd.Request()
        request.inta = 4
        request.intb = 8 + self.count
        self.count += 1
        future = self.client.call_async(request)  # None-block
        future.add_done_callback(self.done_callback)

    def done_callback(self, future):  # Future 가 완료 되는 시점에서 함수 호출
        response: AddAndOdd.Response = future.result()
        self.get_logger().info(f"{response.sum}")
        self.get_logger().info(f"{response.odd}")

    def update(self):
        self.get_logger().info("updating!!")

def main(args=None):
    rclpy.init(args=args)
    node = AddClient()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
