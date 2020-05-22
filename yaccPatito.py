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

def p_programa2(p):
    '''
    programa2 : declaracion programa2
              | programa3
    '''
    print("Ya declaro variables.")

def p_programa3(p):
    '''
    programa3 : declaracionFuncion principal
    '''
    print("Ya declaro funciones.")

def p_principal(p):
    '''
    principal : PRINCIPAL OPAREN CPAREN OBRACKET estatutos CBRACKET np_printCuadruplos
    '''
    print("YA TERMINÓ PRINCIPAL!!!!!!!!!!!")
    global funcionActual
    #mt.deleteFuncion(funcionActual)
    funcionActual = "PRINCIPAL"
    #mt.deleteFuncion(funcionActual)
    # agregar np_agregarFuncion

def p_declaracion(p):
    '''
    declaracion : VAR INT np_defineTipo COLON declaracion2
                | VAR FLOAT np_defineTipo COLON declaracion2
                | VAR CHAR np_defineTipo COLON declaracion2
    '''
    # agregar np_tipoDeVariable
    #
    # def np_tipoDeVariable(p):
    # np_tipoDeVariable :
    # global tipoDeVariable = p[-1]

def p_np_defineTipo(p):
    '''
    np_defineTipo :
    '''
    global tipoVariable
    tipoVariable = p[-1]


def p_declaracion2(p):
    '''
    declaracion2 : np_agregarFondo posibleIDDeclaracion declaracion3
    '''

def p_declaracion3_1(p):
    '''
    declaracion3 : np_quitarFondo SEMICOLON
                 | np_quitarFondo COMA declaracion2
                 | ASSIGN np_insertarOperador expresion np_quitarFondo SEMICOLON
                 | ASSIGN np_insertarOperador expresion np_quitarFondo COMA declaracion2
    '''

def p_declaracionFuncion(p):
    '''
    declaracionFuncion : FUNCION VOID ID np_declfunc OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET np_endFunc
                       | FUNCION INT ID np_declfunc OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET np_endFunc
                       | FUNCION FLOAT ID np_declfunc OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET np_endFunc
                       | FUNCION CHAR ID np_declfunc OPAREN declaracionFuncionParametros CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET np_endFunc
    '''
    global funcionActual
    print("Successful Function Declaration")
    #mt.deleteFuncion(p[3])
    funcionActual = "PROGRAMA"

def p_np_endFunc(p):
    '''
    np_endFunc :
    '''
    gc.endFunc()
    print("Se llamo a una función.")

def p_np_termino(p):
    '''
    np_termino :
    '''
    print("TERMINO CON VARIABLES\n\n\n")
    # agregar np_tipoDeFuncion (es necesario?)
    # agregar np_agregarFuncion
    # agregar np_ borrar variables locales

def p_declaracionFuncionParametros_1(p): #define argumentos
    '''
    declaracionFuncionParametros : empty
    '''

def p_declaracionFuncionParametros_3(p): #define argumentos
    '''
    declaracionFuncionParametros : INT np_defineTipo np_agregarFondo posibleIDDeclaracion np_quitarFondo declaracionFuncionParametros2
                                 | CHAR np_defineTipo np_agregarFondo posibleIDDeclaracion np_quitarFondo declaracionFuncionParametros2
                                 | FLOAT np_defineTipo np_agregarFondo posibleIDDeclaracion np_quitarFondo declaracionFuncionParametros2
    '''

def p_declaracionFuncionParametros2_1(p): #define argumentos
    '''
    declaracionFuncionParametros2 : empty
    '''

def p_declaracionFuncionParametros2_4(p): #define argumentos
    '''
    declaracionFuncionParametros2 : COMA INT np_defineTipo np_agregarFondo posibleIDDeclaracion np_quitarFondo declaracionFuncionParametros2
                                  | COMA FLOAT np_defineTipo np_agregarFondo posibleIDDeclaracion np_quitarFondo declaracionFuncionParametros2
                                  | COMA CHAR np_defineTipo np_agregarFondo posibleIDDeclaracion np_quitarFondo declaracionFuncionParametros2
    '''


def p_declaracionFuncionVariables(p):
    '''
    declaracionFuncionVariables : empty
                                | declaracion
    '''

def p_np_declfunc(p):
    '''
    np_declfunc :
    '''
    global funcionActual
    funcionActual = p[-1]
    if not mt.existeFuncion(funcionActual):
        mt.addFuncion(p[-1], p[-2])
    else:
        print("YA EXISTE LA FUNCIÓN:",funcionActual)
        print(p[-1])
        exit(-1)

