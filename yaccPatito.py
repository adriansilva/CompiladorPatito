import ply.yacc as yacc
import sys

from lexPatito import tokens

precedence = (
    ('left','PLUS','MINUS'),
    ('left','MULTIPLY','DIVIDE'),
    ('left','OPMATRIZ')
)

def p_expresion_4(p):
    '''
    expresion : expresion OPMATRIZ LOGIC expresion
    '''
    p[0] = (p[3],p[1],p[2],p[4])

def p_expresion_3(p):
    '''
    expresion : expresion LOGIC expresion
              | expresion RELOP expresion
    '''
    p[0] = (p[2],p[1],p[3])

def p_expresion_2(p):
    '''
    expresion : termino OPMATRIZ
    '''
    p[0] = (p[1],p[2])

def p_expresion_1(p):
    '''
    expresion : termino
    '''
    p[0] = p[1]

    #elif p[2] == "&&" || p[2] == "||":
    #    if p[2] == "&&":
    #        p[0] = (p[1] && p[3])
    #    else:
    #        p[0] = (p[1] || p[3])
    #else:
    #    if p[2] == "<=":
    #        p[0] =


def p_termino_3(p):
    '''
    termino : termino PLUS termino
            | termino MINUS termino
            | termino MULTIPLY termino
            | termino DIVIDE termino
    '''
    p[0] = (p[2],p[1],p[3])

def p_termino_1(p):
    '''
    termino : termino1
    '''
    p[0] = p[1]

def p_termino1_1(p):
    '''
    termino1 : ID
             | ENTERO
             | FLOTANTE
             | CARACTER
    '''
    p[0] = p[1]

def p_termino1_3(p):
    '''
    termino1 : LPAREN expresion RPAREN
    '''
    p[0] = (p[1],p[2],p[3])

def p_error(p):
    print("Something's wrong baby :(")


parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
