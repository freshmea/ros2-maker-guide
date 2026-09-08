# ROS2 Maker Guide

**『ROS2 입문』**의 독자용 실습 코드 저장소입니다.

- 부제: Ubuntu 24.04·Jazzy·Gazebo Harmonic과 AI로 시작하는 로봇 메이커 가이드
- 저자: 최수길 · 출판사: 마담
- 기준 환경: Ubuntu 24.04 / ROS2 Jazzy / Gazebo Harmonic (Windows에서는 WSL2)
- 책 정보와 목차: [BOOK.md](BOOK.md)
- 장별 코드와 실행 안내: [docs/chapters.md](docs/chapters.md)
- 검증 결과와 한계: [docs/validation.md](docs/validation.md)

## 빠른 시작

책 2~3장에 따라 Ubuntu와 ROS2 Jazzy를 먼저 설치합니다. 아래는 Ubuntu Bash 명령입니다.
`~/ros_ws`가 아직 없는 새 실습 환경을 기준으로 합니다.

```bash
git clone https://github.com/freshmea/ros2-maker-guide.git ~/ros_ws
cd ~/ros_ws
source /opt/ros/jazzy/setup.bash
sudo apt update
sudo apt install python3-colcon-common-extensions python3-rosdep
```

처음 rosdep을 사용하는 환경에서만 `sudo rosdep init`을 한 번 실행합니다.
기본 실습 의존성은 다음처럼 설치하고 빌드합니다. 27장 시뮬레이터는 별도로 준비합니다.

```bash
rosdep update
rosdep install --from-paths src/user_interface src/maker_basic src/gong_basic src/tf2_basic --ignore-src --rosdistro jazzy -r -y
colcon build --symlink-install --packages-select user_interface maker_basic gong_basic tf2_basic
source install/setup.bash
ros2 launch maker_basic class_message.launch.py
```

Publisher와 Subscriber가 실행되고 `Class message:` 메시지가 반복되면 첫 실행에 성공한 것입니다.
다른 터미널에서도 다음 환경을 적용한 뒤 책의 명령을 실행합니다.

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros_ws/install/setup.bash
ros2 topic echo /message --once
```

매번 source가 필요합니다. 필요하면 위 두 source 명령을 `~/.bashrc`에 **중복 없이** 추가합니다.
종료는 실행 터미널에서 `Ctrl+C`를 누릅니다.

이미 `~/ros_ws`가 있다면 다른 이름으로 clone하고 기존 패키지와 비교하세요.
같은 이름의 패키지를 중복 배치하거나 기존 실습 파일을 덮어쓰지 마세요.
책에서 직접 작성하는 과정과 완성 코드를 실행하는 과정은 별도 작업 공간에서 진행하면 편리합니다.

## 제공 범위

| 폴더 | 내용 |
|---|---|
| `src/maker_basic` | 7~16장 본문 예제: Node, Topic, QoS, Service, Executor, Parameter |
| `src/user_interface` | 사용자 정의 Message, Service, Action |
| `src/gong_basic` | 책에서 참조하는 기초 수업 코드, Action, Turtlesim Namespace |
| `src/tf2_basic` | 22~26장 TF, URDF, 관절 운동, Xacro, RViz2 |
| `src/wall_follow_lab` | 27장 Gazebo 벽 따라가기 실습과 합성 입력 검사 |

`maker_basic`과 `gong_basic`은 책에서 사용하는 이름을 그대로 유지합니다.
본문 예제와 수업 참고 예제의 동작이 모두 같지는 않습니다. 실행할 장의 패키지 이름을 확인하세요.
23장의 고정 관절 원본은 `two_link_fixed.urdf`, 24장의 회전 관절 완성본은 `two_link.urdf`입니다.
20장의 종합 과제는 독자가 구현하는 과제이며 별도의 완성 답안은 제공하지 않습니다.

## 공개 범위와 이용

실습 코드, 설치·실행 안내, 책 소개와 목차만 제공합니다.
책 본문, 표지·삽화, PDF·EPUB, 집필 도구, 개발 이력, 실물 매니퓰레이터·카메라·AI 모델은 포함하지 않습니다.
이 저장소는 독립된 Git 이력으로 관리합니다.
코드는 기존 Apache License 2.0을 유지합니다. [LICENSE](LICENSE)를 확인하세요.
이 코드의 라이선스가 별도로 출판되는 책 본문·이미지의 이용 허락을 의미하지는 않습니다.

오류 제보는 [Issues](https://github.com/freshmea/ros2-maker-guide/issues)에 장 번호,
실행 명령, ROS2 버전, 오류 로그를 남겨 주세요. 비밀번호나 개인 정보는 제거해 주세요.
