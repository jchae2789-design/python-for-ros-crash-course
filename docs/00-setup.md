# 설치 및 준비: 컴퓨터 준비하기

첫날에 **한 번만** 진행해요. 약 1–2시간 걸려요. 사용할 컴퓨터의 운영 체제는 **Ubuntu 24.04**로, ROS 2가 사용하는 운영 체제와 같아요.

어느 단계가 잘되지 않으면 건너뛰지 마세요. 정확한 오류 메시지를 적고 멘토에게 물어보세요.

---

## 1. Ubuntu 터미널 열기

**Ctrl + Alt + T**를 누르세요. 커서가 깜박이는 창이 열려요. 이 창이 **Ubuntu 터미널**이에요. 별도의 터미널 창은 VS Code를 설치하기 전인 준비 과정의 첫 부분에서만 사용해요. 여기에 명령을 입력하고 **Enter**를 눌러 실행해요.

이 안내에서 아래와 같은 상자는 "Ubuntu 터미널에 입력하고 Enter를 누르세요"라는 뜻이에요.

```bash
echo hello
```

터미널에 `hello`가 나와야 해요.

> **도움말:** Ubuntu 터미널에서 복사는 **Ctrl + Shift + C**, 붙여 넣기는 **Ctrl + Shift + V**예요(Ctrl + C / Ctrl + V가 아니에요).

---

## 2. 도구 설치하기

Ubuntu 터미널에 다음 명령을 한 줄씩 입력하고, 각 명령 뒤에 Enter를 누르세요. 비밀번호를 물어보면 Ubuntu 비밀번호를 입력하세요. 입력하는 동안 화면에 아무것도 나타나지 않아도 정상이에요.

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git gh
```

Ubuntu 터미널에 `python3 --version`을 입력해서 설치된 파이썬 버전을 확인하세요.

```bash
python3 --version
```

`Python 3.12.`로 시작하는 버전이 나와야 해요.

---

## 3. VS Code 설치하기(코드 편집기)

Ubuntu 터미널에 아래 명령을 입력하세요. 설치가 끝나면 Ubuntu 터미널 프롬프트가 다시 나타나요.

```bash
sudo snap install code --classic
```

Ubuntu 터미널에 `code`를 입력해서 VS Code 편집기를 여세요.

```bash
code
```

VS Code 창에서 **Ctrl + `**(숫자 1 왼쪽 키)를 누르거나 **Terminal → New Terminal** 메뉴를 선택해서 통합 터미널을 여세요. 편집기 아래쪽 패널에 나타나요. 별도로 열었던 Ubuntu 터미널은 닫으세요. 이제부터 이 안내의 모든 명령은 **VS Code 터미널**에 입력하세요.

---

## 4. GitHub 계정 확인하기

첫날 멘토에게 받은 인쇄물 **0일차: 시작하기 전에**를 보고 GitHub 계정을 이미 만들었어요. 사용자 이름은 그 인쇄물에 적혀 있어요.

1. 브라우저에서 <https://github.com>에 접속하세요.
2. 브라우저의 GitHub 페이지 오른쪽 위를 확인하세요.
   - 프로필 사진(작고 둥근 아이콘)이 보이면 로그인된 상태예요.
   - **Sign in**이 보이면 클릭하고 0일차에 사용한 이메일과 비밀번호로 로그인하세요.
3. 아직 GitHub 계정이 **없다면** 여기서 멈추고 멘토에게 0일차 인쇄물을 요청하세요. 6단계에서 계정이 필요해요.

---

## 5. Git에 사용자 정보 등록하기

VS Code 터미널에 다음 명령을 순서대로 입력하세요. `Your Name`은 실제 이름으로, `you@example.com`은 GitHub 이메일 주소로 바꾸세요. 각 명령은 아무것도 출력하지 않고 VS Code 터미널 프롬프트로 돌아와요.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

---

## 6. VS Code 터미널에서 GitHub에 로그인하기

VS Code 터미널에 `gh auth login`을 입력하면 로그인 질문이 나와요.

```bash
gh auth login
```

VS Code 터미널에서 방향키로 다음 답을 선택하고, 답을 고를 때마다 Enter를 누르세요.

- **Where do you use GitHub?** → **GitHub.com**
- **Preferred protocol?** → **HTTPS**
- **Authenticate Git with your GitHub credentials?** → **Yes**
- **How would you like to authenticate?** → **Login with a web browser**

`gh auth login`이 보여 주는 일회용 코드를 복사하세요. Enter를 눌러 브라우저에서 GitHub 로그인 페이지를 여세요.
브라우저의 코드 입력란에 코드를 붙여 넣고 **Continue**를 클릭하세요.

브라우저에서 GitHub CLI 접근을 승인하세요. 터미널에 로그인되었다는 확인 메시지가 나와야 해요.

---

## 7. 과정 저장소 포크하고 내려받기

