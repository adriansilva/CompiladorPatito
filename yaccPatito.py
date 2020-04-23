"""
Se añadieron nuevas reglas al parser y ahora las reglas anteriores arrojan
resultados en lugar de regresar sólo tuplas. Aún no consideran matríces.
LYa de arregló el error de la recursión infinita. Ya jalan las reglas de
programa a pesar de que siguen estando limitadas. Algún input prueba podría
ser: PROGRAMA p; VAR INT: VAR FLOAT: FUNCION FUNCION PRINCIPAL También las
reglas de declaración y declaración función están incompletas. Se pusieron
asi para testear. OJO ahorita el yacc corre como primera regla la de
programa porque asi está especificado yacc.yacc(start='programa') para
hacer debugging. Si quieres usar otra regla para comenzar sólo pon el
nombre de la regla u omite este campo.

"""
import ply.yacc as yacc
import sys

from lexPatito import tokens

precedence = (
    ('left','PLUS','MINUS'),
    ('left','MULTIPLY','DIVIDE'),
    ('left','OPMATRIZ')
)

def p_programa(p):
    '''
    programa : PROGRAMA ID SEMICOLON programa2
    '''
    p[0] = p[1]

def p_programa2(p):
    '''
    programa2 : declaracion programa2
              | programa3
    '''
    print(p[1])
    p[0] = p[1]

def p_programa3(p):
    '''
    programa3 : declaracionFuncion programa3
              | principal
    '''
    p[0] = p[1]

def p_principal(p):
    '''
    principal : PRINCIPAL OPAREN CPAREN OBRACKET principal1 CBRACKET
    '''
    p[0] = p[1]

def p_principal1(p):
    '''
    principal1 : estatutos principal1
               | empty
    '''

def p_declaracion(p):
    '''
    declaracion : VAR INT COLON declaracion2
                | VAR FLOAT COLON declaracion2
                | VAR CHAR COLON declaracion2
    '''
    p[0] = p[1]

def p_declaracion2_1(p):
    '''
    declaracion2 : SEMICOLON
    '''
    p[0] = p[1]

def p_declaracion2_2(p):
    '''
    declaracion2 : ID declaracion3
    '''
    p[0] = p[1]

def p_declaracion3_1(p):
    '''
    declaracion3 : SEMICOLON
    '''
    p[0] = p[1]

def p_declaracion3_2(p):
    '''
    declaracion3 : COMA declaracion2
    '''
    p[0] = p[1]

def p_declaracion3_3(p):
    '''
    declaracion3 : ASSIGN expresion SEMICOLON
    '''
    p[0] = p[1]

def p_declaracion3_4(p):
    '''
    declaracion3 : ASSIGN expresion COMA declaracion2
    '''
    p[0] = p[1]

def p_declaracionFuncion(p):
    '''
    declaracionFuncion : FUNCION VOID ID LPAREN declaracionFuncion2 RPAREN declaracion OBRACKET estatutos
                       | FUNCION INT ID LPAREN declaracionFuncion2 RPAREN declaracion OBRACKET estatutos
                       | FUNCION FLOAT ID LPAREN declaracionFuncion2 RPAREN declaracion OBRACKET estatutos
                       | FUNCION CHAR ID LPAREN declaracionFuncion2 RPAREN declaracion OBRACKET estatutos
    '''
    p[0] = "Successful Function Declaration"


def p_declaracionFuncion2(p): #define argumentos
    '''
    declaracionFuncion2 : ID
                        | ID COMA declaracionFuncion2 
    '''
    p[0] = None

def p_estatutos(p):
    '''
    estatutos : declaracion CBRACKET
              | declaracion estatutos 
    '''
    p[0] = None

def p_asignacion_4(p):
    '''
    asignacion : ID ASSIGN expresion SEMICOLON
    '''

def p_expresion_3(p):
    '''
    expresion : expresion LOGIC expresion
              | expresion RELOP expresion
    '''
    p[0] = (p[2],p[1],p[3])

def p_expresion_2(p):
    '''
    expresion : termino1 OPMATRIZ
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
    if(isinstance(p[3], tuple)):
        if (len(p[3]) == 3) & (p[3][0] == '(') & (p[3][2] == ')'):
            if p[2] == '+':
                p[0] = p[1] + p[3][1]
            elif p[2] == '-':
                p[0] = p[1] - p[3][1]
            elif p[2] == '*':
                p[0] = p[1] * p[3][1]
            elif p[2] == '/':
                p[0] = p[1] / p[3][1]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]

def p_termino_2(p):
        '''
        termino : termino1 OPMATRIZ
        '''
        p[0] = (p[1],p[2])

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
    termino1 : OPAREN expresion CPAREN
    '''
    p[0] = (p[1],p[2],p[3])


def p_estatutoRepeticionIncondicional(p):
    '''
    estatutoRepeticionIncondicional : DESDE ID ASSIGN expresion HASTA expresion HAZ OBRACKET CBRACKET
    '''

def p_error(p):
    print("Something's wrong baby :(")

def p_empty(p):
    '''
    empty :
    '''

parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
