# Undo-Redo Text Editor (simple CLI)

A tiny command-line text editor demonstrating a basic undo/redo system using two stacks.

This repository contains:
- A clean, improved implementation: `undo_redo.py`
- Unit tests: `tests/test_undo_redo.py`
- GitHub Actions workflow to run tests on push
- MIT license and `.gitignore`

## Features
- Append text entries
- Undo/Redo (multi-step)
- Display current text
- Optional save/load to a file

## Quickstart

```bash
# clone
git clone <your-repo-url>
cd <your-repo>

# run
python3 undo_redo.py

# run tests
pip install -r requirements.txt   # (none required, but recommended to use venv)
pytest
