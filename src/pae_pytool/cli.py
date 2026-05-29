"""Command-line interface for pae-pytool-sample."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from pae_pytool.core import char_count, word_count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pae-pytool", description="Tiny text-statistics CLI.")
    sub = parser.add_subparsers(dest="command", required=True)

    words = sub.add_parser("words", help="Count words.")
    words.add_argument("text", nargs="?", help="Text to analyze (reads stdin if omitted).")

    chars = sub.add_parser("chars", help="Count characters.")
    chars.add_argument("text", nargs="?", help="Text to analyze (reads stdin if omitted).")
    chars.add_argument(
        "--no-spaces", action="store_true", help="Exclude whitespace from the count."
    )

    return parser


def _read_text(arg: str | None) -> str:
    if arg is not None:
        return arg
    return sys.stdin.read()


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    text = _read_text(args.text)
    if args.command == "words":
        print(word_count(text))
    elif args.command == "chars":
        print(char_count(text, include_spaces=not args.no_spaces))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
