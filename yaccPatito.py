import ply.yacc as yacc
import sys
import tablas
import generadorDeCuadruplos
import MaquinaVirtual

from lexPatito import tokens

gc = generadorDeCuadruplos.generadorDeCuadruplos()
mv = MaquinaVirtual.MaquinaVirtual()

tipoVariable = None
funcionActual = 'PROGRAMA'
currentDimension = 0
esParametro = False
esUMINUS = False
restarDimension = 0
IDActual = []
funcionObjetivo = 'PRINCIPAL'

gc.mt.addFuncion(funcionActual,'VOID')
gc.mt.addFuncion('TEMPORALES', 'VOID')
gc.mt.addFuncion('CONSTANTES', 'VOID')
gc.mt.addConstante(str(1),'INT')
gc.constanteCuadruplo(1)

precedence = (
    ('left','PLUS','MINUS'),
    ('left','MULTIPLY','DIVIDE'),
    ('right','OPMATRIZ'),
    ('right', 'UMINUS')
)

def p_programa(p):
    '''
    programa : PROGRAMA ID SEMICOLON programa2
    '''
    cuadruplos = gc.returnCuadruplos()
    tabla = gc.mt
    mv.processInput(cuadruplos,tabla)
    p[0] = 'TERMINO DE PROCESAR PROGRAMA'

def p_programa2(p):
    '''
    programa2 : declaracion programa2
              | np_gotoMain programa3
    '''

def p_np_gotoMain(p):
    '''
    np_gotoMain :
    '''
    gc.gotoMain()

def p_programa3(p):
    '''
    programa3 : declaracionFuncion programa3
              | principal
    '''

def p_principal(p):
    '''
    principal : PRINCIPAL np_declfuncprincipal np_updateMain OPAREN CPAREN OBRACKET estatutos CBRACKET np_end np_printCuadruplos
    '''
    global funcionActual
    funcionActual = "PRINCIPAL"

def p_np_updateMain(p):
    '''
    np_updateMain :
    '''
    gc.updateMain()

def p_np_end(p):
    '''
    np_end :
    '''
    gc.endProgram()

def p_np_printTablas(p):
    '''
    np_printTablas :
    '''
    gc.mt.printTablas()

def p_declaracion(p):
    '''
    declaracion : VAR INT np_defineTipo COLON declaracion2
                | VAR FLOAT np_defineTipo COLON declaracion2
                | VAR CHAR np_defineTipo COLON declaracion2
    '''

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
    declaracionFuncion : FUNCION VOID ID np_declfunc np_comienzaFunc OPAREN np_esParametro declaracionFuncionParametros np_yaNoEsParametro CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET np_endFunc
                       | FUNCION INT ID np_declfunc np_comienzaFunc OPAREN np_esParametro declaracionFuncionParametros np_yaNoEsParametro CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET np_endFunc
                       | FUNCION FLOAT ID np_declfunc np_comienzaFunc OPAREN np_esParametro declaracionFuncionParametros np_yaNoEsParametro CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET np_endFunc
                       | FUNCION CHAR ID np_declfunc np_comienzaFunc OPAREN np_esParametro declaracionFuncionParametros np_yaNoEsParametro CPAREN declaracionFuncionVariables OBRACKET estatutos CBRACKET np_endFunc
    '''
    global funcionActual
    funcionActual = "PROGRAMA"

def p_np_esParametro(p):
    '''
    np_esParametro :
    '''
    global esParametro
    esParametro = True

def p_np_yaNoEsParametro(p):
    '''
    np_yaNoEsParametro :
    '''
    global esParametro
    esParametro = False

def p_np_endFunc(p):
    '''
    np_endFunc :
    '''
    gc.endFunc(funcionActual)
    #print("Se llamo a una función.")

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
    if not gc.mt.existeFuncion(funcionActual):
        gc.mt.addFuncion(funcionActual, p[-2])
        gc.updateDirFunc(funcionActual)
        if p[-2] != 'VOID':
            #print(p[-2])
            gc.mt.addVariable('PROGRAMA',funcionActual,p[-2],False)
            gc.mt.actualizarDimensiones('PROGRAMA',funcionActual,0)
    else:
        print("YA EXISTE LA FUNCIÓN:",funcionActual)
        print(p[-1])
        exit(-1)

def p_np_declprincipal(p):
    '''
    np_declfuncprincipal :
    '''
    global funcionActual
    funcionActual = p[-1]
    gc.mt.addFuncion(p[-1], 'VOID')

def p_np_comienzaFunc(p):
    '''
    np_comienzaFunc :
    '''
    gc.mt.comienzaFunc(p[-2], len(gc.outputCuadruplos) + 1)

def p_estatutos_1(p):
    '''
    estatutos : return estatutos
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
    #print("llamando estatutos")

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
    escritura2 : np_agregarFondo expresion np_quitarFondo np_print escritura3
               | STRING np_printStr escritura3
    '''

def p_escritura3_1(p):
    '''
    escritura3 : empty
    '''

def p_escritura3_3(p):
    '''
    escritura3 : COMA np_agregarFondo expresion np_quitarFondo np_print escritura3
               | COMA STRING np_printStr escritura3
    '''

def p_np_print(p):
    '''
    np_print :
    '''
    gc.print(funcionActual)

def p_np_printStr(p):
    '''
    np_printStr :
    '''
    gc.print(funcionActual,p[-1])

def p_decision(p):
    '''
    decision : SI OPAREN np_agregarFondo expresion np_quitarFondo np_iniciaIf CPAREN ENTONCES OBRACKET estatutos CBRACKET SINO OBRACKET np_iniciaElse np_agregarFondo estatutos np_quitarFondo np_terminaElse CBRACKET
             | SI OPAREN np_agregarFondo expresion np_quitarFondo np_iniciaIf CPAREN ENTONCES OBRACKET estatutos CBRACKET np_terminaIf
    '''

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
    llamadaFuncion : ID np_existeFuncion np_llamadaFuncion np_agregarFondoParam OPAREN paramsLlamada1 CPAREN np_quitarFondoParam np_goSUB
    '''
    p[0] = 100000

