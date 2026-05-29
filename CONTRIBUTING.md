# Contributing

`main` is protected: **no direct pushes**. Every change lands through a pull
request, and CI (ruff + pytest) must be green before merge.

## Workflow

1. Branch off `main`.
2. Make your change. Add or update tests for any behavior change.
3. Run the checks locally:
   ```bash
   ruff check . && ruff format --check . && pytest
   ```
4. Open a pull request with a conventional-commit title (`feat:`, `fix:`, `docs:`…).

## Conventions

- Keep `core.py` functions small and pure; the CLI layer stays thin.
- Every new branch of behavior gets a test.
- Conventional-commit messages, one-sentence imperative subject.
