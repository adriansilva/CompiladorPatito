"""
Todo el lexer funciona igual. Agregué algunos otros elementos como los operadores
de logica (&& y ||), brackets y los operadores de matrices. Intente seguirle con
el YACC y cree algo en base a la documentación pero no funciona. En sí ya tengo
declaradas las reglas para expresión. Cambié un poco las reglas, porque no es
necesario tener tantas reglas llamadas "termino". En sí, puedes tener todos los
operadores en un mismo set, y les añades precedencia en la función de precedence
que se ve más abajo. El problema es que al tratar de parsear un string, la variable
'p' no contiene nada. Entonces no puedo trabajar con nada que arroje yacc. Si te fijas
hay un nuevo documento llamado parser.out. Ahí se puede ver todo lo que hace el parser
Ya es muy tarde y no tuve mucho tiempo de observarlo para ver si encontraba algo.
Si puedes dale una repasada a todo lo que codié del YACC y fijate si puedes arreglar
el bug. Nuevamente el bug es que las variables P tienen valores en [0] y [1] como None.
"""




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
    'MULTIPLY',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'RELOP',
    'ASSIGN',
    'LOGIC',
    'OBRACKET',
    'CBRACKET',
    'SEMICOLON',
    'OPMATRIZ'
]


"""
Digito:  [0-9]
Digitos:  Digito+
Numero:  Digitos(\. Digitos)?
Letra: [A-Za-z]
Tipo: (Int | Float | Char)

"""

def t_COMENTARIO(t):
    r'\%\%.*'
    t.type = 'COMENTARIO'
    return t

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

def t_IGNORE(t):
    r'\ '
    pass
    #t.lexer.skip(1)

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

def t_SEMICOLON(t):
    r'\;'
    t.type = 'SEMICOLON'
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

lexer.input('!')

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
