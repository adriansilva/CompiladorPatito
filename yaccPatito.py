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
import tablas

from lexPatito import tokens

mt = tablas.ManejadorDeTablas()

funcionActual = 'PROGRAMA'

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
    global funcionActual
    funcionActual = 'PROGRAMA'

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
    principal : PRINCIPAL OPAREN CPAREN OBRACKET estatutos CBRACKET
    '''
    p[0] = p[1]

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
    declaracion2 : posibleID declaracion3
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
    declaracionFuncion : FUNCION VOID ID OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET
                       | FUNCION INT ID OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET
                       | FUNCION FLOAT ID OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET
                       | FUNCION CHAR ID OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET
    '''
    p[0] = "Successful Function Declaration"


def p_declaracionFuncionParametros_1(p): #define argumentos
    '''
    declaracionFuncionParametros : empty
    '''
    p[0] = None

def p_declaracionFuncionParametros_2(p): #define argumentos
    '''
    declaracionFuncionParametros : INT ID
                                 | FLOAT ID
                                 | CHAR ID
    '''
    p[0] = None

def p_declaracionFuncionParametros_3(p): #define argumentos
    '''
    declaracionFuncionParametros : INT ID declaracionFuncionParametros2
                                 | FLOAT ID declaracionFuncionParametros2
                                 | CHAR ID declaracionFuncionParametros2
    '''
    p[0] = None

def p_declaracionFuncionParametros2_3(p): #define argumentos
    '''
    declaracionFuncionParametros2 : COMA INT ID
                                  | COMA FLOAT ID
                                  | COMA CHAR ID
    '''
    p[0] = None

def p_declaracionFuncionParametros2_4(p): #define argumentos
    '''
    declaracionFuncionParametros2 : COMA INT ID declaracionFuncionParametros2
                                  | COMA FLOAT ID declaracionFuncionParametros2
                                  | COMA CHAR ID declaracionFuncionParametros2
    '''
    p[0] = None

def p_declaracionFuncionVariables(p):
    '''
    declaracionFuncionVariables : empty
                                | declaracion
    '''

def p_estatutos_1(p):
    '''
    estatutos : empty
              | return
    '''

def p_estatutos_2(p):
    '''
    estatutos : declaracion estatutos
              | estatutoRepeticionIncondicional estatutos
              | estatutoRepeticionCondicional estatutos
              | lectura estatutos
              | llamadaFuncion estatutos
              | asignacion estatutos
              | escritura estatutos
              | decision estatutos
    '''
    p[0] = "llamando estatutos"

def p_escritura(p):
    '''
    escritura : ESCRIBE OPAREN escritura2 CPAREN SEMICOLON
    '''

def p_escritura2_1(p):
    '''
    escritura2 : empty
    '''

def p_escritura2_2(p):
    '''
    escritura2 : ID escritura3
               | STRING escritura3
    '''

def p_escritura3_1(p):
    '''
    escritura3 : empty
    '''

def p_escritura3_3(p):
    '''
    escritura3 : COMA ID escritura3
               | COMA STRING escritura3
    '''

def p_decision(p):
    '''
    decision : SI OPAREN expresion CPAREN ENTONCES OBRACKET estatutos CBRACKET decision2
    '''
    p[0] = "tomando decision"

def p_decision_2(p):
    '''
    decision2 : SINO OBRACKET estatutos CBRACKET
              | empty
    '''

def p_llamadaFuncion(p):
    '''
    llamadaFuncion : ID OPAREN primerParametro extraParametros CPAREN SEMICOLON
    '''
    p[0] = "llamando funcion"

def p_primerParametro(p):
    '''
    primerParametro : expresion
                    | empty
    '''

def p_extraParametros(p):
    '''
    extraParametros : COMA expresion extraParametros
                    | empty
    '''

def p_lectura(p):
    '''
    lectura : LEE OPAREN posibleID lectura2 CPAREN SEMICOLON
    '''

def p_lectura2_1(p):
    '''
    lectura2 : empty
    '''

def p_lectura2_3(p):
    '''
    lectura2 : COMA posibleID lectura2
    '''

def p_asignacion(p):
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
    #Este código se va a usar cuando ya tengamos tabla de variables
    """
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
    """
    p[0] = (p[2],p[1],p[3])
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
    termino1 : posibleID
             | ENTERO
             | FLOTANTE
             | CARACTER
    '''
    p[0] = p[1]

def p_posibleID_1(p):
    '''
    posibleID : ID np_ID
    '''
    p[0] = p[1]

def p_posibleID_4(p):
    '''
    posibleID : ID OCORCH expresion CCORCH
    '''
    p[0] = (p[1],'[',p[3],']')

def p_posibleID_6(p):
    '''
    posibleID : ID np_ID OCORCH expresion COMA expresion CCORCH
    '''
    p[0] = (p[1],'[',p[3],',',p[5],']')


def p_termino1_3(p):
    '''
    termino1 : OPAREN expresion CPAREN
    '''
    p[0] = (p[1],p[2],p[3])


def p_estatutoRepeticionIncondicional(p):
    '''
    estatutoRepeticionIncondicional : DESDE ID ASSIGN expresion HASTA expresion HAZ OBRACKET estatutos CBRACKET
    '''

def p_estatutoRepeticionCondicional(p):
    '''
    estatutoRepeticionCondicional : MIENTRAS OPAREN expresion CPAREN HAZ OBRACKET estatutos CBRACKET
    '''
    print("Que hay de nuevo viejo")

def p_return(p):
    '''
    return : REGRESA expresion SEMICOLON
    '''

def p_error(p):
    print("Something's wrong baby :(")

def p_np_ID(p):
    '''
    np_ID :
    '''

    mt.addFuncion('PROGRAMA','VOID')
    if(not mt.contieneID(funcionActual,p[-1])):
        mt.addVariable(funcionActual,p[-1],'INT',900)
        print("No existe la variable.")
    else:
        print("All good baby!")


def p_empty(p):
    '''
    empty :
    '''

parser = yacc.yacc(start='estatutoRepeticionCondicional')

while True:
    try:
        s = input('')
    except EOFError:
        break
    if not s: continue

    result = parser.parse(s)
    print(result)
