import rclpy
from rclpy.duration import Duration
from rclpy.node import Node
from rclpy.time import Time
from tf2_ros import Buffer, TransformException, TransformListener


class TfLookup(Node):
    def __init__(self):
        super().__init__('tf_lookup')
        self.buffer = Buffer()
        self.listener = TransformListener(self.buffer, self)
        self.timer = self.create_timer(1.0, self.lookup)

    def lookup(self):
        try:
            # world의 데이터를 joint2 기준으로 바꾸는 최신 Transform이다.
            transform = self.buffer.lookup_transform(
                'joint2',
                'world',
                Time(),
                timeout=Duration(seconds=0.2),
            )
        except TransformException as error:
            self.get_logger().warning(f'TF 조회 대기: {error}')
            return

        position = transform.transform.translation
        self.get_logger().info(
            f'world in joint2: x={position.x:.2f}, y={position.y:.2f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = TfLookup()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
