# oss_personal_project

# 구현 목표
###  본 프로젝트는 제리맥 래티프가 개발한 '큐브'(Jerimac Ratliff's Cube)라는 게임이 원형으로 여겨지는 Microsoft Windows의 기본 게임 중 하나인 지뢰찾기(Minesweeper)를 pygame으로 구현하는 것이 목표이다. 지뢰찾기에서 지뢰는 무작위로 배치되고, 게임의 핵심 로직은 사용자의 마우스 좌클릭으로 칸을 열거나 우클릭 깃발을 표시하는 것이다. 지뢰가 있는 칸을 열면 게임에서 패배하게 되며, 게임의 승리 조건은 모든 지뢰가 아닌 칸을 열고, 그 외의 칸 전부에 깃발 표시를 마치는 것이다.

# 구현 기능
* pygame, box2d 기반 게임 board(환경) 구현

# Reference
[1] https://github.com/pybox2d/pybox2d "pybox2d" 

[2] https://github.com/pygame/pygame "pygame"

# 지원 Operating Systems 및 실행 방법

## 지원 Operating Systems
|OS| 지원 여부 |
|-----|--------|
|windows | :o:  |
| Linux  | :x: |
|MacOS  | :x:  |

## 실행 방법
### Windows

1. python3.12를 설치한다
2. swiging을 설치한다
```
1. https://sourceforge.net/projects/swig/files/swigwin/swigwin-3.0.2/swigwin-3.0.2.zip/download 에서 파일 다운로드

2. C:\ 경로에 압축해제

3. 시작 > 시스템 환경변수 > 환경 변수... > 시스템 변수, Path, 편집 > 새로만들기, 편집 C:\swigwin-3.0.2 추가 
```
3. Microsoft Visual c++ Build Tools 설치
```
1. https://visualstudio.microsoft.com/ko/visual-cpp-build-tools/ 에서   Build Tools 다운로드 후 실행

2. Visual Studio Installer가 실행 된 경우 해당 버전의 "수정(Modify)" 클릭

3. Desktop & Mobile 에서 c++ build Tools 체크 표시 이후 설치

4. 시스템 재부팅
```
4. powershell 창에서 아래 pip3 library를 설치

```
pip3 install pygame
pip3 install ~~~ // 추가예정
```

5. 재부팅 이후 python main.py를 실행하면 게임 초기창이 뜬다 (현재 환경에서 python3 main.py가 작동하지 않아 python main.py로 구동함)

6. 프롬프트 창에 1~3 중 하나의 값 입력으로 해당 난이도의 게임이 실행됨


# 실행 예시
python main.py로 실행시 아래와 같이 난이도 선택 기능 활성화
프롬프트 창에서 1 or 2 or 3 입력으로 해당 난이도의 지뢰찾기 게임 시작

<img width="399" alt="1" src="https://github.com/aiden0105/oss_personal_project/assets/54185322/8bdad159-1aa3-4991-ae84-09b2b3fb5cd2">

![mine](https://github.com/aiden0105/oss_personal_project/assets/54185322/1c4206d8-1edc-4c15-8c1f-01e3d2d3ecbe)


# 코드 설명
## main.py
### class Score
- Description : 게임 내에서 점수와 타이머를 관리하는 클래스
  1. Def init: 점수와 타이머를 초기화하고, 폰트 및 화면 설정을 수행함
  2. Def update_score_for_open_cell: 셀이 열릴 때 점수를 업데이트함
  3. Def apply_game_over_penalty: 게임 오버 시 점수에서 페널티를 적용함
  4. Def display_score: 현재 점수와 경과 시간을 화면에 표시함
  5. Def reset: 게임 재시작 시 점수와 타이머를 리셋함

### class Minesweeper
- Description : 지뢰 찾기 게임의 주 로직과 사용자 상호작용을 처리하는 메인 클래스
  1. Def init: 게임 초기 설정과 화면 구성을 초기화함
  2. Def choose_difficulty: 난이도를 선택하고 관련 설정을 적용함
  3. Def reset: 게임 보드와 변수들을 초기 상태로 리셋함
  4. Def place_mines: 지뢰를 무작위 위치에 배치함
  5. Def handle_mouse_input: 마우스 입력을 처리하여 셀을 열거나 깃발을 표시함
  6. Def open_cell: 사용자가 셀을 클릭했을 때 해당 셀을 열고, 만약 셀에 지뢰가 있다면 게임 오버를 처리하 고, 주변에 지뢰가 없다면 인접한 셀들도 자동으로 연다.
  7. Def open_adjacent_cells: 열린 셀 주변에 지뢰가 없는 경우 인접한 셀들을 재귀적으로 엽니다. 이 함수는 주변 셀들을 안전하게 열기 위해 open_cell을 호출한다.
  8. Def toggle_flag: 사용자가 오른쪽 마우스 버튼을 클릭할 때 해당 셀에 깃발을 표시하거나 제거합니다. 깃발은 지뢰가 있다고 추정되는 위치에 사용자가 표시할 수 있다.
  9. Def draw_board: 게임 보드를 시각적으로 표현함
 

# TODO List
* 남은 지뢰 개수 표시하기
* 상단부 표시란에 현재 난이도 표시하기
