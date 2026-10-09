import re

from timekit.units import SECONDS

_PART = re.compile(r"(\d+)([hm])")


def parse_duration(text):
    total = 0
    for amount, unit in _PART.findall(text.strip().lower()):
        total += int(amount) * SECONDS[unit]
    return total
