import lexico
import semantico

def analyze_code(code):
    lexer = lexico.lexer
    lexer.input(code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(f"{tok.type}: {tok.value} at line {tok.lineno}")

    errors, _, syntaxs = semantico.analyze_code(code)

    return errors, tokens, syntaxs
