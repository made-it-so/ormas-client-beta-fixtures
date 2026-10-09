from ormas_acceptance import run


def slug(*words):
    result = run(["python3", "slug_cli.py", *words])
    assert result["returncode"] == 0
    return result["output"].strip()


def test_two_words():
    assert slug("Hello", "World") == "hello-world"


def test_collapses_repeated_spaces():
    assert slug("  Many   spaces here ") == "many-spaces-here"


def test_single_word_unchanged():
    assert slug("ormas") == "ormas"
