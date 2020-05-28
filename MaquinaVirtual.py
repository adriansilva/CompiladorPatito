
class MaquinaVirtual:

    heap = None
    stack = None

    isParam = None

    def __init__(self):
        self.heap = {}      # memoria que almacena variables globales, constantes y temporales
        self.stack = [{}]   # memoria local, cada ves que se usa una funcion, se agrega otro diccionario a esta
                            # lista de diccionarios y representa una nueva seccion de memoria

        self.isParam = False

    def processInput(self, cuadruplos, mt):
        ip = 0
        pilaReturn = []

        print("INICIA MAQUINA VIRTUAL")

        while cuadruplos[ip][0] != 'END':

            #input(cuadruplos[ip])

            # GOTO ---------------------------------

            if cuadruplos[ip][0] == 'GOTO':
                ip = cuadruplos[ip][3] - 1
                continue

            if cuadruplos[ip][0] == 'GOTOF':

                if self.getValue(cuadruplos[ip][1]) == False:
                    ip = cuadruplos[ip][3] - 1
                    continue

            if cuadruplos[ip][0] == 'GOTOV':

                if self.getValue(cuadruplos[ip][1]) == True:
                    ip = cuadruplos[ip][3] - 1
                    continue

            # operadores primitivos ---------------------------------

            if cuadruplos[ip][0][0] == '+':
                #print("Entró al +")
                if len(cuadruplos[ip][0]) > 1:
                    print("deberia entrar.")
                    '''
                    Para este punto, ya se asegura el cubo de que las dimensiones de cada arreglo
                    sean las correctas para realizar las operaciones. Sólo falta la lógica de la
                    operación dependiendo de cada caso. (arreglo+valor, arreglo+arreglo, matriz+valor, etc)
                    '''
                    if cuadruplos[ip][0][1] == '1' and cuadruplos[ip][0][2] == '0':
                            #Falta implementarlo para que funcione con pointers.
                            valor = self.getValue(cuadruplos[ip][1][0]+i) + self.getValue(cuadruplos[ip][2][0])
                            self.setValue(cuadruplos[ip][3]+i, valor)

                            #print("i:",cuadruplos[ip][1][0]+i)
                            #print("valor:",valor)
                            #print("Entro aquí xd.")
                    if cuadruplos[ip][0][1] == '1' and cuadruplos[ip][0][2] == '1':
                        #Aquí sería que cada elemento del arreglo 1 le sumas su respectivo elemento de arreglo2
                        pass
                    if cuadruplos[ip][0][1] == '2' and cuadruplos[ip][0][2] == '0':
                        #A todos los elementos de la matriz, le sumas el valor único
                        pass
                    if cuadruplos[ip][0][1] == '2' and cuadruplos[ip][0][2] == '1':
                        #Para todas las filas de la matriz, le sumas respectivamente el valor de cada columna del arreglo
                        pass
                    if cuadruplos[ip][0][1] == '2' and cuadruplos[ip][0][2] == '2':
                        #Por cada elemento de la matriz 1 le sumas su respectivo valor de la matriz 2
                        pass

                else:
                    if cuadruplos[ip][3] >= 24000: # si se esta asignando a un pointer, entonces el 3 elemento del cuadurplo no va a ser un address, si no una constante
                        valor = self.getValue(cuadruplos[ip][1]) + cuadruplos[ip][2]
                        self.setPointer(cuadruplos[ip][3], valor)
                    else:
                        valor = self.getValue(cuadruplos[ip][1]) + self.getValue(cuadruplos[ip][2])
                        self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == '-':
                valor = self.getValue(cuadruplos[ip][1]) - self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == '*':
                valor = self.getValue(cuadruplos[ip][1]) * self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == '/':
                valor = self.getValue(cuadruplos[ip][1]) / self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            # ASIGNACION ---------------------------------

            if cuadruplos[ip][0] == '=':

                if cuadruplos[ip][3]  >= 13000 and cuadruplos[ip][3] < 16000: # SI estamos agregando una constante
                    constante = cuadruplos[ip][1]
                    self.setValue(cuadruplos[ip][3], constante)

                else:
                    valor = self.getValue(cuadruplos[ip][1])
                    self.setValue(cuadruplos[ip][3], valor)


            # RELOP ---------------------------------

            if cuadruplos[ip][0] == '<':
                valor = self.getValue(cuadruplos[ip][1]) < self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == '<=':
                valor = self.getValue(cuadruplos[ip][1]) <= self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == '>':
                valor = self.getValue(cuadruplos[ip][1]) > self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == '>=':
                valor = self.getValue(cuadruplos[ip][1]) >= self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == '==':
                valor = self.getValue(cuadruplos[ip][1]) == self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == '<>':
                valor = self.getValue(cuadruplos[ip][1]) != self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            # LOGIC ---------------------------------
            if cuadruplos[ip][0] == '&&':
                valor = self.getValue(cuadruplos[ip][1]) and self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == '||':
                valor = self.getValue(cuadruplos[ip][1]) or self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            # PRINT ---------------------------------

            if cuadruplos[ip][0] == 'PRINT':
                #print(cuadruplos[ip][1]," print.")
                print(self.getValue(cuadruplos[ip][1]))

            # READ ---------------------------------

            if cuadruplos[ip][0] == 'READ':
                temp = input("input: ")
                try:
                    val = int(temp)
                    if ((cuadruplos[ip][3] >= 5000 and cuadruplos[ip][3] <6000) or
                        (cuadruplos[ip][3] >= 9000 and cuadruplos[ip][3] <10000) or
                        (cuadruplos[ip][3] >= 13000 and cuadruplos[ip][3] <14000) or
                        (cuadruplos[ip][3] >= 16000 and cuadruplos[ip][3] <18000)):
                        self.setValue(cuadruplos[ip][3], temp)
                    else:
                        print("ERROR DE ASIGNACION: El tipo de dato introducido (INT) no matchea con la variable.")
                        exit(-1)

                except ValueError:
                    try:
                        val = float(temp)
                        if ((cuadruplos[ip][3] >= 6000 and cuadruplos[ip][3] <7000) or
                            (cuadruplos[ip][3] >= 10000 and cuadruplos[ip][3] <11000) or
                            (cuadruplos[ip][3] >= 14000 and cuadruplos[ip][3] <15000) or
                            (cuadruplos[ip][3] >= 18000 and cuadruplos[ip][3] <20000)):
                            self.setValue(cuadruplos[ip][3], temp)
                        else:
                            print("ERROR DE ASIGNACION: El tipo de dato introducido (FLOAT) no matchea con la variable.")
                            exit(-1)
                    except ValueError:
                        if ((cuadruplos[ip][3] >= 7000 and cuadruplos[ip][3] <8000) or
                            (cuadruplos[ip][3] >= 11000 and cuadruplos[ip][3] <12000) or
                            (cuadruplos[ip][3] >= 15000 and cuadruplos[ip][3] <16000) or
                            (cuadruplos[ip][3] >= 20000 and cuadruplos[ip][3] <22000)):
                            self.setValue(cuadruplos[ip][3], temp)
                        else:
                            print("ERROR DE ASIGNACION: El tipo de dato introducido (CHAR/STRING) no matchea con la variable.")
                            exit(-1)

            # FUNCION ---------------------------------
            if cuadruplos[ip][0] == 'ERA': # agrega un segmento de memoria
                self.stack.append({})
                self.isParam = True

            if cuadruplos[ip][0] == 'PARAM':
                valor = self.getValue(cuadruplos[ip][1])
                self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == 'ENDfunc': # elimina segmento de memoria
                self.stack.pop()
                ip = pilaReturn.pop()
                continue

            if cuadruplos[ip][0] == 'GOSUB':
                pilaReturn.append(ip + 1)
                ip = cuadruplos[ip][3] - 1
                self.isParam = False
                continue

            if cuadruplos[ip][0] == 'RETURN':
                valor = self.getValue(cuadruplos[ip][1])
                self.setValue(cuadruplos[ip][3], valor)


            # ARREGLOS Y MATRICES ---------------------------------
            if cuadruplos[ip][0] == 'VER':
                if self.getValue(cuadruplos[ip][1]) < 0 or self.getValue(cuadruplos[ip][1]) > cuadruplos[ip][3]:
                    print("RUNTIME ERROR: el indice de acceso excede el tamano de la variable")
                    exit(-1)

            # INCREMENTA INSTRUCTION POINTER
            ip += 1

    def getValue(self, address):

        if self.isParam:
            if address >= 9000 and address < 13000: # la direccion es local entonces esta almacenada en stack
                return self.stack[-2][address]

        if address >= 9000 and address < 13000: # la direccion es local entonces esta almacenada en stack
            return self.stack[-1][address]

        if address >= 16000 and address < 24000: # la direccion es temporal entonces esta almacenada en stack.
            return self.stack[-1][address]

        if address >= 24000: #la direccion es un pointer a otro address. #Se deberia de agregar esto tambien dentro de stack y a is param?
            try:
                newAddress = self.heap[address]
                return self.getValue(newAddress)
            except:
                print("La dirreccion del arreglo/matriz a la que se trata de accesar no ha sido no ha sido asignada")
                exit(-1)

        else: # la direccion esta almacenada en heap
            return self.heap[address]

    def setValue(self, address, value):

        if address >= 9000 and address < 13000: # la direccion es local entonces esta almacenada en stack
            self.stack[-1][address] = value

        if address >= 16000 and address < 24000: # la direccion es temporal entonces esta almacenada en stack
            self.stack[-1][address] = value

        if address >= 24000:
            newAddress = self.heap[address]
            self.setValue(newAddress, value)

        else: # la direccion esta almacenada en heap
            self.heap[address] = value

    def setPointer(self, pointer, address):
        self.heap[pointer] = address
