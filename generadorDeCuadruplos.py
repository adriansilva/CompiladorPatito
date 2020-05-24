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
    outputCuadruplos = None
    contadorTemporales = None
    pilaReturns = None
    pilaIDFor = None
    pilaParams = None
    constanteDeclarada = None # revisa si el cuadruplo de asignacion de una constate ya existe
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
        self.contadorTemporales = 0
        self.pilaIDFor = []
        self.pilaParams = []
        self.constanteDeclarada = []
        self.mt = tablas.ManejadorDeTablas()


    # TODO: FALTA agregar el tipo del temporal y sus dimensiones a las pilas respectivas
    # TODO: FALTA hacer check que las operaciones entre variables sean validas
    def operador(self, o):
        #Si es paréntesis abierto, se agrega un fondo falso
        if o == '(':
            self.pilaOperadores.append('(')
        #Si se cierra el paréntesis, se limpia toda la pila hasta el fondo falso

        if o == ')':
            print('Se está limpiando la pila...')
            while self.pilaOperadores[-1] != '(':
                tempOperador = self.pilaOperadores.pop()
                tempOperando2 = self.pilaOperandos.pop()
                tempOperando1 = self.pilaOperandos.pop()
                #print((tempOperador,tempOperando1,tempOperando2))
                resultado = cs.cubo(self.pilaTipos[-2],self.pilaTipos[-1],tempOperador,self.pilaDimensiones[-2],self.pilaDimensiones[-1])

                self.pilaTipos.pop()
                self.pilaTipos.pop()
                self.pilaDimensiones.pop()
                self.pilaDimensiones.pop()
                if tempOperador == '=':
                    self.outputCuadruplos.append(list((tempOperador,tempOperando2,None,tempOperando1)))
                    self.pilaOperandos.append(tempOperando1)
                else:
                    nuevoTemporal = self.mt.getNewTemporal(resultado[0])
                    self.outputCuadruplos.append(list((tempOperador,tempOperando1,tempOperando2,nuevoTemporal)))
                    self.pilaOperandos.append(nuevoTemporal)
                self.pilaTipos.append(resultado[0])
                self.pilaDimensiones.append(resultado[1])
            self.pilaOperadores.pop()

        if o in ['*','/']:
            while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
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

            self.pilaOperadores.append(o)

        if o in ['+','-']:
            while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/', '+','-']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
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

            self.pilaOperadores.append(o)

        if o in ['<=','>=','<>','>','<','==']:

            while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/', '+','-', '<=','>=','<>','>','<','==']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
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

            self.pilaOperadores.append(o)

        if o in ['&&', '||']:
            while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/', '+','-', '<=','>=','<>','>','<','==', '&&', '||']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
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

            self.pilaOperadores.append(o)


        if o == '=':

            self.pilaOperadores.append(o)


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

        #Para cada operador, implementar lógica de pops y push
        #print("Se añadió un operador:",o)
        #print("Pila operadores:",self.pilaOperadores)
        #print("Pila operandos: ",self.pilaOperandos)
        #print("Pila tipos: ",self.pilaTipos)
        #print()

        for i in self.outputCuadruplos:
            print(i)
        print()

    def operando(self, o, tipo, dimensiones, func):
        #Añadir a pila de operandos
        #Añadir a pila de tipos
        #Añadir a pila de dimensiones
        self.pilaOperandos.append(self.mt.getDireccionVariable(func,o))
        self.pilaTipos.append(tipo)
        self.pilaDimensiones.append(dimensiones)

        print("Se añadió un operando:", o)
        #print(self.pilaOperadores)

    def constanteCuadruplo(self, con):
        if con not in self.constanteDeclarada:
            self.outputCuadruplos.append(list(('=', con, None, self.mt.getDireccionVariable('CONSTANTES', str(con)))))
            self.constanteDeclarada.append(con)

    def print(self, s = None):
        if s == None:
            self.outputCuadruplos.append(list(('PRINT', self.pilaOperandos[-1], None, None)))
        else:
            self.outputCuadruplos.append(list(('PRINT', s, None, None)))

    def read(self, id, func):
        self.outputCuadruplos.append(list(('READ', None, None, self.mt.getDireccionVariable(func,id))))

    def ifStatement(self):
        print(self.pilaOperandos)
        print(self.pilaTipos)
        operando = self.pilaOperandos.pop()

        if self.pilaTipos.pop() == 'BOOL' and self.pilaDimensiones.pop() == 0:
            #print("Migaja")
            self.pilaMigajas.append(len(self.outputCuadruplos))
            print(self.pilaMigajas)
            self.outputCuadruplos.append(list(('GOTOF',operando,None,None)))
            print(self.outputCuadruplos)
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
            nuevoTemporal = self.mt.getNewTemporal('BOOL')
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

    def regresa(self,tipoFunc,tipoVar):
        print(tipoFunc," <---Func | Var---> ",self.pilaTipos[-1])
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

                self.outputCuadruplos.append(list(('RETURN',None,None,operando)))
                self.pilaReturns.append(len(self.outputCuadruplos))
                self.outputCuadruplos.append(list(('GOTO',None,None,None)))

    def endFunc(self):
        whereToJump = len(self.outputCuadruplos)+1
        while len(self.pilaReturns) > 0:
            index = self.pilaReturns.pop()
            self.outputCuadruplos[index][3] = whereToJump

        self.outputCuadruplos.append(list(('ENDfunc',None,None,None)))

    def llamadaFuncion(self,func):
        self.outputCuadruplos.append(list(('ERA',None,None,func)))

    def agregarFondoParam(self):
        self.pilaParams.append('(')

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

    def resolverParam(self, func):
        #if self.pilaTipos[-1] !=
        operando = self.pilaOperandos.pop()
        self.pilaParams.append(self.pilaTipos.pop())
        self.pilaDimensiones.pop()
        #Falta determinar donde se va a guardar el parámetro,
        #probablemente en alguna variable dentro de la función objetivo
        self.outputCuadruplos.append(list(('PARAM',operando,None,'Tabla de Variables de: '+func)))

    def goSUB(self,func):
        self.outputCuadruplos.append(list(('GOSUB',None,None,func)))

        tipoNuevoTemporal = self.mt.getTipoFuncion(func)
        nuevoTemporal = self.mt.getNewTemporal(tipoNuevoTemporal)

        self.outputCuadruplos.append(list(('=',self.mt.getDireccionVariable('PROGRAMA',func),None,nuevoTemporal)))
        #print("OPERANDOOOO")
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