import ply.lex as lex

# Lista de tokens
tokens = (
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'STRING',
    'PUBLIC', 'CLASS', 'STATIC', 'VOID', 'MAIN', 'PRINTLN', 'DOT', 'COMMA'
)

# Reglas de expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_DOT = r'\.'
t_COMMA = r','
t_STRING = r'\"([^\\\n]|(\\.))*?\"'

# Reglas de expresiones regulares con acciones
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = {
        'public': 'PUBLIC',
        'class': 'CLASS',
        'static': 'STATIC',
        'void': 'VOID',
        'main': 'MAIN',
        'System': 'ID',
        'out': 'ID',
        'println': 'PRINTLN'
    }.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Definir la regla de nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
