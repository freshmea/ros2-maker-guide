# 검증 기록

2026-09-08, Ubuntu 24.04 / ROS2 Jazzy에서 공개용 작업 공간을 별도로 빌드했습니다.

| 검사 | 결과 |
|---|---|
| user_interface, maker_basic, gong_basic, tf2_basic, wall_follow_lab colcon build | 5개 패키지 성공 |
| Python 59개 파일 문법 검사, 전체 Node 모듈 import | 통과 |
| XML / URDF / Xacro / SDF XML 파싱 | 통과 |
| reusable_robot, prefixed_arm Xacro 확장 및 check_urdf | 통과 |
| two_link 회전 관절 URDF check_urdf | 통과 |
| ch24_joint_motion Launch 인자 로딩 | 통과 |
| wall_follow_lab 합성 입력 단위 테스트 | 7개 통과 |
| class_message Launch 실제 Topic 송수신 | Class message: 3 수신, Publisher/Subscriber 정상 종료 |

Topic 검사는 별도 ROS_DOMAIN_ID와 localhost 발견 범위를 사용했습니다.
최초 CLI 자동 Type 발견이 완료되기 전 조회는 실패했고, Type을 명시한 재검사에서 수신했습니다.
발견이 늦으면 다음처럼 Type을 명시합니다.

```bash
ros2 topic echo /message std_msgs/msg/String --once
```

검증하지 않은 항목: 새 OS에서의 전체 의존성 설치, 모든 Service/Action 시나리오,
RViz2 GUI·슬라이더 화면, Gazebo 물리 주행, 실제 로봇 실행.
빌드 성공과 합성 입력 검사만으로 이 항목들의 성공을 의미하지 않습니다.