def p_np_existeFuncion(p):
    '''
    np_existeFuncion :
    '''
    if not gc.mt.existeFuncion(p[-1]):
        print("No existe la funcion:",p[-1])
        exit(-1)

def p_np_llamadaFuncion(p):
    '''
    np_llamadaFuncion :
    '''
    global funcionObjetivo
    funcionObjetivo = p[-2]
    gc.llamadaFuncion(funcionObjetivo)

def p_np_agregarFondoParam(p):
    '''
    np_agregarFondoParam :
    '''
    gc.agregarFondoParam(p[-3])

def p_np_quitarFondoParam(p):
    '''
    np_quitarFondoParam :
    '''
    gc.quitarFondoParam(p[-7])

def p_paramsLlamada1(p):
    '''
    paramsLlamada1 : empty
                   | paramsLlamada2
    '''

def p_paramsLlamada2(p):
    '''
    paramsLlamada2 : np_agregarFondo expresion np_quitarFondo np_resolverParam
                   | np_agregarFondo expresion np_quitarFondo np_resolverParam COMA paramsLlamada2
    '''

def p_np_resolverParam(p):
    '''
    np_resolverParam :
    '''
    gc.resolverParam(funcionObjetivo)

def p_np_goSUB(p):
    '''
    np_goSUB :
    '''
    gc.goSUB(p[-8])

def p_lectura(p):
    '''
    lectura : LEE OPAREN posibleID np_read lectura2 CPAREN SEMICOLON
    '''

def p_lectura2_1(p):
    '''
    lectura2 : empty
    '''

def p_lectura2_3(p):
    '''
    lectura2 : COMA posibleID np_read lectura2
    '''

def p_np_read(p):
    '''
    np_read :
    '''
    gc.read(p[-1],funcionActual)

def p_asignacion(p):
    '''
    asignacion : posibleID np_agregarFondo ASSIGN np_insertarOperador np_agregarFondo expresion np_quitarFondo np_quitarFondo SEMICOLON
    '''

def p_expresion_3(p):
    '''
    expresion : expresion logicORelop np_insertarOperador expresion
    '''

def p_logicORelop(p):
    '''
    logicORelop : LOGIC
                | RELOP
    '''
    p[0] = p[1]

def p_expresion_1(p):
    '''
    expresion : termino
    '''

