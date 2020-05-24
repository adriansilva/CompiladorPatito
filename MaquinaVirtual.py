
class MaquinaVirtual:

    memoria = None

    def __init__(self):
        self.memoria = {}


    def processInput(self, cuadruplos):
        ip = 0

        while cuadruplos[ip][0] != 'END':

            #GOTO
            input(cuadruplos[ip])

            if cuadruplos[ip][0] == 'GOTO':
                ip = cuadruplos[ip][3]
                continue

            if cuadruplos[ip][0] == 'GOTOF':

                if self.memoria[cuadruplos[ip][1]] == False:
                    ip = cuadruplos[ip][3]
                    continue

            if cuadruplos[ip][0] == 'GOTOV':

                if self.memoria[cuadruplos[ip][1]] == True:
                    ip = cuadruplos[ip][3]
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
                self.memoria[cuadruplos[ip][3]] = input("input")

            # INCREMENTA INSTRUCTION POINTER   
            ip += 1
