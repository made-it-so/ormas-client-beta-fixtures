REQUIRED = ("name", "url", "port", "retries")


def check(config):
    errors = set()
    if any(key not in config for key in REQUIRED):
        errors.add("E1")
    return sorted(errors)
