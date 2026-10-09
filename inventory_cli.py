import argparse

from inventory.data import ITEMS
from inventory.report import table

parser = argparse.ArgumentParser()
parser.add_argument("--format", default="table")
args = parser.parse_args()
if args.format != "table":
    raise SystemExit(2)
print(table(ITEMS))
