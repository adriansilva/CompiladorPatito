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
import generadorDeCuadruplos

from lexPatito import tokens

gc = generadorDeCuadruplos.generadorDeCuadruplos()
mt = tablas.ManejadorDeTablas()
tipoVariable = None
funcionActual = 'PROGRAMA'
currentDimension = 0

mt.addFuncion(funcionActual,'VOID')

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
    principal : PRINCIPAL npdeclfunc OPAREN CPAREN OBRACKET estatutos CBRACKET
    '''
    global funcionActual
    p[0] = p[1]
    #mt.deleteFuncion(funcionActual)
    funcionActual = "PROGRAMA"
    #mt.deleteFuncion(funcionActual)
    # agregar np_agregarFuncion

def p_declaracion(p):
    '''
    declaracion : VAR INT defineTipo COLON declaracion2
                | VAR FLOAT defineTipo COLON declaracion2
                | VAR CHAR defineTipo COLON declaracion2
    '''
    p[0] = p[1]
    # agregar np_tipoDeVariable
    #
    # def np_tipoDeVariable(p):
    # np_tipoDeVariable :
    # global tipoDeVariable = p[-1]

def p_defineTipo(p):
    '''
    defineTipo :
    '''
    global tipoVariable
    tipoVariable = p[-1]


def p_declaracion2(p):
    '''
    declaracion2 : posibleID np_addVariable np_actualizarDimensiones declaracion3
    '''

    p[0] = p[1]

def p_declaracion3_1(p):
    '''
    declaracion3 : SEMICOLON
                 | COMA declaracion2
                 | ASSIGN expresion SEMICOLON
                 | ASSIGN expresion COMA declaracion2
    '''
    p[0] = p[1]


def p_declaracionFuncion(p):
    '''
    declaracionFuncion : FUNCION VOID ID npdeclfunc OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET
                       | FUNCION INT ID npdeclfunc OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET
                       | FUNCION FLOAT ID npdeclfunc OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET
                       | FUNCION CHAR ID npdeclfunc OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET
    '''
    global funcionActual
    p[0] = "Successful Function Declaration"
    #mt.deleteFuncion(p[3])
    funcionActual = "PROGRAMA"

    # agregar np_tipoDeFuncion (es necesario?)
    # agregar np_agregarFuncion
    # agregar np_ borrar variables locales

def p_declaracionFuncionParametros_1(p): #define argumentos
    '''
    declaracionFuncionParametros : empty
    '''
    p[0] = None

def p_declaracionFuncionParametros_3(p): #define argumentos
    '''
    declaracionFuncionParametros : INT ID np_addVariableParametro np_actualizarDimensiones declaracionFuncionParametros2
                                 | FLOAT ID np_addVariableParametro np_actualizarDimensiones declaracionFuncionParametros2
                                 | CHAR ID np_addVariableParametro np_actualizarDimensiones declaracionFuncionParametros2
    '''

    p[0] = None

def p_declaracionFuncionParametros2_1(p): #define argumentos
    '''
    declaracionFuncionParametros2 : empty
    '''
    p[0] = None

def p_declaracionFuncionParametros2_4(p): #define argumentos
    '''
    declaracionFuncionParametros2 : COMA INT ID np_addVariableParametro np_actualizarDimensiones declaracionFuncionParametros2
                                  | COMA FLOAT ID np_addVariableParametro np_actualizarDimensiones declaracionFuncionParametros2
                                  | COMA CHAR ID np_addVariableParametro np_actualizarDimensiones declaracionFuncionParametros2
    '''

    p[0] = None


def p_declaracionFuncionVariables(p):
    '''
    declaracionFuncionVariables : empty
                                | declaracion
    '''

def p_npdeclfunc(p):
    '''
    npdeclfunc :
    '''
    global funcionActual
    funcionActual = p[-1]
    mt.addFuncion(p[-1], p[-2])

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
              | asignacion estatutos
              | escritura estatutos
              | decision estatutos
    '''
    p[0] = "llamando estatutos"

def p_estatutos_3(p):
    '''
    estatutos : llamadaFuncion SEMICOLON estatutos
    '''

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
    escritura2 : posibleID escritura3
               | STRING escritura3
    '''
    # agregar np_agregarVariableConstante

def p_escritura3_1(p):
    '''
    escritura3 : empty
    '''

def p_escritura3_3(p):
    '''
    escritura3 : COMA expresion escritura3
               | COMA STRING escritura3
    '''
    # agregar np_agregarVariableConstante

def p_decision(p):
    '''
    decision : SI OPAREN expresion np_iniciaIf CPAREN ENTONCES OBRACKET estatutos CBRACKET SINO OBRACKET np_iniciaElse estatutos np_terminaElse CBRACKET
             | SI OPAREN expresion np_iniciaIf CPAREN ENTONCES OBRACKET estatutos CBRACKET np_terminaIf
    '''
    p[0] = "tomando decision"

def p_np_iniciaIf(p):
    '''
    np_iniciaIf :
    '''
    gc.ifStatement()

def p_np_terminaIf(p):
    '''
    np_terminaIf :
    '''
    gc.terminaIfStatement()

def p_np_iniciaElse(p):
    '''
    np_iniciaElse :
    '''
    gc.elseStatement()

def p_np_terminaElse(p):
    '''
    np_terminaElse :
    '''
    gc.terminaElseStatement()

def p_llamadaFuncion(p):
    '''
    llamadaFuncion : ID OPAREN primerParametro extraParametros CPAREN
    '''
    if not mt.existeFuncion(p[1]):
        print("No existe la funcion:",p[1])
        exit(-1)
# checar si ID existe en tabla funciones con np veda
# considerar agregar la posibilidad de pasar segmentos de matrices o arreglos

def p_primerParametro(p):
    '''
    primerParametro : expresion
                    | empty
    '''
# revisar si ver tipo de expresion es cuadruplo o no
# considerar agregar variable global (arreeglo) para tipos de parametros de funcion

def p_extraParametros(p):
    '''
    extraParametros : COMA expresion extraParametros
                    | empty
    '''
# revisar si ver tipo de expresion es cuadruplo o no
# considerar agregar variable global (arreeglo) para tipos de parametros de funcion

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
    asignacion : posibleID ASSIGN expresion SEMICOLON
    '''
