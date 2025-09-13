# Habit Tracking App (Python)

A minimal, modular backend for tracking habits with daily/weekly periodicities, a simple CLI, JSON persistence, and a functional analytics module.

## Features
- Create, edit, delete habits (daily or weekly)
- Check off completions (timestamps stored)
- JSON persistence (no DB setup needed)
- Functional analytics:
  - List all habits
  - List habits by periodicity
  - Longest streak overall
  - Longest streak for a specific habit
- Unit tests with 4 weeks of predefined data

## Quickstart
```zsh
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python main.py
