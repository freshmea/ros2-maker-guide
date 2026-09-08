from pathlib import Path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    share = Path(get_package_share_directory('tf2_basic'))
    description = (share / 'urdf' / 'two_link.urdf').read_text(
        encoding='utf-8'
    )
    gui = LaunchConfiguration('gui')

    return LaunchDescription([
        DeclareLaunchArgument('gui', default_value='true',
                              choices=['true', 'false']),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': description}],
            output='screen',
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            condition=IfCondition(gui),
            output='screen',
        ),
        Node(
            package='tf2_basic',
            executable='ch24_joint_wave',
            condition=UnlessCondition(gui),
            output='screen',
        ),
        Node(package='rviz2', executable='rviz2', output='screen'),
    ])
