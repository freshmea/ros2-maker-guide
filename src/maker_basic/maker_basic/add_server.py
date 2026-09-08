import rclpy
from rclpy.node import Node
from user_interface.srv import AddAndOdd


class AddServer(Node):
    def __init__(self):
        super().__init__('add_server')
        self.service = self.create_service(
            AddAndOdd, 'add_and_odd', self.add_callback
        )

    def add_callback(self, request, response):
        # 계산 결과와 판정 문자열을 같은 응답에 담는다.
        response.sum = request.inta + request.intb
        if response.sum % 2 == 1:
            response.odd = 'sum is odd'
        else:
            response.odd = 'sum is even'

        self.get_logger().info(
            f'{request.inta} + {request.intb} = {response.sum}'
        )
        return response


def main(args=None):
    rclpy.init(args=args)
    node = AddServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
