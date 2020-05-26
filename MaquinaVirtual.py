
class MaquinaVirtual:

    heap = None
    stack = None

    def __init__(self):
        self.heap = {}      # memoria que almacena variables globales, constantes y temporales
        self.stack = [{}]   # memoria local, cada ves que se usa una funcion, se agrega otro diccionario a esta 
                            # lista de diccionarios y representa una nueva seccion de memoria

    def processInput(self, cuadruplos, mt):
        ip = 0

        print("INICIA MAQUINA VIRTUAL")

        while cuadruplos[ip][0] != 'END':

            #GOTO

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

            if cuadruplos[ip][0] == '+':
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


            # INCREMENTA INSTRUCTION POINTER
            ip += 1

    def getValue(self, address):

        if address >= 9000 and address < 13000: # la direccion es local entonces esta almacenada en stack
            return self.stack[-1][address]

        else: # la direccion esta almacenada en heap
            return self.heap[address]

    def setValue(self, address, value):

        if address >= 9000 and address < 13000: # la direccion es local entonces esta almacenada en stack
            self.stack[-1][address] = value

        else: # la direccion esta almacenada en heap
            self.heap[address] = value

        