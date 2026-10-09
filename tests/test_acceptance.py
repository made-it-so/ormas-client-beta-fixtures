from ormas_acceptance import run


def codes(case):
    # Inputs are committed under tests/data so the isolated candidate can read them.
    result = run(["python3", "config_check.py", f"tests/data/{case}.json"])
    return result["returncode"], result["output"].strip().splitlines()


def test_valid_config_ok():
    assert codes("good") == (0, ["OK"])


def test_missing_key_e1():
    assert codes("missing_url")[1] == ["E1"]


def test_port_range_e2():
    assert codes("port_70000") == (1, ["E2"])
    assert codes("port_string") == (1, ["E2"])


def test_https_e3():
    assert codes("http_url") == (1, ["E3"])


def test_retries_e4():
    assert codes("retries_9") == (1, ["E4"])
    assert codes("retries_true") == (1, ["E4"])


def test_duplicate_replicas_e5():
    assert codes("duplicate_replicas") == (1, ["E5"])


def test_multiple_errors_sorted():
    assert codes("multiple_errors") == (1, ["E2", "E3", "E4"])
