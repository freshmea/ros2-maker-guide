from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    parameter_file = PathJoinSubstitution(
        [FindPackageShare('maker_basic'), 'config', 'status.yaml']
    )

    return LaunchDescription([
        Node(
            package='maker_basic',
            executable='periodic_status',
            name='periodic_status',
            parameters=[parameter_file],
            output='screen',
        )
    ])
