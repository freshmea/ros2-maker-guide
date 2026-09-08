import math

import rclpy
from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose


class TurtleTf(Node):
    def __init__(self):
        super().__init__('turtle_tf')
        self.broadcaster = TransformBroadcaster(self)
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10
        )

    def pose_callback(self, pose: Pose):
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = 'world'
        transform.child_frame_id = 'turtle1'
        transform.transform.translation.x = pose.x
        transform.transform.translation.y = pose.y
        transform.transform.translation.z = 0.0

        # Turtlesim의 Yaw를 Quaternion의 z와 w 성분으로 변환한다.
        transform.transform.rotation.z = math.sin(pose.theta / 2.0)
        transform.transform.rotation.w = math.cos(pose.theta / 2.0)
        self.broadcaster.sendTransform(transform)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleTf()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
