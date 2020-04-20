import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
    'PROGRAMA',
    'PRINCIPAL',
    'FUNCION',
    'REGRESA',
    'VAR',
    'LEE',
    'ESCRIBE',
    'SI',
    'ENTONCES',
    'SINO',
    'MIENTRAS',
    'HAZ',
    'DESDE',
    'HASTA',
    'ID',
    'INT',
    'FLOAT',
    'ENTERO',
    'FLOTANTE',
    'CARACTER',
    'VOID',
    'NEWLINE',
    'COMENTARIO',
    'IGNORE',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
]


"""
Digito:  [0-9]
Digitos:  Digito+
Numero:  Digitos(\. Digitos)?
Letra: [A-Za-z]
Caracteres: Caracter+
Relop: < | > | <= | >= | <> | ==
Tipo: (Int | Float | Char)
Ws: ( Blank | Nab | Newline)+
"""

def t_COMENTARIO(t):
    r'\%\%.*'
    t.type = 'COMENTARIO'
    return t

def t_IGNORE(t):
    r'\t '
    t.lexer.skip(1)

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_PLUS(t):
    r'\+'
    t.type = 'PLUS'
    return t

def t_MINUS(t):
    r'\-'
    t.type = 'MINUS'
    return t

def t_TIMES(t):
    r'\*'
    t.type = 'TIMES'
    return t

def t_DIVIDE(t):
    r'\/'
    t.type = 'DIVIDE'
    return t

def t_LPAREN(t):
    r'\('
    t.type = 'LPAREN'
    return t

def t_RPAREN(t):
    r'\)'
    t.type = 'RPAREN'
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

def t_LEE(t):
    r'LEE'
    t.type = 'LEE'
    return t

def t_ESCRIBE(t):
    r'ESCRIBE'
    t.type = 'ESCRIBE'
    return t

def t_SI(t):
    r'SI'
    t.type = 'SI'
    return t

def t_ENTONCES(t):
    r'ENTONCES'
    t.type = 'ENTONCES'
    return t

def t_SINO(t):
    r'SINO'
    t.type = 'SINO'
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

def t_CARACTER(t):
    r'[\w\W]'
    t.type = 'CARACTER'
    return t

def t_error(t):
    print("ERROR!")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input('''
PROGRAMA prog

VAR x = 3 + 4

''')

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
