from ormas_acceptance import run


def seconds(text):
    result = run(["python3", "duration_cli.py", text])
    assert result["returncode"] == 0
    return int(result["output"].strip())


def test_hours_and_minutes():
    assert seconds("1h30m") == 5400


def test_seconds_only():
    assert seconds("45s") == 45


def test_all_units():
    assert seconds("2h5m10s") == 7510


def test_hours_regression():
    assert seconds("3h") == 10800