def p_termino_3(p):
    '''
    termino : termino PLUS np_insertarOperador termino
            | termino MINUS np_insertarOperador termino
            | termino MULTIPLY np_insertarOperador termino
            | termino DIVIDE np_insertarOperador termino
    '''

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
    termino : termino1 np_updateUMINUSFALSE
    '''

def p_np_updateUMINUSFALSE(p):
    '''
    np_updateUMINUSFALSE :
    '''
    global esUMINUS
    esUMINUS = False

def p_np_updateUMINUSTRUE(p):
    '''
    np_updateUMINUSTRUE :
    '''
    global esUMINUS
    esUMINUS = True

def p_termino1_1(p):
    '''
    termino1 : posibleID
             | constante
             | CARACT np_addConstanteCHAR
             | llamadaFuncion
    '''
    p[0] = p[1]

def p_termino1_3(p):
    '''
    termino1 : OPAREN np_insertarOperador expresion CPAREN np_insertarOperador
    '''

def p_constante(p):
    '''
    constante : ENTERO np_addConstanteINT
              | FLOTANTE np_addConstanteFLOAT
    '''
    p[0] = p[1]
    p[1] = -p[1]

def p_termino1_uminus(p):
    'termino1 : MINUS np_updateUMINUSTRUE constante %prec UMINUS'

    p[0] = -p[3]

def p_posibleID_1(p):
    '''
    posibleID : ID np_defIDActual np_contieneID posibleID2 np_quitarIDActual
    '''
    p[0] = p[1] #NO BORRAR lo usa lectura
    #Restar la dimension actual en 1 por cada expresion
    #Verificar que el resultado no sea menor a cero
    #Guardar las dimensiones (tops de pila) en la variable que estas utilizando
    # funcion{nombre, tipo, tablaVariables}
    # tablaVariables{nombre, tipo, dirección, dimension, dimensionx, dimensiony, referencias[(1),(2,4),(5,6)]}
    # * (M(5*limS1+6)) (B) C

def p_posibleID2(p):
    '''
    posibleID2 : OCORCH np_agregarFondo expresion np_quitarFondo posibleID3 CCORCH
               | np_enviarACuadruplos2
    '''
def p_posibleID3(p):
    '''
    posibleID3 : COMA np_agregarFondo expresion np_quitarFondo np_verificarD2
               | np_verificarD1
    '''

def p_np_defIDActual(p):
    '''
    np_defIDActual :
    '''
    global IDActual
    IDActual.append(p[-1])

def p_np_quitarIDActual(p):
    '''
    np_quitarIDActual :
    '''
    global IDActual
    IDActual.pop()

def p_np_verificarD1(p):
    '''
    np_verificarD1 :
    '''
    gc.verificarD1(gc.mt.getDsVariable(gc.mt.getFuncionVariable(funcionActual,IDActual[-1]),IDActual[-1]),funcionActual,IDActual[-1])

def p_np_verificarD2(p):
    '''
    np_verificarD2 :
    '''
    gc.verificarD2(gc.mt.getDsVariable(gc.mt.getFuncionVariable(funcionActual,IDActual[-1]),IDActual[-1]), funcionActual, IDActual[-1])

def p_posibleIDDeclaracion_1(p):
    '''
    posibleIDDeclaracion : ID np_addVariable np_enviarACuadruplos np_actualizarDimensiones
                         | ID np_addVariable np_enviarACuadruplos np_actualizarDimensiones OCORCH ENTERO np_addConstanteINT np_asignarD1 CCORCH np_asignarMemoria1
                         | ID np_addVariable np_enviarACuadruplos np_actualizarDimensiones OCORCH ENTERO np_addConstanteINT np_asignarD1 COMA ENTERO np_addConstanteINT np_asignarD2 CCORCH np_asignarMemoria2
    '''

def p_np_asignarD1(p):
    '''
    np_asignarD1 :
    '''
    gc.mt.asignard1(funcionActual,p[-7],p[-2])

def p_np_asignarD2(p):
    '''
    np_asignarD2 :
    '''
    gc.mt.asignard2(funcionActual,p[-11],p[-2])

def p_np_asignarMemoria1(p):
    '''
    np_asignarMemoria1 :
    '''
    gc.mt.asignarMemoria(funcionActual,p[-9],tipoVariable)

def p_np_asignarMemoria2(p):
    '''
    np_asignarMemoria2 :
    '''
    gc.mt.asignarMemoria(funcionActual,p[-13],tipoVariable)

def p_estatutoRepeticionIncondicional(p):
    '''
    estatutoRepeticionIncondicional : DESDE ID np_verificarValorUnico np_contieneID HASTA np_iniciaFor np_agregarFondo expresion np_quitarFondo np_forFalso HAZ OBRACKET estatutos CBRACKET np_terminaFor
    '''
def p_np_verificarValorUnico(p):
    '''
    np_verificarValorUnico :
    '''
    if gc.mt.getDimensionVariable(gc.mt.getFuncionVariable(funcionActual,p[-1]),p[-1]) != 0:
        print("La variable de condición del for no debe tener más de una dimensión.")
        exit(-1)

def p_np_iniciaFor(p):
    '''
    np_iniciaFor :
    '''
    gc.forStatementInicia(funcionActual, p[-4])

def p_np_forFalso(p):
    '''
    np_forFalso :
    '''
    gc.forStatementFalso()

def p_np_terminaFor(p):
    '''
    np_terminaFor :
    '''
    gc.forStatementTermina(funcionActual)

def p_estatutoRepeticionCondicional(p):
    '''
    estatutoRepeticionCondicional : MIENTRAS OPAREN np_agregarFondo npWhileStExp expresion np_quitarFondo CPAREN HAZ OBRACKET npWhileInicia estatutos CBRACKET npWhileTermina
    '''

def p_npWhileStExp(p):
    '''
    npWhileStExp :
    '''
    gc.whileStatementExpresion()

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
    gc.regresa(gc.mt.getTipoFuncion(funcionActual),'X',funcionActual)

def p_np_returnVOID(p):
    '''
    np_returnVOID :
    '''
    gc.regresa(gc.mt.getTipoFuncion(funcionActual),'VOID',funcionActual)

def p_np_contieneID(p):
    '''
    np_contieneID :
    '''
    if not gc.mt.contieneID(funcionActual,p[-2]):
        print("El ID:",p[-1],"no existe en la funcion:", funcionActual)
        exit(-1)

def p_np_addConstanteINT(p):
    '''
    np_addConstanteINT :
    '''
    temp = p[-1]
    if esUMINUS == True:
        temp = -temp
        #print("SI CAMBIO!",temp,"!!!!!!!!!!!!!!!!!!!!!\n\n\n\n")
    gc.mt.addConstante(str(temp), "INT")
    gc.constanteCuadruplo(int(temp))
    gc.operando(str(temp),'INT',0,'CONSTANTES')

def p_np_addConstanteFLOAT(p):
    '''
    np_addConstanteFLOAT :
    '''
    temp = p[-1]
    if esUMINUS == True:
        temp = -temp
        #print("SI CAMBIO!",temp,"!!!!!!!!!!!!!!!!!!!!!\n\n\n\n")
    gc.mt.addConstante(str(temp), "FLOAT")
    gc.constanteCuadruplo(float(temp))
    gc.operando(str(temp),'FLOAT',0,'CONSTANTES')

def p_np_addConstanteCHAR(p):
    '''
    np_addConstanteCHAR :
    '''
    #print("Llego")
    gc.mt.addConstante(p[-1][1],"CHAR")
    #print(p[-1][1],"WOOOOW")
    gc.constanteCuadruplo(p[-1][1])
    gc.operando(p[-1][1],'CHAR',0,'CONSTANTES')

def p_np_addVariable(p):
    '''
    np_addVariable :
    '''
    gc.mt.addVariable(funcionActual, p[-1], tipoVariable, esParametro)

def p_np_enviarACuadruplos(p):
    '''
    np_enviarACuadruplos :
    '''
    gc.operando(p[-2],gc.mt.getTipoVariable(funcionActual,p[-2]),gc.mt.getDimensionVariable(funcionActual,p[-2]),funcionActual)

def p_np_enviarACuadruplos2(p):
    '''
    np_enviarACuadruplos2 :
    '''
    gc.operando(IDActual[-1],gc.mt.getTipoVariable(funcionActual,IDActual[-1]),gc.mt.getDimensionVariable(funcionActual,IDActual[-1]),funcionActual)

def p_np_actualizarDimensiones(p):
    '''
    np_actualizarDimensiones :
    '''
    gc.mt.actualizarDimensiones(funcionActual,p[-3],currentDimension)

def p_np_agregarFondo(p):
    '''
    np_agregarFondo :
    '''
    #print("se agregó fondo exitosamente.")
    gc.operador('(')

def p_np_quitarFondo(p):
    '''
    np_quitarFondo :
    '''
    #print("Se quitó fondo exitosamente!")
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

def p_error(p):
    print("Hay un error de sintaxis en la línea %s!"%p.lineno)
    exit(-1)

parser = yacc.yacc(start='')

f = open("testBinarySearch.txt", "r")
result = parser.parse(f.read())

print(result)
