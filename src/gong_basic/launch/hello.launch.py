from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(package="gong_basic", executable="class_pub", output="screen"),
            Node(package="gong_basic", executable="class_sub", output="screen"),
        ]
    )
