from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # 실행할 ROS2 Action을 하나의 LaunchDescription으로 반환한다.
    return LaunchDescription(
        [
            Node(
                package='maker_basic',
                executable='class_message_pub',
                output='screen',
            ),
            Node(
                package='maker_basic',
                executable='class_message_sub',
                output='screen',
            ),
        ]
    )
