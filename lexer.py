import ply.lex as lex

reserved = {
    'import': 'IMPORT',
    'export': 'EXPORT',
    'table': 'TABLE',
    'from': 'FROM',
    'as': 'AS',
    'discard': 'DISCARD',
    'rename': 'RENAME',
    'print': 'PRINT',
    'select': 'SELECT',
    'where': 'WHERE',
    'limit': 'LIMIT',
    'create': 'CREATE',
    'join': 'JOIN',
    'using': 'USING',
    'procedure': 'PROCEDURE',
    'do': 'DO',
    'end': 'END',
    'call': 'CALL',
    'and': 'AND',
}

tokens = [
    'ID', 'STRING', 'NUMBER',
    'EQ', 'NEQ', 'LT', 'GT', 'LE', 'GE',
    'COMMA', 'SEMI', 'LPAREN', 'RPAREN', 'ASTERISK'
] + list(reserved.values())

t_ignore = ' \t'

t_EQ = r'='
t_NEQ = r'<>'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_COMMA = r','
t_SEMI = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASTERISK = r'\*'

def t_COMMENT_BLOCK(t):
    r'{-[\s\S]*?-}'
    pass

def t_COMMENT_LINE(t):
    r'--.*'
    pass

def t_STRING(t):
    r'"[^"\n]*"'
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
