import ply.yacc as yacc
from lexico import tokens

def p_program(p):
    '''program : PUBLIC CLASS ID LBRACE main_method RBRACE'''
    p[0] = ('program', p[3], p[5])

def p_main_method(p):
    '''main_method : PUBLIC STATIC VOID MAIN LPAREN STRING LBRACK RBRACK ID RPAREN block'''
    p[0] = ('main_method', p[11])

def p_block(p):
    '''block : LBRACE statements RBRACE'''
    p[0] = ('block', p[2])

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : PRINTLN LPAREN STRING RPAREN SEMI'''
    p[0] = ('println', p[3])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
        parser.errok()
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
