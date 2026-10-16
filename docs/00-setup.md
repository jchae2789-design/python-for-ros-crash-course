# Setup: get your computer ready

You do this **once**, on your first day. It takes about 1–2 hours. Your computer runs **Ubuntu 24.04**, which is the same system that ROS 2 uses.

If a step does not work, do not skip it. Write down the exact error message and ask your mentor.

---

## 1. Open the terminal

Press **Ctrl + Alt + T**. A window with a blinking cursor opens. This is the **terminal**. You type commands here and press **Enter** to run them.

In this guide, a box like the one below means "type this into the terminal and press Enter":

```bash
echo hello
```

The terminal should answer `hello`.

> **Tip:** In the terminal, copy is **Ctrl + Shift + C** and paste is **Ctrl + Shift + V** (not Ctrl + C / Ctrl + V).

---

## 2. Install the tools

In the terminal, type these commands one by one and press Enter after each command. When asked for a password, type your Ubuntu password. Nothing appears on screen while you type it. That is normal.

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git gh
```

In the terminal, type `python3 --version` to check the installed Python version:

```bash
python3 --version
```

You should see `Python 3.12.something`.

---

## 3. Install VS Code (your code editor)

In the terminal, type the command below. When the installation finishes, the terminal prompt returns.

```bash
sudo snap install code --classic
```

In the terminal, type `code` to open the VS Code editor:

```bash
code
```

In VS Code, open the **Extensions** panel (the icon with four squares on the left, or **Ctrl + Shift + X**). Search for **Python** and install the extension by **Microsoft**.

---

## 4. Create a GitHub account

GitHub is a website that stores code. You will save your work there every day, so your mentor can see it.

1. In your browser, go to <https://github.com> and click **Sign up**.
2. On the GitHub sign-up page in your browser, choose a username and finish the account form. Use something professional, for example `kim-minjun-robot`.
3. Send your username to your mentor.

---

## 5. Tell Git who you are

In the terminal, type these commands in order. Replace `Your Name` with your real name and `you@example.com` with your GitHub email address. Each command returns to the terminal prompt without output:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

---

## 6. Log in to GitHub from the terminal

In the terminal, type `gh auth login` to display the login questions:

```bash
gh auth login
```

In the terminal, select these answers with the arrow keys and press Enter after each answer:

- *Where do you use GitHub?* → **GitHub.com**
- *Preferred protocol?* → **HTTPS**
- *Authenticate Git with your GitHub credentials?* → **Yes**
- *How would you like to authenticate?* → **Login with a web browser**

Copy the one-time code shown by `gh auth login`. Press Enter to open the GitHub login page in your browser.
Paste the code into the browser's code field. Click **Continue**.

Approve GitHub CLI access in the browser. The terminal should confirm that you are logged in.

---

## 7. Fork and download the course

A **fork** is your own copy of the course on GitHub. You work in your fork.

1. In your browser, open the course page: `https://github.com/yosaotniell03/python-for-ros-crash-course`
   (your mentor gives you the exact link).
2. On the course GitHub page in your browser, click **Fork** (top right), then **Create fork**. GitHub opens your copy of the course.
3. In your fork, click the **Actions** tab and click **"I understand my workflows, go ahead and enable them"**. This turns on the automatic tests on GitHub.

In the terminal, type these commands in order to download your fork. Replace `YOUR-USERNAME` with your GitHub username. The final `cd` command puts the terminal in `~/code/python-for-ros-crash-course`:

```bash
mkdir -p ~/code
cd ~/code
gh repo clone YOUR-USERNAME/python-for-ros-crash-course
cd python-for-ros-crash-course
```

---

## 8. Create a virtual environment

A **virtual environment** (venv) is a private box for the Python packages of this project. Type these commands in order. They create and activate the venv.
Then they install the packages listed in [`requirements.txt`](../requirements.txt):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After `source .venv/bin/activate`, your prompt starts with `(.venv)`. This means the box is active.

> **Important:** every time you open a new terminal, go to the course folder and activate the venv again:
>
> ```bash
> cd ~/code/python-for-ros-crash-course
> source .venv/bin/activate
> ```

---

## 9. Open the course in VS Code

In the terminal, type `code .` to open the course folder in VS Code:

```bash
code .
```

The `.` means "this folder". If VS Code asks *"Do you trust the authors?"*, click **Yes**.

At the bottom right of VS Code, choose the Python interpreter with `.venv` in its name.
If no interpreter appears, press **Ctrl + Shift + P**.
Type `Python: Select Interpreter`. Choose `.venv`.

You can open a terminal inside VS Code with **Ctrl + `** (the key left of 1).

---

## 10. Check that everything works

Run the Day 1 tests in [`test_w1d1.py`](../exercises/week1/tests/test_w1d1.py):

```bash
pytest exercises/week1/tests/test_w1d1.py
```

You should see **2 failed**. That is correct! You have not written any code yet. The tests fail until you solve the exercises.

If you see `command not found: pytest`, your venv is not active. Go back to step 8.

---

## 11. Your first push

Copy [`logs/TEMPLATE.md`](../logs/TEMPLATE.md) to today's dated log with the commands below.
Type the commands in order. They also commit the log and send the log to your GitHub fork:

```bash
cp logs/TEMPLATE.md logs/$(date +%F).md
git add logs
git commit -m "Add first daily log"
git push
```

Open your fork on GitHub in the browser. You should see your new file in the [`logs`](../logs/) folder.

**Setup is done.** In VS Code, open [progress/week1.md](../progress/week1.md).
Change `[ ]` to `[x]` beside setup. Save with **Ctrl + S**.
Then read the next unchecked step.
