import cuboSemantico as cs
import os,sys
import tablas

class generadorDeCuadruplos:
    pilaSaltos = None #Pila que almacena índice del cuádruplo al que se tiene que saltar
    pilaMigajas = None #Pila que almacena dirección de GOTOs pendientes
    pilaOperandos = None #Pila de operandos
    pilaOperadores = None #Pila de operadores
    pilaTipos = None #Pila del tipo del operando
    pilaDimensiones = None #Pila de las dimensiones del operando
    pilaDs = None #Pila de las Ds del operando (d1,d2) en forma de cuádruplo
    pilaReturns = None #Pila que almacena las posiciones de los returns para indicarle a los GOTOs donde termina la función
    pilaIDFor = None #Pila que almacena los IDs utilizados en la validación del for. Se modifican cada vez que se cumple un ciclo
    pilaParams = None #Pila de los parámetros de una función que ayuda a definir es string con los tipos y la cantidad de parámetros de una función
    outputCuadruplos = None #Pila de los cuádruplos generados
    constanteDeclarada = None #Revisa si el cuadruplo de asignacion de una constate ya existe
    firmaFunc = None #Pila utilizada para comparar elementos enviados en una llamada de función con la firma de dicha función.
    contadorParam = None #Verifica que los parámetros enviados a una función coincidan con su firma
    mt = None #Instancia del manejador de tablas


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
        self.pilaIDFor = []
        self.pilaParams = []
        self.constanteDeclarada = []
        self.mt = tablas.ManejadorDeTablas()
        self.firmaFunc = []
        self.contadorParam = []


    #Se le asigna el número del cuádruplo donde empieza la función
    def updateDirFunc(self,func):
        self.mt.tablaFunciones[func].inicianCuadruplos = len(self.outputCuadruplos)+1

    '''
    A continuación se presentan todos los posibles casos de generador de cuádruplos de operadores y cual es su estructura:

    ['='   ,   dir1   ,    (d1Dir1, d2Dir1)    ,    dir1]
    ['=xx'   ,   dir1    ,    ((d1dir1,d2dir1),(d1dir2,d2dir2))    ,    dir2]
    [operacion   ,   dir1   ,   dir2   ,   temporal]
    ['operacion xx'    ,    (dir1, (d1dir1,d2dir1))   ,    (dir2,(d1dir2,d2dir2))    ,    dir3]

    *Donde las x representan las dimensiones del primer y segundo operando respectivamente.


    Para todos los '=':

        Si es un = normal, los cuádruplos se verán asi: ['=', direccion, (d1Direccion, d2Direccion), direccion2]
        (Esto es asi porque significa que estamos igualando un valor único a otro y no hace falta saber la dimensión de ambos
        {de hecho de ninguno, pero se hizo para respetar un orden})

        Si es un =xx (operador especial), los cuádruplos se verán asi: ['=xx',direccion1,((d1dir1,d2dir1),(d1dir2,d2dir2)),direccion2]
        Esto lo necesitamos porque para operaciones de dimensiones diferentes (matriz = arreglo) necesitamos los tamaños de ambos
        para realizar la operación.

    Para todos los operadores diferentes a '=' (+,-.*,$,?...):

        Si es el operador sólo, los cuádruplos se verán asi: [operacion,direccion1,direccion2,temporal] (nuevamente como se trata
        de valores únicos, no nos tenemos que preocupar por dimensiones)

        Si el operador va acompañado de las dimensiones ('*xx') los cuádruplos se verán asi:
        ['operacion xx',(direccion, (d1direccion,d2direccion)),(direccion2,(d1direccion2,d2direccion2)),direccion3],
        (las ds están justo a un lado de su respectiva dirección) ya es un hecho que la direccion3 tiene el tamaño del
        resultado de la operación de dir1 y dir2.


    '''
    def operador(self, o):
        #Si es paréntesis abierto, se agrega un fondo falso
        if o == '(':
            self.pilaOperadores.append('(')

        #Si se cierra el paréntesis, se limpia toda la pila hasta el fondo falso
        if o == ')':
            while self.pilaOperadores[-1] != '(':
                tempOperador = self.pilaOperadores.pop()
                tempOperando2 = self.pilaOperandos.pop()
                tempOperando1 = self.pilaOperandos.pop()
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

                # Si el operador inicia con un '=' hay 3 opciones disponibles:
                # 1. es un '==', esto se condidera en el if y en caso de ser '==' se trata como cualquier otro operador
                # 2. Es un '=' solo. Esto tiene su propio caso en el que la información del cuádruplo generado varía.
                # 3. Se trata de un operado '=xx'. Dentro de la excepción se condiera el caso en el que el operador incluye
                #    información de las dimensiones.

                # En el caso en el que el operador es algún otro diferente a '=', igual se considera la situación
                # en la que este operador tiene información de dimensiones ('*xx'). De ser así, se genera un cuádruplo
                # diferente al de la operación normal.

                if (resultado[0][0] == '=' and len(resultado[0])>1 and resultado[0][1] != '=') or resultado[0][0] == '=' and len(resultado[0])==1:
                    self.outputCuadruplos.append(list((resultado[0],tempOperando2,resultado[3],tempOperando1)))
                    self.pilaOperandos.append(tempOperando1)
                else:
                    nuevoTemporal = self.mt.getNewTemporal(resultado[1],resultado[3][0],resultado[3][1])
                    if '0' in resultado[0] or '1' in resultado[0] or '2' in resultado[0]:
                        self.outputCuadruplos.append(list((resultado[0],(tempOperando1,dsO1),(tempOperando2,dsO2),nuevoTemporal)))
                    else:
                        self.outputCuadruplos.append(list((resultado[0],tempOperando1,tempOperando2,nuevoTemporal)))
                    self.pilaOperandos.append(nuevoTemporal)
                self.pilaTipos.append(resultado[1])
                self.pilaDimensiones.append(resultado[2])
                self.pilaDs.append(resultado[3])
            self.pilaOperadores.pop()

        if o in ['$','?','¡']:
            # El proceso para procesar los operadores matriciales difiere de todos los demás. Como estamos tratando
            # con una operación en la que sólo participa 1 operando, se utiliza una versión especial del cubo
            # que recibe la información de un único operando.
            self.pilaOperadores.append(o)
            while self.pilaOperadores and self.pilaOperadores[-1] in ['$','?','¡']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
                tempOperador = self.pilaOperadores.pop()
                tempOperando1 = self.pilaOperandos.pop()
                dsO1 = self.pilaDs.pop()

                resultado = cs.cuboSolitario(self.pilaTipos.pop(),tempOperador,self.pilaDimensiones.pop(),dsO1)

                # La lógica de inserción es igual que la de los demás operandos, se puede apreciar la descripción
                # del manejo de los datos de los demás operandos más abajo.
                nuevoTemporal = self.mt.getNewTemporal(resultado[1],resultado[3][0],resultado[3][1])

                self.outputCuadruplos.append(list((resultado[0],tempOperando1,(dsO1,resultado[3]),nuevoTemporal)))
                self.pilaOperandos.append(nuevoTemporal)
                self.pilaTipos.append(resultado[1])
                self.pilaDimensiones.append(resultado[2])
                self.pilaDs.append(resultado[3])


        '''
            La estructura y la lógica es la misma para todos los casos de operadores:
            Si el operador está en el top de la pila, mientras haya operadores de igual o mayor jerarquía, los resuelves.
        '''
        if o in ['*','/']:
            while self.pilaOperadores and self.pilaOperadores[-1] in ['*','/','$','?','¡']: #mientras haya operadores de mayor o igual jerarquia, ejecutarlos.
                tempOperador = self.pilaOperadores.pop()
                tempOperando2 = self.pilaOperandos.pop()
                tempOperando1 = self.pilaOperandos.pop()

                # Se le manda información al cubo del tipo, las dimensiones y las ds de los operandos participando en la operación
                # El resultado determinará el tipo, las dimensiones y las ds del objeto resultante de la operación. Se guarda en un
                # temporal para procesarse.
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

                nuevoTemporal = self.mt.getNewTemporal(resultado[1],resultado[3][0],resultado[3][1])

                # Al procesarse si el cubo nos dice que la operación es especial (participan arreglos o matríces),
                # Se agrega el cuádruplo correspondiente. Se tiene un cuádruplo para operación especial y operación normal
                # porque la información que necesita la máquina virtual depende de la operación y las dimensiones.
                if '0' in resultado[0] or '1' in resultado[0] or '2' in resultado[0]:
                    self.outputCuadruplos.append(list((resultado[0],(tempOperando1,dsO1),(tempOperando2,dsO2),nuevoTemporal)))
                else:
                    self.outputCuadruplos.append(list((resultado[0],tempOperando1,tempOperando2,nuevoTemporal)))

                # Al final se agrega el temporal a la pila para ser utilizado después en otra operación.
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


        # Como el = es el operador de menor jerarquía, sólo se añade a la pila de operadores
        # porque no va a ser procesado hasta quitar el fondo bajo nuestra implementación.
        if o == '=':
            self.pilaOperadores.append(o)

    def operando(self, o, tipo, dimensiones, func):
        # Se busca la dirección del operando y se añaden sus características a sus respectivas pilaSaltos
        self.pilaOperandos.append(self.mt.getDireccionVariable(func,o))
        self.pilaTipos.append(tipo)
        self.pilaDimensiones.append(dimensiones)
        self.pilaDs.append(self.mt.getDsVariable(func,o))

    def constanteCuadruplo(self, con):
        # Se genera un cuádruplo para definir una constante en la tabla de constantes. Este proceso se repite muchas veces
        # a pesar de ya tener la cosntante declarada para asegurarse que esa constante en el flujo de ejecución ya está declarada.
        self.outputCuadruplos.append(list(('=', con, (1,1), self.mt.getDireccionVariable('CONSTANTES', str(con)))))

    def print(self, func, s = None):
        if s == None:
            self.outputCuadruplos.append(list(('PRINT', self.pilaOperandos[-1], self.pilaDs[-1], None)))
        else:
            self.outputCuadruplos.append(list(('PRINT', s[1:-1], None, None)))

    def read(self, id, func):
        #Se genera el cuádruplo del Read
        self.outputCuadruplos.append(list(('READ', None, None, self.mt.getDireccionVariable(func,id))))

    def ifStatement(self):
        # Inicia el if statement
        operando = self.pilaOperandos.pop()

        # Se valida que la comparación haya sido boleana y que no se utilice un objeto multidimensionado en la comparación
        if self.pilaTipos.pop() == 'BOOL' and self.pilaDimensiones.pop() == 0:
            self.pilaMigajas.append(len(self.outputCuadruplos))
            self.outputCuadruplos.append(list(('GOTOF',operando,None,None)))

        else:
            print("La expresion del if en el cuadruplo:", len(self.outputCuadruplos), "no tiene resultado boleano o no es un valor único.")
            exit(-1)

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
            self.outputCuadruplos.append(list(('<',self.pilaIDFor[-1],operando,nuevoTemporal)))

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

    def verificarD1(self, ds, func, var):
        tempOperando = self.pilaOperandos.pop()
        tempTipo = self.pilaTipos.pop()
        tempDimension = self.pilaDimensiones.pop()
        tempDs = self.pilaDs.pop()

        #Verificar que el top de la pila esté en el rango válido para ese objeto multidimensional
        self.outputCuadruplos.append(list(('VER',tempOperando,0,ds[0])))

        resultado = cs.cubo(tempTipo,"INT",
                            "*",
                            tempDimension,0,
                            tempDs,(1,1))

        nuevoTemporal = self.mt.getNewTemporal(resultado[1],1,1)

        #Se multiplica el index por la cantidad de columnas que hay para realizar el desplazamiento
        #Si se tratara de un arreglo, se multiplicaría el index x 1
        self.outputCuadruplos.append(list(('*',tempOperando,self.mt.getDireccionVariable('CONSTANTES',str(ds[1])),nuevoTemporal)))

        resultado2 = cs.cubo(resultado[1],"INT",
                            "+",
                            resultado[2],0,
                            resultado[3],(1,1))

        nuevoTemporal2 = self.mt.getNewTemporal("POINT",1,1)

        #Se le suma la dirección base
        self.outputCuadruplos.append(list(('+',nuevoTemporal,self.mt.getDireccionVariable(func,var),nuevoTemporal2)))

        self.pilaOperandos.append(nuevoTemporal2)
        self.pilaTipos.append(self.mt.getTipoVariable(func,var))
        self.pilaDimensiones.append(self.mt.getDimensionVariable(func,var)-1)

        tempD = self.mt.getDsVariable(func,var)
        self.pilaDs.append((tempD[1],1))

        #Si las dimensiones son menores a cero, se indexó un valor único.
        if self.pilaDimensiones[-1] < 0:
            print("No se puede accesar a una dimensión no existente de la variable:",var)
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

        #Verificar que el top de la pila esté en el rango válido para ese objeto multidimensional
        self.outputCuadruplos.append(list(('VER',tempOperando1,0,ds[0])))
        self.outputCuadruplos.append(list(('VER',tempOperando2,0,ds[1])))

        resultado = cs.cubo(tempTipo1,"INT",
                            "*",
                            tempDimension1,0,
                            tempDs1,(1,1))

        nuevoTemporal = self.mt.getNewTemporal(resultado[1],1,1)

        #Se multiplica el index por la cantidad de columnas que hay para realizar el desplazamiento
        self.outputCuadruplos.append(list(('*',tempOperando1,self.mt.getDireccionVariable('CONSTANTES',str(ds[1])),nuevoTemporal)))

        resultado2 = cs.cubo(resultado[1],"INT",
                            "+",
                            resultado[2],0,
                            resultado[3],(1,1))

        nuevoTemporal2 = self.mt.getNewTemporal("INT",1,1)

        #Se le suma el index de la columna a la memoria
        self.outputCuadruplos.append(list(('+',nuevoTemporal,tempOperando2,nuevoTemporal2)))

        resultado3 = cs.cubo(resultado2[1],"INT",
                            "+",
                            resultado2[2],0,
                            resultado2[3],(1,1))

        nuevoTemporal3 = self.mt.getNewTemporal("POINT",1,1)

        #Se le suma la dirección base
        self.outputCuadruplos.append(list(('+',nuevoTemporal2,self.mt.getDireccionVariable(func,var),nuevoTemporal3)))

        self.pilaOperandos.append(nuevoTemporal3)
        self.pilaTipos.append(self.mt.getTipoVariable(func,var))
        self.pilaDimensiones.append(self.mt.getDimensionVariable(func,var)-2)
        self.pilaDs.append((1,1))

        #Si las dimensiones son menores a cero, se indexó un valor único.
        if self.pilaDimensiones[-1] < 0:
            print("No se puede accesar a una dimensión no existente de la variable:",var)
            exit(-1)

    def regresa(self,tipoFunc,tipoVar,func):
        #genera cuadrulplo de RETURN y Goto para guardar el valor y saltar a ENDFunc
        self.mt.tablaFunciones[func].tieneReturn = True
        if tipoVar == 'VOID': #si la funcion es VOID no neecesita return
            if tipoFunc == 'VOID':
                self.outputCuadruplos.append(list(('RETURN',None,None,None)))
                self.pilaReturns.append(len(self.outputCuadruplos))
                self.outputCuadruplos.append(list(('GOTO',None,None,None)))
            else:
                print("El tipo de retorno no matche(VOID) con el tipo de la función.")
                exit(-1)
        else: #si la funcion no es void, tiene que haber un return, y el tipo de la variable debe de ser igual que el tipo de la funcion
            if self.pilaTipos[-1] != tipoFunc:
                print("El tipo de retorno no matche(!=VOID) con el tipo de la función.")
                exit(-1)
            else:
                operando = self.pilaOperandos.pop()
                tipo = self.pilaTipos.pop()
                self.pilaDimensiones.pop()
                self.pilaDs.pop()

                self.outputCuadruplos.append(list(('RETURN',operando,None,self.mt.getDireccionVariable('PROGRAMA', func))))
                self.pilaReturns.append(len(self.outputCuadruplos))
                self.outputCuadruplos.append(list(('GOTO',None,None,None)))

    def endFunc(self, func):
        #si la funcion no tiene return y no es void, marca error
        if not self.mt.tablaFunciones[func].tieneReturn and self.mt.getTipoFuncion(func) != 'VOID':
            print("Todas las funciones de tipo diferente a VOID necesitan un REGRESA.")
            exit(-1)
        whereToJump = len(self.outputCuadruplos)+1
        while len(self.pilaReturns) > 0:
            index = self.pilaReturns.pop()
            self.outputCuadruplos[index][3] = whereToJump

        #genera cuadruplo ENDfunc
        self.outputCuadruplos.append(list(('ENDfunc',None,None,None)))

    def llamadaFuncion(self,func): #genera cuadruplo que crea segmento de memoria en STACK
        self.outputCuadruplos.append(list(('ERA',None,None,func)))

    def agregarFondoParam(self, nombreFuncion):
        self.pilaParams.append('(')

        self.firmaFunc.append(self.mt.getParamsFuncion(nombreFuncion))
        self.contadorParam.append([9000,10000,11000,12000])


    def quitarFondoParam(self,nombreFuncion): #revisa que los parametros mandados en la llamada tengan el mismo numero y tipos que la funcion
        params = ""
        while self.pilaParams[-1] != '(': #genera firma de los argumentos
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
        if params != self.mt.getParamsFuncion(nombreFuncion): #consigue firma de la funcion
            print("El número de parámetros o los tipos no coinciden entre la llamada y la función:",nombreFuncion)
            print("Params llamada:",params," /// Params función:",self.mt.getParamsFuncion(nombreFuncion))
            exit(-1)
        else:
            #print("Se llamó exitosamente a la función",nombreFuncion,"!\n\n\n\n\n")
            pass

        self.firmaFunc.pop()
        self.contadorParam.pop()

    def resolverParam(self, func):
        # genera cuadruplo que guarda un parametro en una direccion de memoria
        operando = self.pilaOperandos.pop()
        self.pilaParams.append(self.pilaTipos.pop())
        self.pilaDimensiones.pop()
        dsO1 = self.pilaDs.pop()

        tipoParam = self.firmaFunc[-1][0]

        if len(self.firmaFunc[-1]) > 1:
            self.firmaFunc[-1] = self.firmaFunc[-1][1:]

        address = None
        #obtiene tipo e parametro para comparar con firma de funcion
        if tipoParam == 'i':
            address = self.contadorParam[-1][0]
            self.contadorParam[-1][0] += dsO1[0]*dsO1[1]
        elif tipoParam == 'f':
            address = self.contadorParam[-1][1]
            self.contadorParam[-1][1] += dsO1[0]*dsO1[1]
        if tipoParam == 'c':
            address = self.contadorParam[-1][2]
            self.contadorParam[-1][2] += dsO1[0]*dsO1[1]
        if tipoParam == 'b':
            address = self.contadorParam[-1][3]
            self.contadorParam[-1][3] += dsO1[0]*dsO1[1]

        self.outputCuadruplos.append(list(('PARAM',operando,dsO1,address)))

    def goSUB(self,func):
        # genera cuadruplo GOSUB para ir a la funcion 'func'
        self.outputCuadruplos.append(list(('GOSUB',None,None,self.mt.getFuncComienza(func))))

        tipoNuevoTemporal = self.mt.getTipoFuncion(func)
        if tipoNuevoTemporal != 'VOID':
            nuevoTemporal = self.mt.getNewTemporal(tipoNuevoTemporal,1,1)

            # genera cuadruplo de parche guadalupano para guardar el resultado que regresa de la funcion en un temporal
            self.outputCuadruplos.append(list(('=',self.mt.getDireccionVariable('PROGRAMA',func),(1,1),nuevoTemporal)))
            self.operando('Temporal_'+str(nuevoTemporal),tipoNuevoTemporal,0,'TEMPORALES')

    def gotoMain(self):
        # genera cuadrupllo que va a PRINCIPAL despues de declarar variables globales
        self.pilaMigajas.append(len(self.outputCuadruplos))
        self.outputCuadruplos.append(list(('GOTO',None,None,None)))

    def updateMain(self):
        # actualiza cuadruplo de goto main ya que no tenia direccion a donde saltar hasta llegar a main
        update = self.pilaMigajas.pop()
        self.outputCuadruplos[update][3] = len(self.outputCuadruplos) + 1

    def endProgram(self):
        # genera cuadruplo de final de programa
        self.outputCuadruplos.append(list(('END',None, None,None)))

    def printCuadruplos(self):
        f = open('outputCuadruplos.txt','w')

        for c in self.outputCuadruplos:
            print(c, file=f)

    def returnCuadruplos(self):
        return self.outputCuadruplos