# checar si el np para ver si el resultado de la derecha es del mismo tipo que de la izq es cuadruplo o no

def p_expresion_3(p):
    '''
    expresion : expresion LOGIC np_insertarOperador expresion
              | expresion RELOP np_insertarOperador expresion
    '''
    p[0] = (p[2],p[1],p[3])

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
    termino : termino PLUS np_insertarOperador termino
            | termino MINUS np_insertarOperador termino
            | termino MULTIPLY np_insertarOperador termino
            | termino DIVIDE np_insertarOperador termino
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

def p_np_insertarOperador(p):
    '''
    np_insertarOperador :
    '''
    gc.operador(p[-1])

def p_termino_2(p):
    '''
    termino : termino1 OPMATRIZ np_insertarOperador
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
             | ENTERO np_contieneID_Constante_Entero
             | FLOTANTE np_contieneID_Constante_Flotante
             | llamadaFuncion
    '''
    p[0] = p[1]
    # agregar np_agregarVariableConstante

def p_posibleID_1(p):
    '''
    posibleID : ID np_contieneID
    '''
    p[0] = p[1]
    global currentDimension
    currentDimension = 0
    # agregar npID

def p_posibleID_4(p):
    '''
    posibleID : ID np_contieneID OCORCH expresion CCORCH
    '''
    p[0] = p[1]
    global currentDimension
    currentDimension = 1
    #p[0] = (p[1],'[',p[3],']')
    # agregar np_contieneID

def p_posibleID_6(p):
    '''
    posibleID : ID np_contieneID OCORCH expresion COMA expresion CCORCH
    '''
    p[0] = p[1]
    global currentDimension
    currentDimension = 2
    #p[0] = (p[1],'[',p[3],',',p[5],']')
    # agregar np_contieneID

def p_termino1_3(p):
    '''
    termino1 : OPAREN np_insertarOperador expresion CPAREN np_insertarOperador
             | QUOT CARACTER QUOT
    '''
    p[0] = (p[1],p[2],p[3])


def p_estatutoRepeticionIncondicional(p):
    '''
    estatutoRepeticionIncondicional : DESDE ID np_contieneID HASTA expresion HAZ OBRACKET estatutos CBRACKET
    '''
    # agregar np_contieneID

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

def p_np_contieneID(p):
    '''
    np_contieneID :
    '''
    if not mt.contieneID(funcionActual,p[-1]):
        print("El ID:",p[-1],"no existe en la funcion:", funcionActual)
        exit(-1)

def p_np_contieneID_Constante_Entero(p):
    '''
    np_contieneID_Constante_Entero :
    '''
    if not mt.contieneID('PROGRAMA','c_'+str(p[-1])):
        mt.addVariable('PROGRAMA','c_'+str(p[-1]),'C_INT',False)

def p_np_contieneID_Constante_Flotante(p):
    '''
    np_contieneID_Constante_Flotante :
    '''
    if not mt.contieneID('PROGRAMA','c_'+str(p[-1])):
        mt.addVariable('PROGRAMA','c_'+str(p[-1]),'C_FLOAT',False)

def p_np_addVariableParametro(p):
    '''
    np_addVariableParametro :
    '''

    mt.addVariable(funcionActual, p[-1], p[-2], True) #direccion esta hardcodeada por ahora

def p_np_addVariable(p):
    '''
    np_addVariable :
    '''
    mt.addVariable(funcionActual, p[-1], tipoVariable, False) #direccion esta hardcodeada por ahora

# Necesitamos dos tipos de np_contieneID: 1. Necesita accesar a variable global tipo.
#                                 2. No necesita accesar a variable global tipo
# Necesitamos dos tipos de np_funcion: 1. Necesita accesar a variable global tipoFuncion
#                                      2. Puede accesar a la p para conseguir información

def p_np_actualizarDimensiones(p):
    '''
    np_actualizarDimensiones :
    '''
    mt.actualizarDimensiones(funcionActual,p[-2],currentDimension)

def p_empty(p):
    '''
    empty :
    '''

parser = yacc.yacc(start='')

f = open("testInput.txt", "r")
result = parser.parse(f.read())

print(result)
'''
s=''

while True:
    try:
        s += input('')
    except EOFError:
        break
    s+="\n"
    if not s: continue
    if s[len(s)-2] == '°':
        break

print(s)
result = parser.parse(s[0:-2])
print(result)


while True:
    try:
        s = input('')
    except EOFError:
        break
    if not s: continue

    result = parser.parse(s)
    print(result)
'''
