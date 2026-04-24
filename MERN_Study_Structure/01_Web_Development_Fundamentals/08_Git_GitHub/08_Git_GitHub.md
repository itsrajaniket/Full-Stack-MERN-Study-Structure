# Git & GitHub

## 📚 Curriculum Checklist
- [x] Version Control Basics
- [x] GitHub Workflow (Commit, Branches, PRs, Issues)
- [x] Git Docs

## 📝 Detailed Notes

### 1. Version Control Concepts
- **Repository**: The project folder tracked by Git.
- **Commit**: A snapshot of your project at a specific point in time.
- **HEAD**: A pointer to the current commit you are on.

### 2. Core Commands
- `git init`: Create a new local repository.
- `git clone <url>`: Copy a remote repository.
- `git status`: See which files are staged, unstaged, or untracked.
- `git add <file>`: Stage changes for the next commit.
- `git commit -m "msg"`: Save staged changes to history.
- `git log`: View commit history.

### 3. Remote Operations
- `git remote add origin <url>`: Connect local repo to remote.
- `git push origin <branch>`: Upload local commits.
- `git pull origin <branch>`: Download and merge remote changes.

### 4. Branching & Merging
- `git branch`: List branches.
- `git checkout -b <name>`: Create and switch to a new branch.
- `git merge <name>`: Combine a branch into the current one.
- `git stash`: Temporarily save uncommitted changes.

### 5. Advanced Git
- `git rebase`: Re-apply commits on top of another base tip.
- `git reset --hard <hash>`: Revert project state to a specific commit.
- `git cherry-pick <hash>`: Apply a single commit from another branch.

### 6. GitHub Features
- **Pull Requests (PR)**: Proposing changes and code review.
- **Issues**: Tracking bugs, tasks, and feature requests.
- **GitHub Actions**: CI/CD automation.
- **GitHub Pages**: Free hosting for static sites.


## 🎓 Important Interview Questions

### Q1: What is the difference between Git and GitHub?
- **Git**: The software tool that manages version control locally on your machine.
- **GitHub**: A cloud-based hosting service that lets you manage Git repositories online.

### Q2: What is the difference between `git pull` and `git fetch`?
- **`git fetch`**: Downloads the latest changes from the remote but does **not** merge them into your local branch.
- **`git pull`**: Performs a `git fetch` followed immediately by a `git merge`.

### Q3: Explain "Merge Conflicts".
A merge conflict occurs when two branches have made changes to the same line of a file, or when one branch deleted a file that another branch modified. Git cannot decide which version to keep, so the developer must manually resolve it.

### Q4: What is the difference between `git merge` and `git rebase`?
- **Merge**: Creates a new "merge commit" that combines the history of both branches.
- **Rebase**: Moves the entire branch to begin on the tip of the target branch, rewriting the project history by creating brand new commits.

### Q5: What does `git stash` do?
It temporarily shelves (or stashes) changes you've made to your working copy so you can work on something else, and then come back and re-apply them later.


## ❓ Questions & Doubts
- [ ]

---

[⬅️ Previous: Typescript](../../MERN_Study_Structure/01_Web_Development_Fundamentals/07_Typescript/07_Typescript.md) | [🏠 Home](../../README.md) | [Next: Tech Stack HTML CSS JavaScript TypeScript Tailwind CSS ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/09_Tech_Stack_HTML_CSS_JavaScript_TypeScript_Tailwind_CSS/09_Tech_Stack_HTML_CSS_JavaScript_TypeScript_Tailwind_CSS.md)