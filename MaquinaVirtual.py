
class MaquinaVirtual:

    memoria = None

    def __init__(self):
        self.memoria = {}

    def processInput(self, cuadruplos, mt):
        ip = 0

        print("INICIA MAQUINA VIRTUAL")

        while cuadruplos[ip][0] != 'END':

            #GOTO

            if cuadruplos[ip][0] == 'GOTO':
                ip = cuadruplos[ip][3] - 1
                continue

            if cuadruplos[ip][0] == 'GOTOF':

                if self.memoria[cuadruplos[ip][1]] == False:
                    ip = cuadruplos[ip][3] - 1
                    continue

            if cuadruplos[ip][0] == 'GOTOV':

                if self.memoria[cuadruplos[ip][1]] == True:
                    ip = cuadruplos[ip][3] - 1
                    continue

            # operadores primitivos ---------------------------------

            if cuadruplos[ip][0] == '+':
                self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]] + self.memoria[cuadruplos[ip][2]]

            if cuadruplos[ip][0] == '-':
                self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]] - self.memoria[cuadruplos[ip][2]]

            if cuadruplos[ip][0] == '*':
                self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]] * self.memoria[cuadruplos[ip][2]]

            if cuadruplos[ip][0] == '/':
                self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]] / self.memoria[cuadruplos[ip][2]]

            # ASIGNACION ---------------------------------

            if cuadruplos[ip][0] == '=':
                if cuadruplos[ip][3]  >= 13000 and cuadruplos[ip][3] < 16000: # SI estamos agregando una constante
                    self.memoria[cuadruplos[ip][3]] = cuadruplos[ip][1]
                else:
                    self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]]

            # RELOP ---------------------------------

            if cuadruplos[ip][0] == '<':
                self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]] < self.memoria[cuadruplos[ip][2]]

            if cuadruplos[ip][0] == '<=':
                self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]] <= self.memoria[cuadruplos[ip][2]]

            if cuadruplos[ip][0] == '>':
                self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]] > self.memoria[cuadruplos[ip][2]]

            if cuadruplos[ip][0] == '>=':
                self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]] >= self.memoria[cuadruplos[ip][2]]

            if cuadruplos[ip][0] == '==':
                self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]] == self.memoria[cuadruplos[ip][2]]

            if cuadruplos[ip][0] == '<>':
                self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]] != self.memoria[cuadruplos[ip][2]]

            # LOGIC ---------------------------------
            if cuadruplos[ip][0] == '&&':
                self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]] and self.memoria[cuadruplos[ip][2]]

            if cuadruplos[ip][0] == '||':
                self.memoria[cuadruplos[ip][3]] = self.memoria[cuadruplos[ip][1]] or self.memoria[cuadruplos[ip][2]]

            # PRINT ---------------------------------

            if cuadruplos[ip][0] == 'PRINT':
                print(self.memoria[cuadruplos[ip][1]])

            # READ ---------------------------------

            if cuadruplos[ip][0] == 'READ':
                temp = input("input: ")
                try:
                    val = int(temp)
                    if ((cuadruplos[ip][3] >= 5000 and cuadruplos[ip][3] <6000) or
                        (cuadruplos[ip][3] >= 9000 and cuadruplos[ip][3] <10000) or
                        (cuadruplos[ip][3] >= 13000 and cuadruplos[ip][3] <14000) or
                        (cuadruplos[ip][3] >= 16000 and cuadruplos[ip][3] <18000)):
                        self.memoria[cuadruplos[ip][3]] = temp
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
                            self.memoria[cuadruplos[ip][3]] = temp
                        else:
                            print("ERROR DE ASIGNACION: El tipo de dato introducido (FLOAT) no matchea con la variable.")
                            exit(-1)
                    except ValueError:
                        if ((cuadruplos[ip][3] >= 7000 and cuadruplos[ip][3] <8000) or
                            (cuadruplos[ip][3] >= 11000 and cuadruplos[ip][3] <12000) or
                            (cuadruplos[ip][3] >= 15000 and cuadruplos[ip][3] <16000) or
                            (cuadruplos[ip][3] >= 20000 and cuadruplos[ip][3] <22000)):
                            self.memoria[cuadruplos[ip][3]] = temp
                        else:
                            print("ERROR DE ASIGNACION: El tipo de dato introducido (CHAR/STRING) no matchea con la variable.")
                            exit(-1)


            # INCREMENTA INSTRUCTION POINTER
            ip += 1
