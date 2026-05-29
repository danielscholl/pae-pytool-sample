import io

from pae_pytool.cli import main


def test_words_subcommand_with_inline_text(capsys):
    rc = main(["words", "hello world"])
    out = capsys.readouterr().out.strip()
    assert rc == 0
    assert out == "2"


def test_chars_subcommand_excludes_spaces_with_flag(capsys):
    rc = main(["chars", "--no-spaces", "a b c"])
    assert rc == 0
    assert capsys.readouterr().out.strip() == "3"


def test_words_reads_stdin_when_text_omitted(capsys, monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("one two three"))
    rc = main(["words"])
    assert rc == 0
    assert capsys.readouterr().out.strip() == "3"
