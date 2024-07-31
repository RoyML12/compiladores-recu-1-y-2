import re

def analyze_code(code):
    errors = []
    tokens = []
    syntaxs = []

    open_braces_count = 0
    close_braces_count = 0
    open_parens_count = 0
    close_parens_count = 0

    # Palabras reservadas y sus contextos esperados
    reserved_patterns = [
        ('public class', '{'),
        ('public static void main', '('),
        ('System.out.println', ';')
    ]

    # Simulación de análisis léxico, sintáctico y semántico
    lines = code.split('\n')
    for lineno, line in enumerate(lines, start=1):
        tokens.append(f"Tokenized: {line}")

        # Contar paréntesis y llaves para verificación global
        open_parens_count += line.count('(')
        close_parens_count += line.count(')')
        open_braces_count += line.count('{')
        close_braces_count += line.count('}')

        # Verificación de punto y coma al final de las líneas relevantes
        if line.strip() and not line.strip().endswith(';') and not line.strip().endswith('{') and not line.strip().endswith('}'):
            if not line.strip().startswith('//'):  # Ignorar comentarios
                errors.append(f"Syntax Error at line {lineno}: Missing semicolon (;)")

        # Verificación de patrones esperados en el contexto adecuado
        for pattern, next_char in reserved_patterns:
            if pattern in line:
                # Verificar que el siguiente carácter esperado esté en la misma línea
                if next_char not in line:
                    errors.append(f"Syntax Error at line {lineno}: Expected '{next_char}' after '{pattern}'")

        syntaxs.append(f"Syntax checked: {line}")

    # Verificación global de paréntesis y llaves
    if open_parens_count != close_parens_count:
        errors.append("Global Syntax Error: Unmatched parentheses")

    if open_braces_count != close_braces_count:
        errors.append("Global Syntax Error: Unmatched braces")

    # Verificación general de palabras clave ausentes en el código completo
    if 'public class' not in code:
        errors.append("Error: Falta 'public class'")
    if 'public static void main' not in code:
        errors.append("Error: Falta 'public static void main'")

    return errors, tokens, syntaxs