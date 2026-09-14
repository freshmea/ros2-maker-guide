# ROS2 Maker

**Ubuntu 24.04 + ROS2 Jazzy + Gazebo Harmonic**

로봇 프로그래밍, 어디서 시작할지 막막했다면 먼저 읽고 실행해 보세요.
**『ROS2 입문』의 1~3장 무료 컬러 PDF와 실제 실습 코드**를 제공합니다.
환경 설치에서 Python Node, 통신, 로봇 모델링, 시뮬레이션으로 이어지는 책의 체험판입니다.

**[📖 1~3장 무료 SAMPLE PDF](samples/ros2-maker-guide-ch01-03-sample.pdf)** ·
[🚀 30분 Quick Start](#quick-start) · [🤖 직접 실행하는 데모](#demo) · [🎓 강의계획서](#syllabi)

[📘 책 소개](BOOK.md) · [💻 Sample Code](docs/chapters.md) ·
[📚 전체 목차](BOOK.md#목차) · [🛒 부크크 전자책 구매](https://bookk.co.kr/bookStore/6aa76a46dc64fe8c7e11a5e1) · [📕 종이책 구매 안내](BOOK.md#print)

> **ROS2 입문** — Ubuntu 24.04·Jazzy·Gazebo Harmonic과 AI로 시작하는 로봇 메이커 가이드
>
> 최수길 지음 · 마담
>
> **전자책 부크크 입점** · [부크크에서 구매하기](https://bookk.co.kr/bookStore/6aa76a46dc64fe8c7e11a5e1)

<a id="syllabi"></a>

## 대학 강의·집중교육에 활용하세요

『ROS2 입문』과 공개 실습 코드를 수업으로 연결하는 **강의계획서 2종**입니다.
학습 목표, 회차별 실습과 완료 기준, 제출물, 평가 방법, 사전 준비를 담았습니다.
Markdown은 수업에 맞춰 편집할 때, PDF는 배포·인쇄할 때 사용하세요.

| 과정 | 운영과 특징 | Markdown | PDF |
|---|---|---|---|
| **15주 대학 강의** | 주 3시간·총 45시간. 기초부터 모델링·시뮬레이션까지, 중간 실기와 기말 프로젝트 포함 | [계획서 읽기](docs/syllabi/university-15-weeks.md) | [PDF 보기](docs/syllabi/university-15-weeks.pdf) |
| **5일 집중과정** | 일 6시간·총 30시간. 사전 설치 후 핵심 실습과 팀 미니 프로젝트 중심 | [계획서 읽기](docs/syllabi/bootcamp-5-days.md) | [PDF 보기](docs/syllabi/bootcamp-5-days.pdf) |

수업 시간과 평가 비중은 운영 제안이며 기관에 맞게 조정할 수 있습니다.
집중과정의 사전 설치·예습은 수업 30시간에 포함하지 않습니다.
PDF가 바로 열리지 않으면 [15주 PDF 다운로드](https://github.com/freshmea/ros2-maker-guide/raw/refs/heads/main/docs/syllabi/university-15-weeks.pdf) 또는 [5일 PDF 다운로드](https://github.com/freshmea/ros2-maker-guide/raw/refs/heads/main/docs/syllabi/bootcamp-5-days.pdf)를 이용하세요.

## 먼저 3장까지 읽어 보세요

| 무료 공개 | 읽고 나면 할 수 있는 일 |
|---|---|
| 1장. ROS2로 무엇을 만들 수 있는가 | Node와 통신이 로봇 시스템을 구성하는 방식 설명하기 |
| 2장. Windows·WSL2·Ubuntu의 관계 | 어느 터미널에서 작업할지 판단하고 개발 환경 구분하기 |
| 3장. Ubuntu 24.04와 ROS2 Jazzy 설치 | 설치 후 Talker와 Listener의 실제 통신 확인하기 |

**[PDF 바로 읽기](samples/ros2-maker-guide-ch01-03-sample.pdf)** ·
[PDF 다운로드](https://github.com/freshmea/ros2-maker-guide/raw/refs/heads/main/samples/ros2-maker-guide-ch01-03-sample.pdf) ·
[샘플 범위와 이용 안내](samples/README.md)

본문 57쪽에 샘플 안내 2쪽을 더한 총 59쪽의 컬러 PDF, 약 6.1 MiB입니다.
장별 학습 목표, 실행 명령, 확인 방법, 문제 해결, 참고 자료까지 읽을 수 있습니다.
PDF가 GitHub에서 바로 열리지 않으면 다운로드 링크를 사용하세요.

<a id="quick-start"></a>

## 30분 Quick Start

**목표: 두 Python Node를 실행하고 `/message`로 오가는 메시지를 확인합니다.**
Ubuntu 24.04와 ROS2 Jazzy가 설치된 환경에서 약 30분을 목표로 하는 체험입니다.
OS·ROS2 설치 시간은 포함하지 않으며, 다운로드와 PC 성능에 따라 더 걸릴 수 있습니다.
처음이라면 무료 PDF 2~3장부터 진행하세요. 이 체험은 책 9~10장의 완성 코드를 먼저 실행합니다.

### 1. 코드와 도구 준비 · 약 5분

아래는 Ubuntu Bash 명령이며, `~/ros_ws`가 아직 없는 새 실습 환경을 기준으로 합니다.
기존 작업 공간이 있다면 다른 경로를 사용하고 이후 명령의 경로도 함께 변경하세요.

```bash
source /opt/ros/jazzy/setup.bash
sudo apt update
sudo apt install git python3-colcon-common-extensions python3-rosdep
git clone https://github.com/freshmea/ros2-maker-guide.git ~/ros_ws
cd ~/ros_ws
```

### 2. 의존성 설치와 빌드 · 약 15분

처음 rosdep을 사용하는 환경에서만 `sudo rosdep init`을 한 번 실행합니다.
27장 Gazebo 시뮬레이터는 이 체험에 필요하지 않으며 별도로 준비합니다.

```bash
rosdep update
rosdep install --from-paths src/user_interface src/maker_basic src/gong_basic src/tf2_basic --ignore-src --rosdistro jazzy -r -y
colcon build --symlink-install --packages-select user_interface maker_basic gong_basic tf2_basic
source install/setup.bash
```

### 3. 실행하고 관찰하기 · 약 10분

터미널 A에서 두 Node를 실행합니다.

```bash
ros2 launch maker_basic class_message.launch.py
```

`Published: Class message: 0`, `Received: Class message: 0`처럼 발행·수신 로그가
반복되고 숫자가 증가하는지 확인하세요. 시작 시점에 따라 첫 숫자는 다를 수 있습니다.
터미널 B를 새로 열어 메시지를 직접 읽습니다.

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros_ws/install/setup.bash
ros2 topic echo /message std_msgs/msg/String --once
```

`data: 'Class message: ...'`가 한 번 출력되면 통신을 확인한 것입니다.
새 터미널에서는 두 `source` 명령을 매번 적용합니다. 종료는 터미널 A에서 `Ctrl+C`입니다.

실행이 막히면 `Package not found`는 빌드와 `source`를, 메시지가 없으면 터미널 A의
실행 상태와 양쪽 터미널의 `ROS_DOMAIN_ID` 일치 여부를 확인하세요.
[검증 결과와 실행 환경의 한계](docs/validation.md)도 함께 확인할 수 있습니다.

<a id="demo"></a>

## 직접 실행하는 데모

| 체험 | 확인할 결과 | 코드와 안내 |
|---|---|---|
| 두 Node의 메시지 통신 | 1초마다 발행·수신 로그와 증가하는 숫자 | [Publisher](src/maker_basic/maker_basic/class_message_pub.py) · [Subscriber](src/maker_basic/maker_basic/class_message_sub.py) |
| 움직이는 로봇 관절 | `/joint_states` 변화와 RViz2 팔 회전 | [24~26장 실행 안내](docs/chapters.md#대표-실행) |
| 센서로 벽 따라가기 | Gazebo에서 LaserScan을 읽고 주행 명령 발행 | [27장 설치와 실습](src/wall_follow_lab/README.md) |

RViz2와 Gazebo 데모는 별도의 GUI·시뮬레이터 준비가 필요합니다.
현재 연결된 예제 동영상은 없습니다. 실행 절차와 관찰할 결과는 위 링크에서 확인하세요.

## 체험 다음에는

책은 작은 Python Node를 직접 만드는 과정에서 출발해 통신 방식의 선택,
좌표 변환, 로봇 모델 구성, 센서 기반 주행으로 이어집니다.
명령을 실행한 뒤 무엇을 관찰해야 하는지, 실패했을 때 어디부터 확인하는지 함께 다룹니다.

**[전체 27장 목차 보기](BOOK.md#목차)** · **[전자책·종이책 안내](BOOK.md#purchase)**

동료나 스터디에 소개할 때는 이 저장소 또는 무료 PDF 링크를 공유해 주세요.
다시 실습할 때 찾기 쉽도록 저장소에 Star를 남겨도 좋습니다.
[블로그·SNS·스터디용 소개 문구](docs/share.md)도 준비되어 있습니다.

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

실습 코드, 설치·실행 안내, 책 소개와 목차, **1~3장 무료 SAMPLE PDF**를 제공합니다.
전체 도서 PDF·EPUB, 4장 이후 본문, 원고·삽화 원본, 집필 도구,
비공개 개발 이력, 실물 매니퓰레이터·카메라·AI 모델은 포함하지 않습니다.
이 저장소는 독립된 Git 이력으로 관리합니다.
코드는 기존 Apache License 2.0을 유지합니다. [LICENSE](LICENSE)를 확인하세요.
샘플 PDF의 본문·이미지는 코드 라이선스에 포함되지 않습니다. [샘플 이용 안내](samples/README.md)를 확인하세요.

오류 제보는 [Issues](https://github.com/freshmea/ros2-maker-guide/issues)에 장 번호,
실행 명령, ROS2 버전, 오류 로그를 남겨 주세요. 비밀번호나 개인 정보는 제거해 주세요.
