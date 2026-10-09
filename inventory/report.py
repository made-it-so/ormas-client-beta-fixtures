def rows(items):
    return sorted(items, key=lambda item: item["sku"])


def table(items):
    lines = [f"{'SKU':<6} {'NAME':<10} {'QTY':>4}"]
    for item in rows(items):
        lines.append(f"{item['sku']:<6} {item['name']:<10} {item['qty']:>4}")
    return "\n".join(lines)
