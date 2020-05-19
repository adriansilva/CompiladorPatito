class generadorDeCuadruplos:
    pilaSaltos = None
    pilaMigajas = None #Pila que almacena dirección de GOTOs pendientes
    pilaOperandos = None
    pilaOperadores = None
    pilaTipos = None
    pilaDimensiones = None
    outputCuadruplos = None

    def __init__(self):
        self.pilaSaltos = []
        self.pilaOperandos = []
        self.pilaOperadores = []
        self.pilaTipos = []
        self.pilaDimensiones = []
        self.outputCuadruplos = []

    # TODO: FALTA agregar el tipo del temporal y sus dimensiones a las pilas respectivas
    # TODO: FALTA hacer check que las operaciones entre variables sean validas
    def operador(self, o):
        #Si es paréntesis abierto, se agrega un fondo falso
        if o == '(':
            self.pilaOperadores.append('(')
        #Si se cierra el paréntesis, se limpia toda la pila hasta el fondo falso
        if o == ')':
            while self.pilaOperadores[-1] not '(':
                tempOperador = self.pilaOperadores.pop()
                tempOperando2 = self.pilaOperandos.pop()
                tempOperando1 = self.pilaOperandos.pop()
                self.outputCuadruplos.append((tempOperador,tempOperando1,tempOperando2,'Temporal_'+str(contadorTemporales)))
                self.pilaOperandos.append('Temporal_'+str(contadorTemporales))
            self.pilaOperadores.pop()

        if o in ['*','/']:
             while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
                self.outputCuadruplos.append((self.pilaOperadores[-1], self.pilaOperandos[-2], self.pilaOperandos[-1], 'Temporal_'+str(contadorTemporales)))
                self.pilaOperadores.pop() #remueve operador 1
                self.pilaOperandos.pop() #remueve operando 1
                self.pilaOperandos.pop() #remueve operando 2
                self.pilaOperandos.append('Temporal_'+str(contadorTemporales))
                contadorTemporales = contadorTemporales + 1

            self.pilaOperadores.append(o)

        if o in ['+','-']:

            while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/', '+','-']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
                self.outputCuadruplos.append((self.pilaOperadores[-1], self.pilaOperandos[-2], self.pilaOperandos[-1], 'Temporal_'+str(contadorTemporales)))
                self.pilaOperadores.pop() #remueve operador 1
                self.pilaOperandos.pop() #remueve operando 1
                self.pilaOperandos.pop() #remueve operando 2
                self.pilaOperandos.append('Temporal_'+str(contadorTemporales))
                contadorTemporales = contadorTemporales + 1

            self.pilaOperadores.append(o)

        if o in ['<=','>=','<>','>','<','==']:

            while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/', '+','-', '<=','>=','<>','>','<','==']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
                self.outputCuadruplos.append((self.pilaOperadores[-1], self.pilaOperandos[-2], self.pilaOperandos[-1], 'Temporal_'+str(contadorTemporales)))
                self.pilaOperadores.pop() #remueve operador 1
                self.pilaOperandos.pop() #remueve operando 1
                self.pilaOperandos.pop() #remueve operando 2
                self.pilaOperandos.append('Temporal_'+str(contadorTemporales))
                contadorTemporales = contadorTemporales + 1

            self.pilaOperadores.append(o)

        if o in ['&&', '||']:

            while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/', '+','-', '<=','>=','<>','>','<','==', '&&', '||']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
                self.outputCuadruplos.append((self.pilaOperadores[-1], self.pilaOperandos[-2], self.pilaOperandos[-1], 'Temporal_'+str(contadorTemporales)))
                self.pilaOperadores.pop() #remueve operador 1
                self.pilaOperandos.pop() #remueve operando 1
                self.pilaOperandos.pop() #remueve operando 2
                self.pilaOperandos.append('Temporal_'+str(contadorTemporales))
                contadorTemporales = contadorTemporales + 1

            self.pilaOperadores.append(o)


        if o == '=':

            self.pilaOperadores.append(o)


        if o == 'end':

            while self.pilaOperadores:

                if self.pilaOperadores[-1] == '=': # si es = entonces asigna el valor mas reciente en la pila de operandos a la variable siguiente de la pila de operandos, no se borra este sigueinte valor por si hay otra asignacion e.j. a = b = 1 - 2;
                    self.outputCuadruplos.append((self.pilaOperadores[-1], self.pilaOperandos[-1], None, self.pilaOperandos[-2]))
                    self.pilaOperadores.pop() #remueve operador 1
                    self.pilaOperandos.pop() #remueve operando 1
                else:
                    self.outputCuadruplos.append((self.pilaOperadores[-1], self.pilaOperandos[-2], self.pilaOperandos[-1], 'Temporal_'+str(contadorTemporales)))
                    self.pilaOperadores.pop() #remueve operador 1
                    self.pilaOperandos.pop() #remueve operando 1
                    self.pilaOperandos.pop() #remueve operando 2
                    self.pilaOperandos.append('Temporal_'+str(contadorTemporales))
                    contadorTemporales = contadorTemporales + 1

            if self.pilaOperandos: # vaciar la pila de operandos si queda un valor residual. Sirve para el caso de: a = b = 2 * 3;
                self.pilaOperandos = []

        #Para cada operador, implementar lógica de pops y push

    def operando(self, o, tipo, dimensiones):
        #Añadir a pila de operandos
        #Añadir a pila de tipos
        #Añadir a pila de dimensiones
        self.pilaOperandos.append(o)
        self.pilaTipos.append(tipo)
        self.pilaDimensiones.append(dimensiones)

    def ifStatement(self):
        operando = self.pilaOperandos.pop()

        if self.pilaTipos.pop() == 'BOOL' and self.pilaDimensiones.pop() == 0:
            self.pilaMigajas.append(len(self.outputCuadruplos))
            self.outputCuadruplos.append(('GOTOF',operando,None,None))
        else:
            print("La expresion del if en el cuadruplo:", len(self.outputCuadruplos), "no tiene resultado boleano o es un valor único.")
            exit(-1)
        #Haces pop a pila de operandos
        #Te aseguras que el tipo sea
        #Meter línea actual a pila de migajas
        #Generas cuadruplo GOTOF

        '''
        if(A==B+C){

        }
        else{

        }
        1. + B C T1
        2. == A T1 T2
        3. GOTOF T2 8
        4. ...
        5. ...
        6. ...
        7. GOTO   10
        8. ...
        9. Ultima instruccion del else
        10. sigue codigo normal
        '''

    def terminaIfStatement(self):
        #El jump cuando la condición sea falsa es al final del if
        indiceCuadruploAModificar = self.pilaMigajas.pop()
        self.outputCuadruplos[indiceCuadruploAModificar][3] = len(self.outputCuadruplos)
        #Actualizas GOTOF del top de pila de migajas con línea actual

    def elseStatement(self):
        self.outputCuadruplos.append(('GOTO',None,None,None))

        #El jump cuando al condición sea falsa es a donde comienza el else, después del jump al final del if-else
        indiceCuadruploAModificar = self.pilaMigajas.pop()
        self.outputCuadruplos[indiceCuadruploAModificar][3] = len(self.outputCuadruplos)
        #Meter línea actual a pila de migajas
        #Generas cuadruplo GOTOV


    def terminaElseStatement(self):
        indiceCuadruploAModificar = self.pilaMigajas.pop()
        self.outputCuadruplos[indiceCuadruploAModificar][3] = len(self.outputCuadruplos)
        #Actualizas GOTO del top de pila de migajas con línea actual

    def whileStatementExpresion(self):
        self.pilaSaltos.append(len(self.outputCuadruplos))
        #Guardar linea actual en pila de saltos
        '''
        MIENTRAS(A<=B+C)HAZ{

        }
        1. + B C T1
        2. <= A T1 T2
        3. GOTOF T2  8
        4. ...
        5. ...
        6. ...
        7. GOTO 1
        8. ...
        '''

    def whileStatementInicia(self):
        operando = self.pilaOperandos.pop()
        self.pilaTipos.pop()
        self.pilaDimensiones.pop()

        if self.pilaTipos.pop() == 'BOOL' and self.pilaDimensiones.pop() == 0:
            self.pilaMigajas.append(len(self.outputCuadruplos))
            self.outputCuadruplos.append(('GOTOF',operando,None,None))
        else:
            print("La expresion del while en el cuadruplo:", len(self.outputCuadruplos), "no tiene resultado boleano o es un valor único.")
            exit(-1)

        #Agregas a pila de migajas línea actual (tamaño de outputCuadruplos)
        #Generas cuadruplo GOTOF

    def whileStatementTermina(self):
        self.outputCuadruplos.append(('GOTO',None,None,self.pilaSaltos.pop()))

        indiceCuadruploAModificar = self.pilaMigajas.pop()
        self.outputCuadruplos[indiceCuadruploAModificar][3] = len(self.outputCuadruplos)
        #Generas cuadruplo GOTO a top pila de saltos
        #Actualizas GOTOF que está en el top de las migajas con línea actual (tamaño de outputCuadruplos)

    def forStatementExpresion(self):
        self.pilaSaltos.append(len(self.outputCuadruplos))
        #Guardar linea actual en pila de saltos
        #Te aseguras que el tipo de la expresion sea entero
        '''
        DESDE X HASTA Y*5 HAZ{

        }
        1. * Y 5 T1
        2. GOTOF 6
        3. ...
        4. ...
        5. GOTO 1
        6. ...
        '''

    def forStatementInicia(self):
        operando = self.pilaOperandos.pop()
        self.pilaTipos.pop()
        self.pilaDimensiones.pop()

        if self.pilaTipos.pop() == 'INT' and self.pilaDimensiones.pop() == 0:
            #Si la 'X' es mayor a tu expresion, ya terminaste el for. Es necesario convertir a boleano para usar el GOTOV
            self.outputCuadruplos.append(('>',self.pilaOperandos[-1],operando,'Temporal_'+str(contadorTemporales)))

            #Se necesita crear aquí la nueva variable temporal para que se utilice

            self.pilaMigajas.append(len(self.outputCuadruplos))
            self.outputCuadruplos.append(('GOTOV','Temporal_'+str(contadorTemporales),None,None))
        else:
            print("La expresion del for en el cuadruplo:", len(self.outputCuadruplos), "no tiene resultado entero o es un valor único.")
            exit(-1)
        #Agregas a pila de migajas línea actual (tamaño de outputCuadruplos)
        #Generas cuadruplo GOTOF

    def forStatementTermina(self):
        #Se saca la 'X' de las pilas
        self.pilaOperandos.pop()
        self.pilaTipos.pop()
        self.pilaDimensiones.pop()

        self.outputCuadruplos.append(('GOTO',None,None,self.pilaSaltos.pop()))

        indiceCuadruploAModificar = self.pilaMigajas.pop()
        self.outputCuadruplos[indiceCuadruploAModificar][3] = len(self.outputCuadruplos)
        #Generas cuadruplo GOTO hacia top de pila de pilaSaltos
        #Actualizar top de pila de migajas con línea actual
