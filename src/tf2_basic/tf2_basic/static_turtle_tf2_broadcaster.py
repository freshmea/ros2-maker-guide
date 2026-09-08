import rclpy
from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from tf2_ros import StaticTransformBroadcaster


class StaticTurtleTf(Node):
    def __init__(self):
        super().__init__('static_tf')
        self.broadcaster = StaticTransformBroadcaster(self)

        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = 'turtle1'
        transform.child_frame_id = 'joint1'
        transform.transform.translation.x = 1.0
        transform.transform.translation.y = 1.0

        # 회전이 없는 Unit Quaternion을 사용한다.
        transform.transform.rotation.x = 0.0
        transform.transform.rotation.y = 0.0
        transform.transform.rotation.z = 0.0
        transform.transform.rotation.w = 1.0
        second = TransformStamped()
        second.header.stamp = transform.header.stamp
        second.header.frame_id = 'joint1'
        second.child_frame_id = 'joint2'
        second.transform.translation.x = 1.0
        second.transform.translation.y = 1.0
        second.transform.translation.z = 1.0
        second.transform.rotation.w = 1.0
        self.broadcaster.sendTransform([transform, second])


def main(args=None):
    rclpy.init(args=args)
    node = StaticTurtleTf()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
