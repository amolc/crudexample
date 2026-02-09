# Git Basics: From Initialization to Deployment

This guide covers the fundamental Git workflow for managing a project, starting from scratch and moving through the standard "push" routine.

---

## **1. Starting a New Project**

To begin tracking a project with Git, you must first initialize a repository in your project's root directory.

### **Initialize Git**
Open your terminal, navigate to your project folder, and run:
```bash
git init
```
This creates a hidden `.git` directory that stores all your project's version history.

### **Configure Your Identity**
If you haven't done so, set your username and email (used for commit history):
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## **2. The Core Git Workflow**

The most common routine involves three stages: **Staging**, **Committing**, and **Pushing**.

### **Step 1: Stage Changes**
After creating or modifying files, you need to "stage" them. This tells Git which changes you want to include in the next snapshot.

- **Stage specific files**:
  ```bash
  git add filename.py
  ```
- **Stage all changes**:
  ```bash
  git add .
  ```

### **Step 2: Commit Changes**
A commit is a snapshot of your staged changes at a specific point in time. Every commit must have a descriptive message.
```bash
git commit -m "feat: initial project structure"
```

### **Step 3: Check Status**
At any point, you can see which files are staged, modified, or untracked:
```bash
git status
```

---

## **3. The Push Routine (Remote Deployment)**

To save your code to a remote server (like GitHub, GitLab, or Bitbucket), follow this routine.

### **Connect to a Remote Repository**
If you have a fresh remote repository, link it to your local project:
```bash
git remote add origin https://github.com/username/project-name.git
```

### **The Standard Push Workflow**

1.  **Pull latest changes** (Best practice: always pull before pushing to avoid conflicts):
    ```bash
    git pull origin main
    ```

2.  **Add and Commit your work**:
    ```bash
    git add .
    git commit -m "Brief description of changes"
    ```

3.  **Push to Remote**:
    ```bash
    git push origin main
    ```

---

## **4. Common Git Commands Summary**

| Command | Description |
| :--- | :--- |
| `git init` | Initialize a new local Git repository. |
| `git status` | Show the status of your working directory. |
| `git log` | View the commit history. |
| `git diff` | Show changes between commits, commit and working tree, etc. |
| `git branch` | List, create, or delete branches. |
| `git checkout -b <name>` | Create and switch to a new branch. |
| `git merge <branch>` | Merge a branch into the current branch. |

---

## **Pro Tip: Use a .gitignore File**
Always create a `.gitignore` file in your root directory to prevent sensitive or unnecessary files (like `venv/`, `__pycache__/`, or `.env`) from being tracked.

```text
# Example .gitignore
venv/
*.pyc
.env
db.sqlite3
```
## **5. Branching and Merging**

Branching allows you to develop features, fix bugs, or experiment in a contained area without affecting the main codebase.

### **Working with Branches**

- **Create a new branch**:
  ```bash
  git branch feature-name
  ```
- **Switch to a branch**:
  ```bash
  git checkout feature-name
  ```
- **Create and switch in one command**:
  ```bash
  git checkout -b feature-name
  ```
- **List all branches**:
  ```bash
  git branch
  ```

### **Merging Branches**

Once your work in a branch is complete and tested, you can merge it back into the main branch (usually `main`).

1.  **Switch to the target branch** (e.g., `main`):
    ```bash
    git checkout main
    ```
2.  **Update the target branch**:
    ```bash
    git pull origin main
    ```
3.  **Merge the feature branch**:
    ```bash
    git merge feature-name
    ```
4.  **Resolve Conflicts** (if any):
    If Git cannot automatically merge, it will mark the conflicts in the files. You must manually edit the files to resolve them, then:
    ```bash
    git add <resolved-file>
    git commit -m "fix: resolve merge conflicts"
    ```
5.  **Delete the feature branch** (optional):
    ```bash
    git branch -d feature-name
    ```
