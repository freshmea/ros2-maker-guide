from glob import glob
from setuptools import find_packages, setup

package_name = 'maker_basic'
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
        'add_client = maker_basic.add_client:main',
        'add_server = maker_basic.add_server:main',
        'class_message_pub = maker_basic.class_message_pub:main',
        'class_message_sub = maker_basic.class_message_sub:main',
        'message_pub = maker_basic.message_pub:main',
        'message_sub = maker_basic.message_sub:main',
        'periodic_status = maker_basic.periodic_status:main',
        'qos_message_pub = maker_basic.qos_message_pub:main',
        'qos_message_sub = maker_basic.qos_message_sub:main',
        'simple_node = maker_basic.simple_node:main',
        'threaded_add_server = maker_basic.threaded_add_server:main',
        'user_int_pub = maker_basic.user_int_pub:main',
        'user_int_sub = maker_basic.user_int_sub:main',
    ]},
)
