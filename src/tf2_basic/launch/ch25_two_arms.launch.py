from pathlib import Path

import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def make_robot(model_path, namespace, x):
    # 하나의 식별자로 ROS Namespace와 모델 Prefix를 함께 결정한다.
    prefix = namespace + '_'
    description = xacro.process_file(
        str(model_path), mappings={'prefix': prefix}
    ).toxml()

    return [
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            namespace=namespace,
            name='robot_state_publisher',
            parameters=[{
                'robot_description': description,
                'frame_prefix': '',
            }],
            # 두 로봇의 TF는 공통 토픽에서 고유 Frame 이름으로 구분한다.
            remappings=[('tf', '/tf'), ('tf_static', '/tf_static')],
            output='screen',
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            namespace=namespace,
            name='joint_state_publisher_gui',
            output='screen',
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name=namespace + '_mount',
            arguments=[
                '--x', str(x), '--y', '0', '--z', '0',
                '--frame-id', 'world',
                '--child-frame-id', prefix + 'base_link',
            ],
            output='screen',
        ),
    ]


def generate_launch_description():
    share = Path(get_package_share_directory('tf2_basic'))
    model_path = share / 'urdf' / 'prefixed_arm.urdf.xacro'
    nodes = []
    for namespace, x in [('robot1', 0.0), ('robot2', 1.0)]:
        nodes.extend(make_robot(model_path, namespace, x))
    nodes.append(Node(
        package='rviz2', executable='rviz2', output='screen'
    ))
    return LaunchDescription(nodes)
