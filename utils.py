import csv

def load_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(row for row in f if not row.startswith('#'))
        return list(reader)

def save_csv(data, path):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def select_rows(data, fields, cond, limit):
    def match(row):
        if not cond: return True
        match cond:
            case ('and', c1, c2): return match_cond(c1, row) and match_cond(c2, row)
            case _: return match_cond(cond, row)

    def match_cond(c, row):
        op, key, val = c
        r_val = row[key]
        try: r_val = float(r_val)
        except: pass
        return {
            '=': r_val == val,
            '<>': r_val != val,
            '<': r_val < val,
            '>': r_val > val,
            '<=': r_val <= val,
            '>=': r_val >= val,
        }[op]

    rows = [row for row in data if match(row)]
    if limit: rows = rows[:limit]
    return rows if fields == '*' else [{k: row[k] for k in fields} for row in rows]

def join_tables(t1, t2, key):
    result = []
    for r1 in t1:
        for r2 in t2:
            if r1[key] == r2[key]:
                combined = {**r1, **r2}
                result.append(combined)
    return result
