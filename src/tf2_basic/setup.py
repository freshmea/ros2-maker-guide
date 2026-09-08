from glob import glob
from setuptools import find_packages, setup

package_name = 'tf2_basic'
setup(
    name=package_name, version='0.1.0', packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*')),
        ('share/' + package_name + '/config', glob('config/*')),
        ('share/' + package_name + '/urdf', glob('urdf/*')),
        ('share/' + package_name + '/rviz', glob('rviz/*')),
    ],
    install_requires=['setuptools'], zip_safe=True,
    maintainer='choi su gil', maintainer_email='freshmea@naver.com',
    description='ROS2 maker guide book examples', license='Apache-2.0',
    entry_points={'console_scripts': [
        'ch24_joint_wave = tf2_basic.ch24_joint_wave:main',
        'dynamic_turtle_tf2_broadcaster = tf2_basic.dynamic_turtle_tf2_broadcaster:main',
        'static_turtle_tf2_broadcaster = tf2_basic.static_turtle_tf2_broadcaster:main',
        'tf_listener = tf2_basic.tf_listener:main',
    ]},
)
