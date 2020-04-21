import ply.yacc as yacc

from lexPatito import tokens

precedence = (
    ('left','PLUS','MINUS'),
    ('left','MULTIPLY','DIVIDE'),
    ('left','OPMATRIZ')
)

def p_expresion(p):
    '''
    expresion : expresion LOGIC expresion
              | termino RELOP expresion
              | termino
    '''
    print(p)

    if(len(p) == 1):
        p[0] = p[1]
    else:
        p[0] = (p[2],p[1],p[3])



    #elif p[2] == "&&" || p[2] == "||":
    #    if p[2] == "&&":
    #        p[0] = (p[1] && p[3])
    #    else:
    #        p[0] = (p[1] || p[3])
    #else:
    #    if p[2] == "<=":
    #        p[0] =


def p_termino(p):
    '''
    termino : termino1
            | termino PLUS termino
            | termino MINUS termino
            | termino MULTIPLY termino
            | termino DIVIDE termino
    '''
    print(p)

    if(len(p) == 1):
        p[0] = p[1]
    else:
        p[0] = (p[2],p[1],p[3])

def p_termino1(p):
    '''
    termino1 : ID
             | ID OPMATRIZ
             | ENTERO
             | FLOTANTE
             | CARACTER
             | LPAREN expresion RPAREN
    '''
    print(p)

    if(len(p) == 1):
        p[0] = p[1]
    elif(len(p) == 2):
        p[0] = (p[2],p[1])
    elif(len(p) == 3):
        p[0] = (p[1],p[2],p[3])

#def p_empty(p):
#    '''
#    empty :
#    '''
#    p[0] = None

parser = yacc.yacc()

while True:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
