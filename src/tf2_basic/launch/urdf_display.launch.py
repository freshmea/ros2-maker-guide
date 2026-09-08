from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    default_model = PathJoinSubstitution([
        FindPackageShare('tf2_basic'), 'urdf', '01_myfirst.urdf',
    ])
    default_rviz = PathJoinSubstitution([
        FindPackageShare('tf2_basic'), 'rviz', 'urdf.rviz',
    ])

    return LaunchDescription([
        DeclareLaunchArgument('model', default_value=default_model),
        DeclareLaunchArgument('gui', default_value='false'),
        DeclareLaunchArgument('rvizconfig', default_value=default_rviz),
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('urdf_launch'), 'launch', 'display.launch.py',
            ]),
            launch_arguments={
                'urdf_package': 'tf2_basic',
                'urdf_package_path': LaunchConfiguration('model'),
                'rviz_config': LaunchConfiguration('rvizconfig'),
                'jsp_gui': LaunchConfiguration('gui'),
            }.items(),
        ),
    ])
