import ply.yacc as yacc
from lexer import tokens

# AST base
def p_program(p):
    """program : commands"""
    p[0] = p[1]

def p_commands(p):
    """commands : commands command
                | command"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_command_import(p):
    """command : IMPORT TABLE ID FROM STRING SEMI"""
    p[0] = ('import', p[3], p[5])

def p_command_export(p):
    """command : EXPORT TABLE ID AS STRING SEMI"""
    p[0] = ('export', p[3], p[5])

def p_command_discard(p):
    """command : DISCARD TABLE ID SEMI"""
    p[0] = ('discard', p[3])

def p_command_rename(p):
    """command : RENAME TABLE ID ID SEMI"""
    p[0] = ('rename', p[3], p[4])

def p_command_print(p):
    """command : PRINT TABLE ID SEMI"""
    p[0] = ('print', p[3])

def p_command_select(p):
    """command : SELECT select_list FROM ID where_clause limit_clause SEMI"""
    p[0] = ('select', p[2], p[4], p[5], p[6])

def p_select_list(p):
    """select_list : ASTERISK
                   | id_list"""
    p[0] = p[1]

def p_id_list(p):
    """id_list : ID
               | ID COMMA id_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_where_clause(p):
    """where_clause : WHERE condition
                    | """
    p[0] = p[2] if len(p) > 1 else None

def p_limit_clause(p):
    """limit_clause : LIMIT NUMBER
                    | """
    p[0] = p[2] if len(p) > 1 else None

def p_condition(p):
    """condition : ID op value
                 | condition AND condition"""
    if len(p) == 4 and p[2] == 'AND':
        p[0] = ('and', p[1], p[3])
    else:
        p[0] = (p[2], p[1], p[3])

def p_op(p):
    """op : EQ
          | NEQ
          | LT
          | GT
          | LE
          | GE"""
    p[0] = p[1]

def p_value(p):
    """value : NUMBER
             | STRING"""
    p[0] = p[1]

def p_command_create_select(p):
    """command : CREATE TABLE ID SELECT select_list FROM ID where_clause limit_clause SEMI"""
    p[0] = ('create_select', p[3], ('select', p[5], p[7], p[8], p[9]))

def p_command_create_join(p):
    """command : CREATE TABLE ID FROM ID JOIN ID USING LPAREN ID RPAREN SEMI"""
    p[0] = ('create_join', p[3], p[5], p[7], p[10])

def p_command_procedure(p):
    """command : PROCEDURE ID DO commands END SEMI"""
    p[0] = ('procedure', p[2], p[4])

def p_command_call(p):
    """command : CALL ID SEMI"""
    p[0] = ('call', p[2])

def p_error(p):
    print(f"Erro de sintaxe na linha {p.lineno}" if p else "Erro de sintaxe")

parser = yacc.yacc()
