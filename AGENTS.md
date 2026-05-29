# AGENTS.md

Sample repo for the plan-act-evaluate workflow. Python 3.10+.

## Setup

```bash
pip install -e ".[dev]"
```

## Verify commands

```bash
ruff check .           # lint
ruff format --check .  # format
pytest                 # tests
```

## Rules

- `main` is protected — land changes via pull request, never push to `main`.
- Add a test for every behavior change.
- Conventional-commit messages.
