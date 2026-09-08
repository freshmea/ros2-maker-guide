# 27장: Gazebo 벽 따라가기

Ubuntu 24.04, ROS2 Jazzy, Gazebo Harmonic 기준입니다.
기본 실습은 루트 [README](../../README.md)를 먼저 완료합니다.

## 설치와 빌드

```bash
source /opt/ros/jazzy/setup.bash
sudo apt update
sudo apt install ros-jazzy-ros-gz ros-jazzy-turtlebot3-gazebo ros-jazzy-turtlebot3-description
cd ~/ros_ws
rosdep install --from-paths src/wall_follow_lab --ignore-src --rosdistro jazzy -r -y
colcon build --packages-select wall_follow_lab --symlink-install
source install/setup.bash
ros2 pkg prefix turtlebot3_gazebo
ros2 pkg prefix ros_gz_bridge
```

패키지를 찾지 못하면 Jazzy apt 저장소 설정을 확인합니다. 소스 설치가 필요한 환경은
책 27장의 ROBOTIS Jazzy 브랜치 설치 순서를 따릅니다. 다른 ROS 배포판의 패키지를 섞지 않습니다.

## 실행과 관찰

터미널 A:

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros_ws/install/setup.bash
ros2 launch wall_follow_lab wall_room.launch.py
```

Gazebo에 방과 Burger가 생성되는지 확인합니다. 별도 터미널 B에서 환경을 source한 뒤:

```bash
ros2 topic echo /clock --once
ros2 topic info /scan
ros2 topic info /cmd_vel
ros2 run wall_follow_lab wall_follow --ros-args -p use_sim_time:=true
```

`/scan`은 `sensor_msgs/msg/LaserScan`, `/cmd_vel`은 `geometry_msgs/msg/TwistStamped`입니다.
시뮬레이션이 재생 중일 때 오른쪽 벽과의 거리를 유지하는지 관찰합니다.
Scan이 없으면 World의 재생 상태, Bridge와 Topic을 먼저 확인합니다.
제어기를 실행하기 전에 장애물 배치와 모델 생성 결과를 확인하세요.

```bash
python3 ~/ros_ws/src/wall_follow_lab/tests/test_controller.py
```

이 검사는 합성 LaserScan 입력을 사용하며 물리 주행 검증을 대신하지 않습니다.
정상 `Ctrl+C` 종료 때 정지 명령을 전송하지만 강제 종료나 통신 단절 때의 정지를 보장하지 않습니다.
예상과 다르게 움직이면 Gazebo를 Pause하고 입력·상태를 확인합니다.
