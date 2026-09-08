from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import AppendEnvironmentVariable, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    lab = Path(get_package_share_directory('wall_follow_lab'))
    tb3 = Path(get_package_share_directory('turtlebot3_gazebo'))
    gz = Path(get_package_share_directory('ros_gz_sim'))
    description = (tb3 / 'urdf' / 'turtlebot3_burger.urdf').read_text()
    return LaunchDescription([
        AppendEnvironmentVariable(
            'GZ_SIM_RESOURCE_PATH', str(tb3 / 'models')
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(str(gz / 'launch' / 'gz_sim.launch.py')),
            launch_arguments={
                'gz_args': '-r ' + str(lab / 'worlds' / 'wall_room.sdf'),
                'on_exit_shutdown': 'true',
            }.items(),
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': description, 'use_sim_time': True}],
            output='screen',
        ),
        Node(
            package='ros_gz_bridge', executable='parameter_bridge',
            parameters=[{'config_file': str(lab / 'config' / 'bridge.yaml')}],
            output='screen',
        ),
        Node(
            package='ros_gz_sim', executable='create',
            arguments=[
                '-world', 'wall_room', '-name', 'burger',
                '-file', str(tb3 / 'models' / 'turtlebot3_burger' / 'model.sdf'),
                '-x', '-2.0', '-y', '-1.4', '-z', '0.01',
            ],
            output='screen',
        ),
    ])
