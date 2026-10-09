from ormas_acceptance import run


def cli(*args):
    return run(["python3", "inventory_cli.py", *args])


def test_csv_header_and_sorted_rows():
    result = cli("--format", "csv")
    assert result["returncode"] == 0
    lines = result["output"].strip().splitlines()
    assert lines[0] == "sku,name,qty"
    assert [line.split(",")[0] for line in lines[1:]] == ["A-100", "B-200", "C-300"]


def test_csv_quotes_names_with_commas():
    lines = cli("--format", "csv")["output"].strip().splitlines()
    assert 'B-200,"Bolt, M6",120' in lines


def test_table_default_unchanged():
    result = cli()
    assert result["returncode"] == 0
    assert result["output"].splitlines()[1] == "A-100  Anchor        8"


def test_unknown_format_exits_2():
    assert cli("--format", "xml")["returncode"] == 2
