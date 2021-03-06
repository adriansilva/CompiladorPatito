import ply.lex as lex
import sys

tokens = [
    'PROGRAMA',
    'PRINCIPAL',
    'FUNCION',
    'REGRESA',
    'VAR',
    'LEE',
    'ESCRIBE',
    'SINO',
    'SI',
    'ENTONCES',
    'MIENTRAS',
    'HAZ',
    'DESDE',
    'HASTA',
    'ID',
    'INT',
    'FLOAT',
    'CHAR',
    'ENTERO',
    'FLOTANTE',
    'CARACT',
    'VOID',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'OPAREN',
    'CPAREN',
    'RELOP',
    'ASSIGN',
    'LOGIC',
    'OBRACKET',
    'CBRACKET',
    'OCORCH',
    'CCORCH',
    'SEMICOLON',
    'OPMATRIZ',
    'COLON',
    'COMA',
    'STRING'
]

"""
Digito:  [0-9]
Digitos:  Digito+
Numero:  Digitos(\. Digitos)?
Letra: [A-Za-z]
Tipo: (Int | Float | Char)

"""

def t_COMMENT(t):
    r'\%\%.*'
    pass

def t_LOGIC(t):
    r'\&\& | \|\|'
    t.type = 'LOGIC'
    return t

def t_RELOP(t):
    r'<= | >= | <> | < | > | =='
    t.type = 'RELOP'
    return t

def t_ASSIGN(t):
    r'='
    t.type = 'ASSIGN'
    return t

def t_COLON(t):
    r'\:'
    t.type = 'COLON'
    return t

def t_IGNORE(t):
    r'\ '
    pass

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_OPMATRIZ(t):
    r'\$ | \¡ | \?'
    t.type = 'OPMATRIZ'
    return t

def t_PLUS(t):
    r'\+'
    t.type = 'PLUS'
    return t

def t_MINUS(t):
    r'\-'
    t.type = 'MINUS'
    return t

def t_MULTIPLY(t):
    r'\*'
    t.type = 'MULTIPLY'
    return t

def t_DIVIDE(t):
    r'\/'
    t.type = 'DIVIDE'
    return t

def t_OBRACKET(t):
    r'\{'
    t.type = 'OBRACKET'
    return t

def t_CBRACKET(t):
    r'\}'
    t.type = 'CBRACKET'
    return t

def t_OCORCH(t):
    r'\['
    t.type = 'OCORCH'
    return t

def t_CCORCH(t):
    r'\]'
    t.type = 'CCORCH'
    return t

def t_COMA(t):
    r'\,'
    t.type = 'COMA'
    return t

def t_SEMICOLON(t):
    r'\;'
    t.type = 'SEMICOLON'
    return t

def t_OPAREN(t):
    r'\('
    t.type = 'OPAREN'
    return t

def t_CPAREN(t):
    r'\)'
    t.type = 'CPAREN'
    return t

def t_STRING(t):
    r'\"[^"]*\"'
    t.type = 'STRING'
    return t

def t_FLOTANTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VOID(t):
    r'VOID'
    t.type = 'VOID'
    return t

def t_PROGRAMA(t):
    r'PROGRAMA'
    t.type = 'PROGRAMA'
    return t

def t_PRINCIPAL(t):
    r'PRINCIPAL'
    t.type = 'PRINCIPAL'
    return t

def t_FUNCION(t):
    r'FUNCION'
    t.type = 'FUNCION'
    return t

def t_REGRESA(t):
    r'REGRESA'
    t.type = 'REGRESA'
    return t

def t_VAR(t):
    r'VAR'
    t.type = 'VAR'
    return t

def t_INT(t):
    r'INT'
    t.type = 'INT'
    return t

def t_FLOAT(t):
    r'FLOAT'
    t.type = 'FLOAT'
    return t

def t_CHAR(t):
    r'CHAR'
    t.type = 'CHAR'
    return t

def t_LEE(t):
    r'LEE'
    t.type = 'LEE'
    return t

def t_ESCRIBE(t):
    r'ESCRIBE'
    t.type = 'ESCRIBE'
    return t

def t_SINO(t):
    r'SINO'
    t.type = 'SINO'
    return t

def t_SI(t):
    r'SI'
    t.type = 'SI'
    return t

def t_ENTONCES(t):
    r'ENTONCES'
    t.type = 'ENTONCES'
    return t

def t_MIENTRAS(t):
    r'MIENTRAS'
    t.type = 'MIENTRAS'
    return t

def t_HAZ(t):
    r'HAZ'
    t.type = 'HAZ'
    return t

def t_DESDE(t):
    r'DESDE'
    t.type = 'DESDE'
    return t

def t_HASTA(t):
    r'HASTA'
    t.type = 'HASTA'
    return t

def t_ID(t):
    r'[A-Za-z][A-Za-z_0-9]*'
    t.type = 'ID'
    return t

def t_CARACT(t):
    r'\'[A-Za-z_0-9$%&/\(\)\"#=\?\¿\´\+\*\-\.\,\{\}\[\]]\''
    t.type = 'CARACT'
    return t

def t_error(t):
    print("ERROR!")
    t.lexer.skip(1)

lexer = lex.lex()
'''

lexer.input(
A=B;
C=D;
)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
'''
