from glob import glob
from setuptools import find_packages, setup

setup(
    name='wall_follow_lab',
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/wall_follow_lab']),
        ('share/wall_follow_lab', ['package.xml']),
        ('share/wall_follow_lab/launch', glob('launch/*.launch.py')),
        ('share/wall_follow_lab/worlds', glob('worlds/*.sdf')),
        ('share/wall_follow_lab/models', glob('models/*.urdf')),
        ('share/wall_follow_lab/config', glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@example.com',
    description='Chapter 27 TurtleBot3 wall-following simulation',
    license='Apache-2.0',
    entry_points={'console_scripts': [
        'wall_follow = wall_follow_lab.wall_follow:main',
    ]},
)
