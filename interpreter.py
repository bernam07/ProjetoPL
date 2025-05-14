from tables import tables
from utils import load_csv, save_csv, select_rows, join_tables
from procedures import procedures
from os.path import join
import os

def execute_program(commands):
    for cmd in commands:
        execute_command(cmd)

def execute_command(cmd):
    match cmd:
        case ('import', name, path):
            if not os.path.isfile(path):
                path = os.path.join("data", path)
            tables[name] = load_csv(path)
        case ('export', name, path):
            folder = 'data/ficheiros_criados'
            os.makedirs(folder, exist_ok=True)
            path_with_folder = join(folder, path)
            save_csv(tables[name], path_with_folder)
        case ('discard', name):
            tables.pop(name, None)
        case ('rename', old, new):
            tables[new] = tables.pop(old)
        case ('print', name):
            if name not in tables:
                print(f"A tabela '{name}' não foi encontrada.")
                return
            for row in tables[name]:
                print(row)
        case ('select', fields, table, cond, limit):
            rows = select_rows(tables[table], fields, cond, limit)
            for r in rows:
                print(r)
        case ('create_select', name, query):
            _, fields, table, cond, limit = query
            tables[name] = select_rows(tables[table], fields, cond, limit)
        case ('create_join', name, t1, t2, key):
            tables[name] = join_tables(tables[t1], tables[t2], key)
        case ('procedure', name, body):
            procedures[name] = body
        case ('call', name):
            for c in procedures[name]:
                execute_command(c)