def p_estatutos_1(p):
    '''
    estatutos : return
              | empty
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
    print("llamando estatutos")

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
    decision : SI OPAREN np_agregarFondo expresion np_quitarFondo np_iniciaIf CPAREN ENTONCES OBRACKET estatutos CBRACKET SINO OBRACKET np_iniciaElse np_agregarFondo estatutos np_quitarFondo np_terminaElse CBRACKET
             | SI OPAREN np_agregarFondo expresion np_quitarFondo np_iniciaIf CPAREN ENTONCES OBRACKET estatutos CBRACKET np_terminaIf
    '''
    print("tomando decision")

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
    asignacion : posibleID np_agregarFondo ASSIGN np_insertarOperador np_agregarFondo expresion np_quitarFondo np_quitarFondo SEMICOLON
    '''
# checar si el np para ver si el resultado de la derecha es del mismo tipo que de la izq es cuadruplo o no

def p_expresion_3(p):
    '''
    expresion : expresion LOGIC np_insertarOperador expresion
              | expresion RELOP np_insertarOperador expresion
    '''

def p_expresion_1(p):
    '''
    expresion : termino
    '''

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

def p_np_insertarOperador(p):
    '''
    np_insertarOperador :
    '''
    gc.operador(p[-1])

def p_termino_2(p):
    '''
    termino : termino1 OPMATRIZ np_insertarOperador
    '''

def p_termino_1(p):
    '''
    termino : termino1
    '''

def p_termino1_1(p):
    '''
    termino1 : posibleID
             | ENTERO np_contieneID_Constante_Entero
             | FLOTANTE np_contieneID_Constante_Flotante
             | llamadaFuncion
    '''

def p_termino1_3(p):
    '''
    termino1 : OPAREN np_insertarOperador expresion CPAREN np_insertarOperador
             | QUOT CARACTER QUOT
    '''

def p_posibleID_1(p):
    '''
    posibleID : ID np_contieneID np_enviarACuadruplos
              | ID np_contieneID np_enviarACuadruplos OCORCH np_agregarFondo expresion np_quitarFondo CCORCH
              | ID np_contieneID np_enviarACuadruplos OCORCH np_agregarFondo expresion np_quitarFondo COMA np_agregarFondo expresion np_quitarFondo CCORCH
    '''

def p_posibleIDDeclaracion_1(p):
    '''
    posibleIDDeclaracion : np_updateCurrentDimension0 ID np_addVariable np_enviarACuadruplos np_actualizarDimensiones
                         | np_updateCurrentDimension1 ID np_addVariable np_enviarACuadruplos np_actualizarDimensiones OCORCH expresion CCORCH
                         | np_updateCurrentDimension2 ID np_addVariable np_enviarACuadruplos np_actualizarDimensiones OCORCH expresion COMA expresion CCORCH
    '''

def p_np_updateCurrentDimension0(p):
    '''
    np_updateCurrentDimension0 :
    '''
    global currentDimension
    currentDimension = 0

def p_np_updateCurrentDimension1(p):
    '''
    np_updateCurrentDimension1 :
    '''
    global currentDimension
    currentDimension = 1

def p_np_updateCurrentDimension2(p):
    '''
    np_updateCurrentDimension2 :
    '''
    global currentDimension
    currentDimension = 2

def p_estatutoRepeticionIncondicional(p):
    '''
    estatutoRepeticionIncondicional : DESDE ID np_contieneID HASTA expresion HAZ OBRACKET estatutos CBRACKET
    '''
    # agregar np_contieneID

def p_estatutoRepeticionCondicional(p):
    '''
    estatutoRepeticionCondicional : MIENTRAS OPAREN np_agregarFondo expresion np_quitarFondo CPAREN HAZ OBRACKET npWhileInicia estatutos CBRACKET npWhileTermina
    '''
    print("Que hay de nuevo viejo")

def p_npWhileStExp(p):
    '''
    npWhileStExp :
    '''
    #gc.whileStatementExpresion()

def p_npWhileInicia(p):
    '''
    npWhileInicia :
    '''
    gc.whileStatementInicia()

def p_npWhileTermina(p):
    '''
    npWhileTermina :
    '''
    gc.whileStatementTermina()

def p_return(p):
    '''
    return : REGRESA np_agregarFondo expresion np_quitarFondo SEMICOLON np_return
           | REGRESA SEMICOLON np_returnVOID
    '''

def p_np_return(p):
    '''
    np_return :
    '''
    print('X')
    gc.regresa(mt.getTipoFuncion(funcionActual),'X')

def p_np_returnVOID(p):
    '''
    np_returnVOID :
    '''
    print('Void')
    gc.regresa(mt.getTipoFuncion(funcionActual),'VOID')

def p_error(p):
    print("Hay un error de sintaxis!")
    exit(-1)

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

def p_np_enviarACuadruplos(p):
    '''
    np_enviarACuadruplos :
    '''
    gc.operando(p[-2],mt.getTipoVariable(funcionActual,p[-2]),mt.getDimensionVariable(funcionActual,p[-2]))


def p_np_actualizarDimensiones(p):
    '''
    np_actualizarDimensiones :
    '''
    mt.actualizarDimensiones(funcionActual,p[-3],currentDimension)

def p_np_agregarFondo(p):
    '''
    np_agregarFondo :
    '''
    print("se agregó fondo exitosamente.")
    gc.operador('(')

def p_np_quitarFondo(p):
    '''
    np_quitarFondo :
    '''
    print("Se quitó fondo exitosamente!")
    gc.operador(')')

def p_np_printCuadruplos(p):
    '''
    np_printCuadruplos :
    '''
    gc.printCuadruplos()

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
