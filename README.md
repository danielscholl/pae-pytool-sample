# pae-pytool-sample

A tiny text-statistics command-line tool. This repo exists as a **sample target**
for exercising the [`plan-act-evaluate`](https://github.com/danielscholl/keelson)
Keelson workflow: it has a real test suite, CI that runs on every pull request, and
`main` is protected — changes land through a PR, never a direct push.

## What it does

```bash
pae-pytool words "hello world"      # -> 2
pae-pytool chars "hello world"      # -> 11
pae-pytool chars --no-spaces "a b"  # -> 2
echo "piped text here" | pae-pytool words
```

## Develop

Requires Python 3.10+.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Verify (the checks CI runs)

```bash
ruff check .           # lint
ruff format --check .  # format
pytest                 # tests
```

All three must pass before a PR can merge.

## Layout

| Path | Role |
|------|------|
| `src/pae_pytool/core.py` | Pure text-stat functions |
| `src/pae_pytool/cli.py` | argparse CLI wiring |
| `tests/` | pytest suite |
| `.github/workflows/ci.yml` | CI: ruff + pytest on PR |
