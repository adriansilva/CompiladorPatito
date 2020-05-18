class generadorDeCuadruplos:
    pilaSaltos = None
    pilaMigajas = None #Pila que almacena dirección de GOTOs pendientes
    pilaOperandos = None
    pilaOperadores = None
    pilaTipos = None
    pilaDimensiones = None
    outputCuadruplos = None

    def __init__(self):
        pilaSaltos = []
        pilaOperandos = []
        pilaOperadores = []
        pilaTipos = []
        pilaDimensiones = []
        outputCuadruplos = []

    def operador(o):
        if o in ['*','/']:
        if o in ['+','-']:
        if o in ['&&', '||']:
        if o in ['<=','>=','<>','>','<','==']:
        if o == '=':

        #Para cada operador, implementar lógica de pops y push
    def operando(o):
        #Añadir a pila de operandos
        #Añadir a pila de tipos
        #Añadir a pila de dimensiones

    def ifStatement():
        operando = pilaOperandos[-1]

        if pilaTipos[-1] == 'BOOL' and pilaDimensiones[-1] == 0:
            pilaMigajas.append(len(outputCuadruplos))
            outputCuadruplos.append(('GOTOF',operando,None,None))
        else:
            print("La expresion del if en el cuadruplo:", len(outputCuadruplos), "no tiene resultado boleano o es un valor único.")
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
        3. GOTOF T2  7
        4. ...
        5. ...
        6. ...
        7. GOTOV T2 9
        8. ...
        9. Termina else
        '''

    def terminaIfStatement():
        indiceCuadruploAModificar = pilaMigajas.pop()
        outputCuadruplos[indiceCuadruploAModificar][3] = len(outputCuadruplos)
        #Actualizas GOTOF del top de pila de migajas con línea actual

    def elseStatement():
        #Se saca el resultado de A==B+C de las pilas
        operando = pilaOperandos.pop()
        pilaTipos.pop()
        pilaDimensiones.pop()

        pilaMigajas.append(len(outputCuadruplos))
        outputCuadruplos.append(('GOTOV',operando,None,None))
        #Meter línea actual a pila de migajas
        #Generas cuadruplo GOTOV


    def terminaElseStatement():
        indiceCuadruploAModificar = pilaMigajas.pop()
        outputCuadruplos[indiceCuadruploAModificar][3] = len(outputCuadruplos)
        #Actualizas GOTOV del top de pila de migajas con línea actual

    def whileStatementExpresion():
        pilaSaltos.append(len(outputCuadruplos))
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

    def whileStatementInicia():
        operando = pilaOperandos.pop()
        pilaTipos.pop()
        pilaDimensiones.pop()

        if pilaTipos.pop() == 'BOOL' and pilaDimensiones.pop() == 0:
            pilaMigajas.append(len(outputCuadruplos))
            outputCuadruplos.append(('GOTOF',operando,None,None))
        else:
            print("La expresion del while en el cuadruplo:", len(outputCuadruplos), "no tiene resultado boleano o es un valor único.")
            exit(-1)

        #Agregas a pila de migajas línea actual (tamaño de outputCuadruplos)
        #Generas cuadruplo GOTOF

    def whileStatementTermina():
        outputCuadruplos.append(('GOTO',None,None,pilaSaltos.pop()))

        indiceCuadruploAModificar = pilaMigajas.pop()
        outputCuadruplos[indiceCuadruploAModificar][3] = len(outputCuadruplos)
        #Generas cuadruplo GOTO a top pila de saltos
        #Actualizas GOTOF que está en el top de las migajas con línea actual (tamaño de outputCuadruplos)

    def forStatementExpresion():
        pilaSaltos.append(len(outputCuadruplos))
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

    def forStatementInicia():
        operando = pilaOperandos.pop()
        pilaTipos.pop()
        pilaDimensiones.pop()

        if pilaTipos.pop() == 'INT' and pilaDimensiones.pop() == 0:
            #Si la 'X' es mayor a tu expresion, ya terminaste el for. Es necesario convertir a boleano para usar el GOTOV
            outputCuadruplos.append(('>',pilaOperandos[-1],operando,'Temporal_'+str(contadorTemporales)))

            #Se necesita crear aquí la nueva variable temporal para que se utilice

            pilaMigajas.append(len(outputCuadruplos))
            outputCuadruplos.append(('GOTOV','Temporal_'+str(contadorTemporales),None,None))
        else:
            print("La expresion del for en el cuadruplo:", len(outputCuadruplos), "no tiene resultado entero o es un valor único.")
            exit(-1)
        #Agregas a pila de migajas línea actual (tamaño de outputCuadruplos)
        #Generas cuadruplo GOTOF

    def forStatementTermina():
        #Se saca la 'X' de las pilas
        pilaOperandos.pop()
        pilaTipos.pop()
        pilaDimensiones.pop()

        outputCuadruplos.append(('GOTO',None,None,pilaSaltos.pop()))

        indiceCuadruploAModificar = pilaMigajas.pop()
        outputCuadruplos[indiceCuadruploAModificar][3] = len(outputCuadruplos)
        #Generas cuadruplo GOTO hacia top de pila de pilaSaltos
        #Actualizar top de pila de migajas con línea actual
