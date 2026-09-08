# 장별 코드 안내

모든 명령은 README의 빌드와 환경 source 이후 실행합니다.

| 장 | 파일 / 실행 항목 |
|---|---|
| 1~6 | 환경 설치와 CLI, 패키지 생성 실습. 별도 전용 Node 없음 |
| 7 | `maker_basic/simple_node` |
| 8 | `maker_basic/message_pub`, `message_sub` |
| 9~10 | `maker_basic/class_message_pub`, `class_message_sub`; `class_message.launch.py` |
| 11~12 | `maker_basic/qos_message_pub`, `qos_message_sub` |
| 13 | `user_interface/msg/UserInt.msg`; `maker_basic/user_int_pub`, `user_int_sub` |
| 14 | `user_interface/srv/AddAndOdd.srv`; `maker_basic/add_server`, `add_client` |
| 15 | `maker_basic/threaded_add_server` |
| 16 | `maker_basic/periodic_status`; `config/status.yaml`, `status.launch.py` |
| 17~19 | `user_interface/action/Fibonacci.action`; `gong_basic/action_server`, `action_thread_server`, `action_client` |
| 20 | `gong_basic/launch/two_turtle.launch.py`, `gong_basic/mv_turtle_ns` |
| 21~22 | `tf2_basic/static_turtle_tf2_broadcaster`, `dynamic_turtle_tf2_broadcaster`, `tf_listener` |
| 23 | `tf2_basic/urdf/two_link_fixed.urdf` |
| 24 | `tf2_basic/urdf/two_link.urdf`, `ch24_joint_motion.launch.py`, `ch24_joint_wave` |
| 25 | `tf2_basic/urdf/reusable_robot.urdf.xacro`, `prefixed_arm.urdf.xacro`, `ch25_two_arms.launch.py` |
| 26 | `tf2_basic/launch/urdf_display.launch.py`, `rviz/urdf.rviz` |
| 27 | [wall_follow_lab 실습](../src/wall_follow_lab/README.md) |

Python Node는 `src/<패키지>/<패키지>/<실행 항목>.py`에 있습니다.
예를 들어 `ros2 run maker_basic add_server`는 `src/maker_basic/maker_basic/add_server.py`를 실행합니다.

## 대표 실행

```bash
# 각 서버와 클라이언트는 서로 다른 터미널에서 실행합니다.
ros2 run maker_basic add_server
ros2 run maker_basic add_client

# Action의 기본 성공 흐름: 서버를 먼저 실행합니다.
ros2 run gong_basic action_server
ros2 run gong_basic action_client 8

# 24장: GUI 슬라이더 또는 Python 발행자 중 하나만 사용합니다.
ros2 launch tf2_basic ch24_joint_motion.launch.py gui:=true
# GUI 실습을 종료한 다음 코드 발행자로 전환합니다.
ros2 launch tf2_basic ch24_joint_motion.launch.py gui:=false
```

24장에서는 RViz2 Fixed Frame을 `base_link`로 설정하고 RobotModel을 추가해
`/robot_description`을 선택합니다. `/joint_states`의 `base_to_arm` 값 변화와 팔의 회전을 확인합니다.
25장 두 로봇은 Fixed Frame `world`, RobotModel 두 개의 설명 Topic을
`/robot1/robot_description`, `/robot2/robot_description`으로 지정합니다.

Package not found이면 빌드 결과와 해당 터미널의 source를 확인합니다.
실행 항목이 없으면 `ros2 pkg executables <패키지>`를 확인합니다.
RViz2에서 형상이 없으면 Fixed Frame, Robot Description Topic, TF와 `/joint_states`를 확인합니다.
WSL GUI가 열리지 않으면 책 2~3장의 WSLg 환경 점검을 먼저 진행합니다.
