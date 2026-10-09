import json
import sys

from deploycheck.rules import check

errors = check(json.load(open(sys.argv[1])))
print("\n".join(errors) if errors else "OK")
sys.exit(1 if errors else 0)
