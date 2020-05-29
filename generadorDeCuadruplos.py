import cuboSemantico as cs
import os,sys
import tablas

class generadorDeCuadruplos:
    pilaSaltos = None
    pilaMigajas = None #Pila que almacena dirección de GOTOs pendientes
    pilaOperandos = None
    pilaOperadores = None
    pilaTipos = None
    pilaDimensiones = None
    pilaDs = None
    outputCuadruplos = None
    contadorTemporales = None
    pilaReturns = None
    pilaIDFor = None
    pilaParams = None
    constanteDeclarada = None # revisa si el cuadruplo de asignacion de una constate ya existe
    firmaFunc = None
    contadorParam = None
    mt = None


    def __init__(self):
        self.pilaSaltos = []
        self.pilaOperandos = []
        self.pilaOperadores = []
        self.pilaTipos = []
        self.pilaDimensiones = []
        self.outputCuadruplos = []
        self.pilaMigajas = []
        self.pilaReturns = []
        self.pilaDs = []
        self.contadorTemporales = 0
        self.pilaIDFor = []
        self.pilaParams = []
        self.constanteDeclarada = []
        self.mt = tablas.ManejadorDeTablas()
        self.firmaFunc = []
        self.contadorParam = []


    def updateDirFunc(self,func):
        self.mt.tablaFunciones[func].inicianCuadruplos = len(self.outputCuadruplos)+1
        #print("La dirección del cuádruplo donde empieza la función",func,"es:",self.mt.tablaFunciones[func].inicianCuadruplos)

    # TODO: FALTA agregar el tipo del temporal y sus dimensiones a las pilas respectivas
    # TODO: FALTA hacer check que las operaciones entre variables sean validas
    def operador(self, o):
        #Si es paréntesis abierto, se agrega un fondo falso
        if o == '(':
            self.pilaOperadores.append('(')
        #Si se cierra el paréntesis, se limpia toda la pila hasta el fondo falso

        if o == ')':
            #print('Se está limpiando la pila...')
            while self.pilaOperadores[-1] != '(':
                tempOperador = self.pilaOperadores.pop()
                tempOperando2 = self.pilaOperandos.pop()
                tempOperando1 = self.pilaOperandos.pop()
                #print((tempOperador,tempOperando1,tempOperando2))
                resultado = cs.cubo(self.pilaTipos[-2],self.pilaTipos[-1],
                                    tempOperador,
                                    self.pilaDimensiones[-2],self.pilaDimensiones[-1],
                                    self.pilaDs[-2],self.pilaDs[-1])

                self.pilaTipos.pop()
                self.pilaTipos.pop()
                self.pilaDimensiones.pop()
                self.pilaDimensiones.pop()
                dsO2 = self.pilaDs.pop()
                dsO1 = self.pilaDs.pop()
                print(tempOperador)
                print(resultado[0])
                if resultado[0][0] == '=':
                    self.outputCuadruplos.append(list((resultado[0],tempOperando2,resultado[3],tempOperando1)))
                    self.pilaOperandos.append(tempOperando1)
                else:
                    nuevoTemporal = self.mt.getNewTemporal(resultado[1],resultado[3][0],resultado[3][1])
                    if '0' in resultado[0] or '1' in resultado[0] or '2' in resultado[0]:
                        self.outputCuadruplos.append(list((resultado[0],(tempOperando1,dsO1),(tempOperando2,dsO2),nuevoTemporal)))
                    else:
                        self.outputCuadruplos.append(list((resultado[0],tempOperando1,tempOperando2,nuevoTemporal)))
                    self.pilaOperandos.append(nuevoTemporal) #Falta agregar ds a temporal
                self.pilaTipos.append(resultado[1])
                self.pilaDimensiones.append(resultado[2])
                self.pilaDs.append(resultado[3])
            self.pilaOperadores.pop()

        if o in ['$','?','¡']:
            while self.pilaOperadores and self.pilaOperadores[-1] in ['$','?','¡']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
                tempOperador = self.pilaOperadores.pop()
                tempOperando2 = self.pilaOperandos.pop()
                tempOperando1 = self.pilaOperandos.pop()
                #print((tempOperador,tempOperando1,tempOperando2))
                resultado = cs.cubo(self.pilaTipos[-2],self.pilaTipos[-1],
                                    tempOperador,
                                    self.pilaDimensiones[-2],self.pilaDimensiones[-1],
                                    self.pilaDs[-2],self.pilaDs[-1])

                self.pilaTipos.pop()
                self.pilaTipos.pop()
                self.pilaDimensiones.pop()
                self.pilaDimensiones.pop()
                dsO2 = self.pilaDs.pop()
                dsO1 = self.pilaDs.pop()
                print(tempOperador)
                print(resultado[0])
                nuevoTemporal = self.mt.getNewTemporal(resultado[1],resultado[3][0],resultado[3][1])
                if '0' in resultado[0] or '1' in resultado[0] or '2' in resultado[0]:
                    self.outputCuadruplos.append(list((resultado[0],(tempOperando1,dsO1),(tempOperando2,dsO2),nuevoTemporal)))
                else:
                    self.outputCuadruplos.append(list((resultado[0],tempOperando1,tempOperando2,nuevoTemporal)))
                self.pilaOperandos.append(nuevoTemporal)

                self.pilaTipos.append(resultado[1])
                self.pilaDimensiones.append(resultado[2])
                self.pilaDs.append(resultado[3])

            self.pilaOperadores.append(o)

        if o in ['*','/']:
            while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/','$','?','¡']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
                tempOperador = self.pilaOperadores.pop()
                tempOperando2 = self.pilaOperandos.pop()
                tempOperando1 = self.pilaOperandos.pop()
                #print((tempOperador,tempOperando1,tempOperando2))
                resultado = cs.cubo(self.pilaTipos[-2],self.pilaTipos[-1],
                                    tempOperador,
                                    self.pilaDimensiones[-2],self.pilaDimensiones[-1],
                                    self.pilaDs[-2],self.pilaDs[-1])

                self.pilaTipos.pop()
                self.pilaTipos.pop()
                self.pilaDimensiones.pop()
                self.pilaDimensiones.pop()
                dsO2 = self.pilaDs.pop()
                dsO1 = self.pilaDs.pop()
                print(tempOperador)
                print(resultado[0])
                nuevoTemporal = self.mt.getNewTemporal(resultado[1],resultado[3][0],resultado[3][1])
                if '0' in resultado[0] or '1' in resultado[0] or '2' in resultado[0]:
                    self.outputCuadruplos.append(list((resultado[0],(tempOperando1,dsO1),(tempOperando2,dsO2),nuevoTemporal)))
                else:
                    self.outputCuadruplos.append(list((resultado[0],tempOperando1,tempOperando2,nuevoTemporal)))
                self.pilaOperandos.append(nuevoTemporal)

                self.pilaTipos.append(resultado[1])
                self.pilaDimensiones.append(resultado[2])
                self.pilaDs.append(resultado[3])

            self.pilaOperadores.append(o)

        if o in ['+','-']:
            while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/', '+','-','$','?','¡']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
                tempOperador = self.pilaOperadores.pop()
                tempOperando2 = self.pilaOperandos.pop()
                tempOperando1 = self.pilaOperandos.pop()
                #print((tempOperador,tempOperando1,tempOperando2))
                resultado = cs.cubo(self.pilaTipos[-2],self.pilaTipos[-1],
                                    tempOperador,
                                    self.pilaDimensiones[-2],self.pilaDimensiones[-1],
                                    self.pilaDs[-2],self.pilaDs[-1])

                self.pilaTipos.pop()
                self.pilaTipos.pop()
                self.pilaDimensiones.pop()
                self.pilaDimensiones.pop()
                dsO2 = self.pilaDs.pop()
                dsO1 = self.pilaDs.pop()
                print(tempOperador)
                print(resultado[0])
                nuevoTemporal = self.mt.getNewTemporal(resultado[1],resultado[3][0],resultado[3][1])
                if '0' in resultado[0] or '1' in resultado[0] or '2' in resultado[0]:
                    self.outputCuadruplos.append(list((resultado[0],(tempOperando1,dsO1),(tempOperando2,dsO2),nuevoTemporal)))
                else:
                    self.outputCuadruplos.append(list((resultado[0],tempOperando1,tempOperando2,nuevoTemporal)))
                self.pilaOperandos.append(nuevoTemporal)

                self.pilaTipos.append(resultado[1])
                self.pilaDimensiones.append(resultado[2])
                self.pilaDs.append(resultado[3])

            self.pilaOperadores.append(o)

        if o in ['<=','>=','<>','>','<','==']:

            while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/', '+','-', '<=','>=','<>','>','<','==','$','?','¡']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
                tempOperador = self.pilaOperadores.pop()
                tempOperando2 = self.pilaOperandos.pop()
                tempOperando1 = self.pilaOperandos.pop()
                #print((tempOperador,tempOperando1,tempOperando2))
                resultado = cs.cubo(self.pilaTipos[-2],self.pilaTipos[-1],
                                    tempOperador,
                                    self.pilaDimensiones[-2],self.pilaDimensiones[-1],
                                    self.pilaDs[-2],self.pilaDs[-1])

                self.pilaTipos.pop()
                self.pilaTipos.pop()
                self.pilaDimensiones.pop()
                self.pilaDimensiones.pop()
                dsO2 = self.pilaDs.pop()
                dsO1 = self.pilaDs.pop()
                print(tempOperador)
                print(resultado[0])
                nuevoTemporal = self.mt.getNewTemporal(resultado[1],resultado[3][0],resultado[3][1])
                if '0' in resultado[0] or '1' in resultado[0] or '2' in resultado[0]:
                    self.outputCuadruplos.append(list((resultado[0],(tempOperando1,dsO1),(tempOperando2,dsO2),nuevoTemporal)))
                else:
                    self.outputCuadruplos.append(list((resultado[0],tempOperando1,tempOperando2,nuevoTemporal)))
                self.pilaOperandos.append(nuevoTemporal)

                self.pilaTipos.append(resultado[1])
                self.pilaDimensiones.append(resultado[2])
                self.pilaDs.append(resultado[3])

            self.pilaOperadores.append(o)

        if o in ['&&', '||']:
            while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/', '+','-', '<=','>=','<>','>','<','==', '&&', '||','$','?','¡']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
                tempOperador = self.pilaOperadores.pop()
                tempOperando2 = self.pilaOperandos.pop()
                tempOperando1 = self.pilaOperandos.pop()
                #print((tempOperador,tempOperando1,tempOperando2))
                resultado = cs.cubo(self.pilaTipos[-2],self.pilaTipos[-1],
                                    tempOperador,
                                    self.pilaDimensiones[-2],self.pilaDimensiones[-1],
                                    self.pilaDs[-2],self.pilaDs[-1])

                self.pilaTipos.pop()
                self.pilaTipos.pop()
                self.pilaDimensiones.pop()
                self.pilaDimensiones.pop()
                dsO2 = self.pilaDs.pop()
                dsO1 = self.pilaDs.pop()
                print(tempOperador)
                print(resultado[0])
                nuevoTemporal = self.mt.getNewTemporal(resultado[1],resultado[3][0],resultado[3][1])
                if '0' in resultado[0] or '1' in resultado[0] or '2' in resultado[0]:
                    self.outputCuadruplos.append(list((resultado[0],(tempOperando1,dsO1),(tempOperando2,dsO2),nuevoTemporal)))
                else:
                    self.outputCuadruplos.append(list((resultado[0],tempOperando1,tempOperando2,nuevoTemporal)))
                self.pilaOperandos.append(nuevoTemporal)

                self.pilaTipos.append(resultado[1])
                self.pilaDimensiones.append(resultado[2])
                self.pilaDs.append(resultado[3])

            self.pilaOperadores.append(o)


        if o == '=':

            self.pilaOperadores.append(o)

        '''
        if o == 'end':

            while self.pilaOperadores:

                if self.pilaOperadores[-1] == '=': # si es = entonces asigna el valor mas reciente en la pila de operandos a la variable siguiente de la pila de operandos, no se borra este sigueinte valor por si hay otra asignacion e.j. a = b = 1 - 2;
                    self.outputCuadruplos.append(list((self.pilaOperadores[-1], self.pilaOperandos[-1], None, self.pilaOperandos[-2])))
                    self.pilaOperadores.pop() #remueve operador 1
                    self.pilaOperandos.pop() #remueve operando 1
                else:
                    resultado = cs.cubo(self.pilaTipos[-2],self.pilaTipos[-1],self.pilaOperadores[-1],self.pilaDimensiones[-2],self.pilaDimensiones[-1])
                    nuevoTemporal = self.mt.getNewTemporal(resultado[0])

                    self.outputCuadruplos.append(list((self.pilaOperadores[-1], self.pilaOperandos[-2], self.pilaOperandos[-1], nuevoTemporal)))
                    self.pilaOperadores.pop() #remueve operador 1
                    self.pilaOperandos.pop() #remueve operando 1
                    self.pilaOperandos.pop() #remueve operando 2
                    self.pilaTipos.pop()
                    self.pilaTipos.pop()
                    self.pilaDimensiones.pop()
                    self.pilaDimensiones.pop()

                    self.pilaOperandos.append(nuevoTemporal)
                    self.pilaTipos.append(resultado[0])
                    self.pilaDimensiones.append(resultado[1])

            if self.pilaOperandos: # vaciar la pila de operandos si queda un valor residual. Sirve para el caso de: a = b = 2 * 3;
                self.pilaOperandos = []
        '''
        #Para cada operador, implementar lógica de pops y push
        #print("Se añadió un operador:",o)
        #print("Pila operadores:",self.pilaOperadores)
        #print("Pila operandos: ",self.pilaOperandos)
        #print("Pila tipos: ",self.pilaTipos)
        #print()

        for i in self.outputCuadruplos:
            #print(i)
            pass
        #print()

    def operando(self, o, tipo, dimensiones, func):
        #Añadir a pila de operandos
        #Añadir a pila de tipos
        #Añadir a pila de dimensiones
        self.pilaOperandos.append(self.mt.getDireccionVariable(func,o))
        self.pilaTipos.append(tipo)
        self.pilaDimensiones.append(dimensiones)
        self.pilaDs.append(self.mt.getDsVariable(func,o))
        print("Dimensioon:",dimensiones)
        #print("Se añadió un operando:", o)
        #print(self.pilaOperadores)

    def operandoMulti(self, o, tipo, dimensiones, func):
        #Añadir a pila de operandos
        #Añadir a pila de tipos
        #Añadir a pila de dimensiones
        self.pilaOperandos.append(self.mt.getDireccionVariable(func,o))
        self.pilaTipos.append(tipo)
        self.pilaDimensiones.append(dimensiones)
        self.pilaDs.append(self.mt.getDsVariable(func,o))
        print("Dimensioon:",dimensiones)
        #print("Se añadió un operando:", o)
        #print(self.pilaOperadores)

    def constanteCuadruplo(self, con):
        #if con not in self.constanteDeclarada:
        self.outputCuadruplos.append(list(('=', con, (1,1), self.mt.getDireccionVariable('CONSTANTES', str(con)))))
            #self.constanteDeclarada.append(con)

    def print(self, s = None):
        if s == None:
            self.outputCuadruplos.append(list(('PRINT', self.pilaOperandos[-1], None, None)))
        else:
            self.outputCuadruplos.append(list(('PRINT', s, None, None)))

    def read(self, id, func):
        self.outputCuadruplos.append(list(('READ', None, None, self.mt.getDireccionVariable(func,id))))

    def ifStatement(self):
        #print(self.pilaOperandos)
        #print(self.pilaTipos)
        operando = self.pilaOperandos.pop()

        if self.pilaTipos.pop() == 'BOOL' and self.pilaDimensiones.pop() == 0:
            #print("Migaja")
            self.pilaMigajas.append(len(self.outputCuadruplos))
            #print(self.pilaMigajas)
            self.outputCuadruplos.append(list(('GOTOF',operando,None,None)))
            #print(self.outputCuadruplos)
        else:
            print("La expresion del if en el cuadruplo:", len(self.outputCuadruplos), "no tiene resultado boleano o no es un valor único.")
            exit(-1)

        #Haces pop a pila de operandos
        #Te aseguras que el tipo sea
        #Meter línea actual a pila de migajas
        #Generas cuadruplo GOTOF

    def terminaIfStatement(self):
        #El jump cuando la condición sea falsa es al final del if
        indiceCuadruploAModificar = self.pilaMigajas.pop()
        self.outputCuadruplos[indiceCuadruploAModificar][3] = len(self.outputCuadruplos)+1

    def elseStatement(self):
        indiceCuadruploAModificar = self.pilaMigajas.pop()
        self.outputCuadruplos[indiceCuadruploAModificar][3] = len(self.outputCuadruplos)+2

        self.pilaMigajas.append(len(self.outputCuadruplos))
        self.outputCuadruplos.append(list(('GOTO',None,None,None)))
        #El jump cuando al condición sea falsa es a donde comienza el else, después del jump al final del if-
        #Meter línea actual a pila de migajas
        #Generas cuadruplo GOTOV


    def terminaElseStatement(self):
        indiceCuadruploAModificar = self.pilaMigajas.pop()
        self.outputCuadruplos[indiceCuadruploAModificar][3] = len(self.outputCuadruplos)+1
        #Actualizas GOTO del top de pila de migajas con línea actual

    def whileStatementExpresion(self):
        self.pilaSaltos.append(len(self.outputCuadruplos) + 1)
        #Guardar linea actual en pila de saltos

    def whileStatementInicia(self):
        operando = self.pilaOperandos.pop()

        if self.pilaTipos.pop() == 'BOOL' and self.pilaDimensiones.pop() == 0:
            self.pilaMigajas.append(len(self.outputCuadruplos))
            self.outputCuadruplos.append(list(('GOTOF',operando,None,None)))
        else:
            print("La expresion del while en el cuadruplo:", len(self.outputCuadruplos), "no tiene resultado boleano o es un valor único.")
            exit(-1)

        #Agregas a pila de migajas línea actual (tamaño de outputCuadruplos)
        #Generas cuadruplo GOTOF

    def whileStatementTermina(self):
        self.outputCuadruplos.append(list(('GOTO',None,None,self.pilaSaltos.pop())))

        indiceCuadruploAModificar = self.pilaMigajas.pop()
        self.outputCuadruplos[indiceCuadruploAModificar][3] = len(self.outputCuadruplos) + 1
        #Generas cuadruplo GOTO a top pila de saltos
        #Actualizas GOTOF que está en el top de las migajas con línea actual (tamaño de outputCuadruplos)

    def forStatementInicia(self, funcionActual, id):
        if self.mt.getTipoVariable(funcionActual,id) == 'INT':
            self.pilaIDFor.append(self.mt.getDireccionVariable(funcionActual, id))
            self.pilaSaltos.append(len(self.outputCuadruplos)+1)
        else:
            print("El for necesita una variable entera para comparar.")
            exit(-1)

    def forStatementFalso(self):

        operando = self.pilaOperandos.pop()
        tipo = self.pilaTipos.pop()

        if tipo == 'INT' and self.pilaDimensiones.pop() == 0:
            #Si la 'X' es mayor a tu expresion, ya terminaste el for. Es necesario convertir a boleano para usar el GOTOV
            nuevoTemporal = self.mt.getNewTemporal('BOOL',1,1)
            self.outputCuadruplos.append(list(('<=',self.pilaIDFor[-1],operando,nuevoTemporal)))

            #Se necesita crear aquí la nueva variable temporal para que se utilice y guardarla en mt

            self.pilaMigajas.append(len(self.outputCuadruplos))
            self.outputCuadruplos.append(list(('GOTOF',nuevoTemporal,None,None)))
        else:
            print("La expresion del for en el cuadruplo:", len(self.outputCuadruplos), "no tiene resultado entero o es un valor único.")
            exit(-1)
        #Agregas a pila de migajas línea actual (tamaño de outputCuadruplos)
        #Generas cuadruplo GOTOF
        #Guardar linea actual en pila de saltos
        #Te aseguras que el tipo de la expresion sea entero

    def forStatementTermina(self,func):
        self.outputCuadruplos.append(list(('+',self.pilaIDFor[-1],self.mt.getDireccionVariable('CONSTANTES','1'),self.pilaIDFor.pop())))
        #Cambiar 1 por dirección de tabla de constantes

        self.outputCuadruplos.append(list(('GOTO',None,None,self.pilaSaltos.pop())))

        indiceCuadruploAModificar = self.pilaMigajas.pop()
        self.outputCuadruplos[indiceCuadruploAModificar][3] = len(self.outputCuadruplos)+1
        #Generas cuadruplo GOTO hacia top de pila de pilaSaltos
        #Actualizar top de pila de migajas con línea actual

    def regresa(self,tipoFunc,tipoVar,func):
        #print(tipoFunc," <---Func | Var---> ",self.pilaTipos[-1])
        self.mt.tablaFunciones[func].tieneReturn = True
        if tipoVar == 'VOID':
            if tipoFunc == 'VOID':
                self.outputCuadruplos.append(list(('RETURN',None,None,None)))
                self.pilaReturns.append(len(self.outputCuadruplos))
                self.outputCuadruplos.append(list(('GOTO',None,None,None)))
            else:
                print("El tipo de retorno no matche(VOID) con el tipo de la función.")
                exit(-1)
        else:
            if self.pilaTipos[-1] != tipoFunc:
                print("El tipo de retorno no matche(!=VOID) con el tipo de la función.")
                exit(-1)
            else:
                operando = self.pilaOperandos.pop()
                tipo = self.pilaTipos.pop()
                self.pilaDimensiones.pop()

                self.outputCuadruplos.append(list(('RETURN',operando,None,self.mt.getDireccionVariable('PROGRAMA', func))))
                self.pilaReturns.append(len(self.outputCuadruplos))
                self.outputCuadruplos.append(list(('GOTO',None,None,None)))

    def endFunc(self, func):
        if not self.mt.tablaFunciones[func].tieneReturn and self.mt.getTipoFuncion(func) != 'VOID':
            print("Todas las funciones de tipo diferente a VOID necesitan un REGRESA.")
            exit(-1)
        whereToJump = len(self.outputCuadruplos)+1
        while len(self.pilaReturns) > 0:
            index = self.pilaReturns.pop()
            self.outputCuadruplos[index][3] = whereToJump

        self.outputCuadruplos.append(list(('ENDfunc',None,None,None)))

    def llamadaFuncion(self,func):
        self.outputCuadruplos.append(list(('ERA',None,None,func)))

    def agregarFondoParam(self, nombreFuncion):
        self.pilaParams.append('(')

        self.firmaFunc.append(self.mt.getParamsFuncion(nombreFuncion))
        self.contadorParam.append([9000,10000,11000,12000])


    def quitarFondoParam(self,nombreFuncion):
        params = ""
        while self.pilaParams[-1] != '(':
            param = self.pilaParams.pop()
            if param == 'INT':
                params = "i" + params
            if param == 'FLOAT':
                params = "f" + params
            if param == 'CHAR':
                params = "c" + params
            if param == 'BOOL':
                params = "b" + params

        self.pilaParams.pop()
        if params != self.mt.getParamsFuncion(nombreFuncion):
            print("El número de parámetros o los tipos no coinciden entre la llamada y la función:",nombreFuncion)
            print("Params llamada:",params," /// Params función:",self.mt.getParamsFuncion(nombreFuncion))
            exit(-1)
        else:
            print("Se llamó exitosamente a la función",nombreFuncion,"!\n\n\n\n\n")

        self.firmaFunc.pop()
        self.contadorParam.pop()

    def verificarD1(self, ds, func, var):
        tempOperando = self.pilaOperandos.pop()
        tempTipo = self.pilaTipos.pop()
        tempDimension = self.pilaDimensiones.pop()
        tempDs = self.pilaDs.pop()

        self.outputCuadruplos.append(list(('VER',tempOperando,0,ds[0])))

        resultado = cs.cubo(tempTipo,"INT",
                            "*",
                            tempDimension,0,
                            tempDs,(1,1))

        nuevoTemporal = self.mt.getNewTemporal(resultado[1],1,1)

        self.outputCuadruplos.append(list(('*',tempOperando,self.mt.getDireccionVariable('CONSTANTES',str(ds[1])),nuevoTemporal)))

        resultado2 = cs.cubo(resultado[1],"INT",
                            "+",
                            resultado[2],0,
                            resultado[3],(1,1))

        nuevoTemporal2 = self.mt.getNewTemporal("POINT",1,1)

        self.outputCuadruplos.append(list(('+',nuevoTemporal,self.mt.getDireccionVariable(func,var),nuevoTemporal2)))
        print(nuevoTemporal2)
        self.pilaOperandos.append(nuevoTemporal2)
        self.pilaTipos.append(self.mt.getTipoVariable(func,var))
        self.pilaDimensiones.append(self.mt.getDimensionVariable(func,var)-1)
        print("Esto es la func:",func)
        print("Esta es la variable:",var)
        tempD = self.mt.getDsVariable(func,var)
        print(tempD)
        self.pilaDs.append((tempD[1],1))
        print(self.pilaDs[-1])

        if self.pilaDimensiones[-1] < 0:
            print("VerD1 No se puede accesar a una dimensión no existente de la variable:",var)
            exit(-1)

    def verificarD2(self, ds, func, var):
        tempOperando2 = self.pilaOperandos.pop()
        tempTipo2 = self.pilaTipos.pop()
        tempDimension2 = self.pilaDimensiones.pop()
        tempDs2 = self.pilaDs.pop()

        tempOperando1 = self.pilaOperandos.pop()
        tempTipo1 = self.pilaTipos.pop()
        tempDimension1 = self.pilaDimensiones.pop()
        tempDs1 = self.pilaDs.pop()

        self.outputCuadruplos.append(list(('VER',tempOperando1,0,ds[0])))
        self.outputCuadruplos.append(list(('VER',tempOperando2,0,ds[1])))

        resultado = cs.cubo(tempTipo1,"INT",
                            "*",
                            tempDimension1,0,
                            tempDs1,(1,1))

        nuevoTemporal = self.mt.getNewTemporal(resultado[1],1,1)

        self.outputCuadruplos.append(list(('*',tempOperando1,self.mt.getDireccionVariable('CONSTANTES',str(ds[1])),nuevoTemporal)))

        resultado2 = cs.cubo(resultado[1],"INT",
                            "+",
                            resultado[2],0,
                            resultado[3],(1,1))

        nuevoTemporal2 = self.mt.getNewTemporal("INT",1,1)

        self.outputCuadruplos.append(list(('+',nuevoTemporal,tempOperando2,nuevoTemporal2)))

        resultado3 = cs.cubo(resultado2[1],"INT",
                            "+",
                            resultado2[2],0,
                            resultado2[3],(1,1))

        nuevoTemporal3 = self.mt.getNewTemporal("POINT",1,1)

        self.outputCuadruplos.append(list(('+',nuevoTemporal2,self.mt.getDireccionVariable(func,var),nuevoTemporal3)))

        self.pilaOperandos.append(nuevoTemporal3)
        self.pilaTipos.append(self.mt.getTipoVariable(func,var))
        self.pilaDimensiones.append(self.mt.getDimensionVariable(func,var)-2)
        self.pilaDs.append((1,1))

        if self.pilaDimensiones[-1] < 0:
            print("No se puede accesar a una dimensión no existente de la variable:",var)
            exit(-1)

    def resolverParam(self, func):
        #if self.pilaTipos[-1] !=
        operando = self.pilaOperandos.pop()
        self.pilaParams.append(self.pilaTipos.pop())
        self.pilaDimensiones.pop()

        tipoParam = self.firmaFunc[-1][0]

        if len(self.firmaFunc[-1]) > 1:
            self.firmaFunc[-1] = self.firmaFunc[-1][1:]

        address = None

        if tipoParam == 'i':
            address = self.contadorParam[-1][0]
            self.contadorParam[-1][0] += 1
        elif tipoParam == 'f':
            address = self.contadorParam[-1][1]
            self.contadorParam[-1][1] += 1
        if tipoParam == 'c':
            address = self.contadorParam[-1][2]
            self.contadorParam[-1][2] += 1
        if tipoParam == 'b':
            address = self.contadorParam[-1][3]
            self.contadorParam[-1][3] += 1

        #Falta determinar donde se va a guardar el parámetro,
        #probablemente en alguna variable dentro de la función objetivo
        self.outputCuadruplos.append(list(('PARAM',operando,None,address)))

    def goSUB(self,func):
        self.outputCuadruplos.append(list(('GOSUB',None,None,self.mt.getFuncComienza(func))))

        tipoNuevoTemporal = self.mt.getTipoFuncion(func)
        nuevoTemporal = self.mt.getNewTemporal(tipoNuevoTemporal,1,1)

        self.outputCuadruplos.append(list(('=',self.mt.getDireccionVariable('PROGRAMA',func),self.mt.getDimensionVariable('PROGRAMA',func),nuevoTemporal)))
        self.operando('Temporal_'+str(nuevoTemporal),tipoNuevoTemporal,0,'TEMPORALES')

    def gotoMain(self):
        self.pilaMigajas.append(len(self.outputCuadruplos))
        self.outputCuadruplos.append(list(('GOTO',None,None,None)))

    def updateMain(self):
        update = self.pilaMigajas.pop()
        self.outputCuadruplos[update][3] = len(self.outputCuadruplos) + 1

    def endProgram(self):
        self.outputCuadruplos.append(list(('END',None, None,None)))

    def printCuadruplos(self):
        f = open('outputCuadruplos.txt','w')

        for c in self.outputCuadruplos:
            print(c, file=f)

    def returnCuadruplos(self):
        return self.outputCuadruplos
