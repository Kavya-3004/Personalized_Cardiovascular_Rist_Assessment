# Scripts & Utilities

This folder contains developer and repository automation utilities.

## 📜 `create_git_history.py`

This script sets up your Git repository and builds a realistic, chronological commit history of **up to ~106 commits** across the 12 phases of project development.

### How to Run:

```bash
# Basic run with your Git username and email:
python scripts/create_git_history.py --author-name "Your Name" --author-email "your-email@example.com"

# Or simply run without arguments to use your existing Git config:
python scripts/create_git_history.py
```

### Options:
* `--author-name`: Name to associate with Git commits.
* `--author-email`: Email to associate with Git commits (make sure this matches your GitHub account email so your commits count on your GitHub contribution graph!).
* `--days`: Number of days in the past to distribute the commits across (default: 21 days).
* `--branch`: Primary branch name (default: `main`).