**포크**는 GitHub에 만드는 나만의 과정 저장소 복사본이에요. 실습은 이 포크에서 진행해요.

1. 브라우저에서 과정 페이지 `https://github.com/yosaotniell03/python-for-ros-crash-course`를 여세요.
   (정확한 링크는 멘토가 알려 줘요.)
2. 브라우저의 과정 GitHub 페이지 오른쪽 위에서 **Fork**(포크)를 클릭하고 **Create fork**를 클릭하세요. GitHub에 과정 저장소의 복사본이 열려요.
3. 포크에서 **Actions** 탭을 클릭하고 **"I understand my workflows, go ahead and enable them"**을 클릭하세요. GitHub에서 자동 테스트가 켜져요.

VS Code 터미널에 다음 명령을 순서대로 입력해서 포크를 내려받으세요. `YOUR-USERNAME`은 GitHub 사용자 이름으로 바꾸세요. 마지막 `cd` 명령은 VS Code 터미널의 현재 폴더를 `~/code/python-for-ros-crash-course`로 바꿔요.

```bash
mkdir -p ~/code
cd ~/code
gh repo clone YOUR-USERNAME/python-for-ros-crash-course
cd python-for-ros-crash-course
```

---

## 8. 가상 환경 만들기

**가상 환경(venv)**은 이 프로젝트의 파이썬 패키지만 따로 담아 두는 상자와 같아요. VS Code 터미널에 다음 명령을 순서대로 입력하세요. 가상 환경을 만들고 활성화해요.
그런 다음 [`requirements.txt`](../requirements.txt)에 나열된 패키지를 설치해요.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`source .venv/bin/activate`를 실행하면 프롬프트 앞에 `(.venv)`가 붙어요. 상자가 활성화되었다는 뜻이에요.

---

## 9. VS Code에서 과정 폴더 열기

VS Code 터미널에 `code .`을 입력해서 과정 폴더를 VS Code에서 여세요.

```bash
code .
```

`.`은 "현재 폴더"라는 뜻이에요. 또는 VS Code에서 **File → Open Folder**를 선택하고 `~/code/python-for-ros-crash-course`를 고르세요. VS Code에서 **"Do you trust the authors?"**라고 물어보면 **Yes**를 클릭하세요. VS Code에서 **Microsoft**의 권장 **Python** 확장 프로그램을 설치하라는 안내가 나오면 설치하세요.

VS Code 오른쪽 아래에서 이름에 `.venv`가 들어간 파이썬 인터프리터를 선택하세요.
인터프리터가 보이지 않으면 **Ctrl + Shift + P**를 누르세요.
**Python: Select Interpreter**를 입력하고 `.venv`를 선택하세요.

**Ctrl + `**(숫자 1 왼쪽 키)를 누르거나 **Terminal → New Terminal**을 선택해서 **VS Code 터미널**을 여세요. 과정 폴더에서 시작해요. 프롬프트 앞에 `(.venv)`가 있는지 확인하세요. 없으면 터미널의 **휴지통 아이콘**으로 닫고 새 터미널을 여세요. 새 프롬프트에도 `(.venv)`가 없으면 VS Code 터미널에 다음 명령을 입력하세요.

```bash
source .venv/bin/activate
```

이후의 모든 명령도 이 VS Code 터미널에서 실행하세요. 파일은 터미널 위의 VS Code 편집기에서 수정하세요.

---

## 10. 제대로 동작하는지 확인하기

VS Code 터미널에서 [`test_w1d1.py`](../exercises/week1/tests/test_w1d1.py)의 1일차 테스트를 실행하세요.

```bash
pytest exercises/week1/tests/test_w1d1.py
```

**2 failed**가 나와야 해요. 이 상태가 맞아요! 아직 코드를 작성하지 않았기 때문이에요. 연습 문제를 풀기 전까지는 테스트가 실패해요.

`command not found: pytest`가 나오면 가상 환경이 활성화되지 않은 거예요. 9단계에서 안내한 터미널 활성화 방법을 따라 하세요.

---

## 11. 첫 푸시하기

아래 명령으로 [`logs/TEMPLATE.md`](../logs/TEMPLATE.md)를 오늘 날짜의 실습 일지로 복사하세요.
VS Code 터미널에 명령을 순서대로 입력하세요. 일지를 커밋하고 GitHub 포크로 보내는 명령도 포함돼 있어요.

```bash
cp logs/TEMPLATE.md logs/$(date +%F).md
git add logs
git commit -m "Add first daily log"
git push
```

브라우저에서 GitHub의 포크를 여세요. [`logs`](../logs/) 폴더에 새 파일이 보여야 해요.

**설치 및 준비를 마쳤어요.** VS Code 편집기에서 [progress/week1.md](../progress/week1.md)를 여세요.
설치 및 준비 항목 옆의 `[ ]`를 `[x]`로 바꾸고 **Ctrl + S**로 저장하세요.
그런 다음 아직 체크하지 않은 다음 단계를 읽으세요.
