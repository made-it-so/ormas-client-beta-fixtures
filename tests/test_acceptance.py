from ormas_acceptance import run


def top(case, n):
    # Inputs are committed under tests/data so the isolated candidate can read them.
    result = run(["python3", "wordfreq_cli.py", f"tests/data/{case}.txt", str(n)])
    assert result["returncode"] == 0
    return result["output"].strip().splitlines()


def test_counts_case_insensitive_and_stopwords():
    assert top("case_and_stopwords", 2) == ["cat 2", "dog 1"]


def test_ties_are_alphabetical():
    assert top("ties", 3) == ["apple 2", "pear 2", "fig 1"]


def test_apostrophes():
    assert top("apostrophes", 3) == ["don't 2", "quoted 1", "tis 1"]


def test_limit_and_digits():
    assert top("digits", 2) == ["v2 3", "x1 2"]
