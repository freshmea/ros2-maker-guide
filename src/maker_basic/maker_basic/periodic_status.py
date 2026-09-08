import rclpy
from rcl_interfaces.msg import SetParametersResult
from rclpy.node import Node


class PeriodicStatus(Node):
    def __init__(self):
        super().__init__('periodic_status')
        self.declare_parameter('message', 'robot ready')
        self.declare_parameter('publish_period', 1.0)

        self.message = self.get_parameter('message').value
        self.publish_period = self.get_parameter('publish_period').value
        self.timer = self.create_timer(
            self.publish_period, self.timer_callback
        )
        self.add_on_set_parameters_callback(self.parameter_callback)

    def timer_callback(self):
        self.get_logger().info(
            f'{self.message}, period={self.publish_period:.2f}s'
        )

    def parameter_callback(self, parameters):
        next_message = self.message
        next_period = self.publish_period

        for parameter in parameters:
            if parameter.name == 'message':
                next_message = parameter.value
            elif parameter.name == 'publish_period':
                if not 0.1 <= parameter.value <= 10.0:
                    return SetParametersResult(
                        successful=False,
                        reason='publish_period는 0.1~10.0초여야 한다.',
                    )
                next_period = parameter.value

        # 모든 입력이 유효할 때만 내부 상태를 한꺼번에 갱신한다.
        self.message = next_message
        if next_period != self.publish_period:
            self.publish_period = next_period
            self.timer.cancel()
            self.timer = self.create_timer(
                self.publish_period, self.timer_callback
            )

        return SetParametersResult(successful=True)


def main(args=None):
    rclpy.init(args=args)
    node = PeriodicStatus()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
