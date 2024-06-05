# oss_personal_project

# 구현 목표
###  본 프로젝트는 제리맥 래티프가 개발한 '큐브'(Jerimac Ratliff's Cube)라는 게임이 원형으로 여겨지는 Microsoft Windows의 기본 게임 중 하나인 지뢰찾기(Minesweeper)를 pygame으로 구현하는 것이 목표이다. 지뢰찾기에서 지뢰는 무작위로 배치되고, 게임의 핵심 로직은 사용자의 마우스 좌클릭으로 칸을 열거나 우클릭 깃발을 표시하는 것이다. 지뢰가 있는 칸을 열면 게임에서 패배하게 되며, 게임의 승리 조건은 모든 지뢰가 아닌 칸을 여는 것이다.

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

5. 재부팅 이후 python main.py를 실행하면 게임 창이 뜨면서 실행됨. (현재 환경에서 python3 main.py가 작동하지 않아 python main.py로 구동함)


# 실행 예시
<span style="color:red">동영상 업로드 시 gif로 변환 후 링크를 삽입</span>
<span style="color:red">아래 홈페이지 참고 : https://onlydev.tistory.com/15 </span>

![example](https://github.com/RmKuma/oss_personal_project_phase1/assets/20412048/98ecfe0c-34c5-4592-86e9-defded705a36)

# 코드 설명
## main.py
### class ~~~
- Description : ~~~
  1. 

### class ~~~
- Description : ~~~
  1. 
 

# TODO List
