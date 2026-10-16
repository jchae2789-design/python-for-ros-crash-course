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

Run these commands one by one. When asked for a password, type your Ubuntu password. Nothing appears on screen while you type it. That is normal.

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git gh
```

Check that Python works:

```bash
python3 --version
```

You should see `Python 3.12.something`.

---

## 3. Install VS Code (your code editor)

```bash
sudo snap install code --classic
```

Start it:

```bash
code
```

In VS Code, open the **Extensions** panel (the icon with four squares on the left, or **Ctrl + Shift + X**). Search for **Python** and install the extension by **Microsoft**.

---

## 4. Create a GitHub account

GitHub is a website that stores code. You will save your work there every day, so your mentor can see it.

1. Go to <https://github.com> and click **Sign up**.
2. Choose a username. Use something professional, for example `kim-minjun-robot`.
3. Send your username to your mentor.

---

## 5. Tell Git who you are

Use your real name and the email of your GitHub account:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

---

## 6. Log in to GitHub from the terminal

```bash
gh auth login
```

Answer the questions with the arrow keys and Enter:

- *Where do you use GitHub?* → **GitHub.com**
- *Preferred protocol?* → **HTTPS**
- *Authenticate Git with your GitHub credentials?* → **Yes**
- *How would you like to authenticate?* → **Login with a web browser**

Copy the code it shows, press Enter, paste the code in the browser and confirm.

---

## 7. Fork and download the course

A **fork** is your own copy of the course on GitHub. You work in your fork.

1. Open the course page: `https://github.com/yosaotniell03/python-for-ros-crash-course`
   (your mentor gives you the exact link).
2. Click **Fork** (top right), then **Create fork**.
3. In your fork, click the **Actions** tab and click **"I understand my workflows, go ahead and enable them"**. This turns on the automatic tests on GitHub.

Now download your fork to your computer. Replace `YOUR-USERNAME`:

```bash
mkdir -p ~/code
cd ~/code
gh repo clone YOUR-USERNAME/python-for-ros-crash-course
cd python-for-ros-crash-course
```

---

## 8. Create a virtual environment

A **virtual environment** (venv) is a private box for the Python packages of this project. Create it once:

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

```bash
code .
```

The `.` means "this folder". If VS Code asks *"Do you trust the authors?"*, click **Yes**.

At the bottom right of VS Code, choose the Python interpreter that has `.venv` in its name. If you do not see it, press **Ctrl + Shift + P**, type `Python: Select Interpreter` and choose `.venv`.

You can open a terminal inside VS Code with **Ctrl + `** (the key left of 1).

---

## 10. Check that everything works

Run the tests for Day 1:

```bash
pytest exercises/week1/tests/test_w1d1.py
```

You should see **2 failed**. That is correct! You have not written any code yet. The tests fail until you solve the exercises.

If you see `command not found: pytest`, your venv is not active. Go back to step 8.

---

## 11. Your first push

Create your first daily log and send it to GitHub:

```bash
cp logs/TEMPLATE.md logs/$(date +%F).md
git add logs
git commit -m "Add first daily log"
git push
```

Open your fork on GitHub in the browser. You should see your new file in the `logs` folder.

**Setup is done.** Start with [Week 1, Day 1](../lessons/week1/day1-terminal-and-first-program.md).
