import numpy as np

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

            #print(cuadruplos[ip])

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

            # OPERADORES PRIMITIVOS ---------------------------------

            # SUMA ============================

            if cuadruplos[ip][0] == '+':
                if cuadruplos[ip][3] >= 24000: # si se esta asignando a un pointer, entonces el 3 elemento del cuadurplo no va a ser un address, si no una constante
                    valor = self.getValue(cuadruplos[ip][1]) + cuadruplos[ip][2]
                    self.setPointer(cuadruplos[ip][3], valor)
                else:
                    valor = self.getValue(cuadruplos[ip][1]) + self.getValue(cuadruplos[ip][2])
                    self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == '+10': #suma arreglo con valor unico
                arrSize = cuadruplos[ip][1][1][0]

                arrAddress = cuadruplos[ip][1][0]
                if arrAddress >= 24000:
                    arrAddress = self.getAddressFromPointer(cuadruplos[ip][1][0])

                uniqueVal = self.getValue(cuadruplos[ip][2][0])

                for i in range(arrSize):
                    result = self.getValue(arrAddress + i) + uniqueVal
                    self.setValue(cuadruplos[ip][3] + i, result)

            if cuadruplos[ip][0] == '+11': #suma arreglo con arreglo
                arrSize = cuadruplos[ip][1][1][0]

                arr1Address = cuadruplos[ip][1][0]
                if arr1Address >= 24000:
                    arr1Address = self.getAddressFromPointer(cuadruplos[ip][1][0])

                arr2Address = cuadruplos[ip][2][0]
                if arr2Address >= 24000:
                    arr2Address = self.getAddressFromPointer(cuadruplos[ip][2][0])

                for i in range(arrSize):
                    result = self.getValue(arr1Address + i) + self.getValue(arr2Address + i)
                    self.setValue(cuadruplos[ip][3] + i, result)



            if cuadruplos[ip][0] == '+20': #suma matriz con valor unico
                matSize = cuadruplos[ip][1][1][0] * cuadruplos[ip][1][1][1]
                matAddress = cuadruplos[ip][1][0]

                uniqueVal = self.getValue(cuadruplos[ip][2][0])

                for i in range(matSize):
                    result = self.getValue(matAddress + i) + uniqueVal
                    self.setValue(cuadruplos[ip][3] + i, result)


            if cuadruplos[ip][0] == '+21': #suma matriz con arreglo
                matSize = cuadruplos[ip][1][1][0] * cuadruplos[ip][1][1][1]
                arrSize = cuadruplos[ip][2][1][0]

                matAddress = cuadruplos[ip][1][0]

                arrAddress = cuadruplos[ip][2][0]
                if arrAddress >= 24000:
                    arrAddress = self.getAddressFromPointer(cuadruplos[ip][2][0])

                for i in range(matSize):
                    result = self.getValue(matAddress + i) + self.getValue(arrAddress + i%arrSize)
                    self.setValue(cuadruplos[ip][3] + i, result)


            if cuadruplos[ip][0] == '+22': #suma matriz con matriz
                matSize = cuadruplos[ip][1][1][0] * cuadruplos[ip][1][1][1]

                mat1Address = cuadruplos[ip][1][0]
                mat2Address = cuadruplos[ip][2][0]

                for i in range(matSize):
                    result = self.getValue(mat1Address + i) + self.getValue(mat2Address + i)
                    self.setValue(cuadruplos[ip][3] + i, result)


            # RESTA ============================

            if cuadruplos[ip][0] == '-':
                valor = self.getValue(cuadruplos[ip][1]) - self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == '-10': #resta arreglo con valor unico
                arrSize = cuadruplos[ip][1][1][0]

                arrAddress = cuadruplos[ip][1][0]
                if arrAddress >= 24000:
                    arrAddress = self.getAddressFromPointer(cuadruplos[ip][1][0])

                uniqueVal = self.getValue(cuadruplos[ip][2][0])

                for i in range(arrSize):
                    result = self.getValue(arrAddress + i) - uniqueVal
                    self.setValue(cuadruplos[ip][3] + i, result)


            if cuadruplos[ip][0] == '-11': #resta arreglo con arreglo
                arrSize = cuadruplos[ip][1][1][0]

                arr1Address = cuadruplos[ip][1][0]
                if arr1Address >= 24000:
                    arr1Address = self.getAddressFromPointer(cuadruplos[ip][1][0])

                arr2Address = cuadruplos[ip][2][0]
                if arr2Address >= 24000:
                    arr2Address = self.getAddressFromPointer(cuadruplos[ip][2][0])

                for i in range(arrSize):
                    result = self.getValue(arr1Address + i) - self.getValue(arr2Address + i)
                    self.setValue(cuadruplos[ip][3] + i, result)



            if cuadruplos[ip][0] == '-20': #resta matriz con valor unico
                matSize = cuadruplos[ip][1][1][0] * cuadruplos[ip][1][1][1]

                matAddress = cuadruplos[ip][1][0]

                uniqueVal = self.getValue(cuadruplos[ip][2][0])

                for i in range(matSize):
                    result = self.getValue(matAddress + i) - uniqueVal
                    self.setValue(cuadruplos[ip][3] + i, result)


            if cuadruplos[ip][0] == '-21': #resta matriz con arreglo
                matSize = cuadruplos[ip][1][1][0] * cuadruplos[ip][1][1][1]
                arrSize = cuadruplos[ip][2][1][0]

                matAddress = cuadruplos[ip][1][0]

                arrAddress = cuadruplos[ip][2][0]
                if arrAddress >= 24000:
                    arrAddress = self.getAddressFromPointer(cuadruplos[ip][2][0])


                for i in range(matSize):
                    result = self.getValue(matAddress + i) - self.getValue(arrAddress + i%arrSize)
                    self.setValue(cuadruplos[ip][3] + i, result)


            if cuadruplos[ip][0] == '-22': #resta matriz con matriz
                matSize = cuadruplos[ip][1][1][0] * cuadruplos[ip][1][1][1]

                mat1Address = cuadruplos[ip][1][0]
                mat2Address = cuadruplos[ip][2][0]

                for i in range(matSize):
                    result = self.getValue(mat1Address + i) - self.getValue(mat2Address + i)
                    self.setValue(cuadruplos[ip][3] + i, result)


            # MULTIPLICACION ============================

            if cuadruplos[ip][0] == '*':
                valor = self.getValue(cuadruplos[ip][1]) * self.getValue(cuadruplos[ip][2])
                self.setValue(cuadruplos[ip][3], valor)

            if cuadruplos[ip][0] == '*22':
                mat1Address = cuadruplos[ip][1][0]
                mat1rows = cuadruplos[ip][1][1][0]
                mat1cols = cuadruplos[ip][1][1][1]

                mat2Address = cuadruplos[ip][2][0]
                mat2rows = cuadruplos[ip][2][1][0]
                mat2cols = cuadruplos[ip][2][1][1]

                mat1 = []
                for i in range(mat1rows):
                    mat1.append([])
                    for j in range(mat1cols):
                        mat1[-1].append(self.getValue(mat1Address + i*mat1cols + j))

                mat2 = []
                for i in range(mat2rows):
                    mat2.append([])
                    for j in range(mat2cols):
                        mat2[-1].append(self.getValue(mat2Address + i*mat2cols + j))

                mat3 = []
                mat3rows = mat1rows
                mat3cols = mat2cols
                mat3Address = cuadruplos[ip][3]

                for i in range(mat3rows):
                    mat3.append([])
                    for j in range(mat3cols):
                        mat3[-1].append(0)

                for i in range(mat1rows):
                    for j in range(mat2cols):
                        for k in range(mat2rows):
                            mat3[i][j] += mat1[i][k] * mat2[k][j]

                for i in range(mat3rows):
                    for j in range(mat3cols):
                        self.setValue(mat3Address + i*mat3cols + j, mat3[i][j])

            if cuadruplos[ip][0] == '*21':
                print("mat x arr no esta implementado todavia")
                exit(-1)

            if cuadruplos[ip][0] == '*20':
                mat1Address = cuadruplos[ip][1][0]
                mat1rows = cuadruplos[ip][1][1][0]
                mat1cols = cuadruplos[ip][1][1][1]

                vUnico = self.getValue(cuadruplos[ip][2][0])

                mat1 = []
                for i in range(mat1rows):
                    mat1.append([])
                    for j in range(mat1cols):
                        mat1[-1].append(self.getValue(mat1Address + i*mat1cols + j) * vUnico)

                destAddress = cuadruplos[ip][3]
                for i in range(mat1rows):
                    for j in range(mat1cols):
                        self.setValue(destAddress + i*mat1cols + j, mat1[i][j])

            if cuadruplos[ip][0] == '*11':
                print("arr x arr no esta implementado todavia")
                exit(-1)

            if cuadruplos[ip][0] == '*10':
                print("arr x vUnico no esta implementado todavia")
                exit(-1)


            # DIVISION ============================

            if cuadruplos[ip][0] == '/':
                address = cuadruplos[ip][3]
                if address >= 24000:
                    address = self.heap[cuadruplos[ip[3]]]
                if ((address >= 5000 and address<6000) or
                   (address >= 9000 and address<10000) or
                   (address >= 13000 and address<14000) or
                   (address >= 16000 and address<18000)):
                    valor = self.getValue(cuadruplos[ip][1]) // self.getValue(cuadruplos[ip][2])
                    self.setValue(cuadruplos[ip][3], valor)
                else:
                    valor = self.getValue(cuadruplos[ip][1]) / self.getValue(cuadruplos[ip][2])
                    self.setValue(cuadruplos[ip][3], valor)

            # ASIGNACION ---------------------------------

            if cuadruplos[ip][0] == '=': #asigna valor unico a valor unico

                if cuadruplos[ip][3]  >= 13000 and cuadruplos[ip][3] < 16000: # SI estamos agregando una constante
                    constante = cuadruplos[ip][1]
                    self.setValue(cuadruplos[ip][3], constante)

                else:
                    valor = self.getValue(cuadruplos[ip][1])
                    self.setValue(cuadruplos[ip][3], valor)


            if cuadruplos[ip][0] == '=11': #asigna arreglo con arreglo

                arrAddress = cuadruplos[ip][1]
                arrDestAddress = cuadruplos[ip][3]
                sz = cuadruplos[ip][2][0][0]

                if arrAddress >= 24000:
                    arrAddress = self.getAddressFromPointer(arrAddress)
                if arrDestAddress >= 24000:
                    arrDestAddress = self.getAddressFromPointer(arrDestAddress)

                for i in range(sz):
                    valor = self.getValue(arrAddress + i)
                    self.setValue(arrDestAddress + i, valor)

            if cuadruplos[ip][0] == '=22': #asigna matriz con matriz
                matAddress = cuadruplos[ip][1]
                matDestAddress = cuadruplos[ip][3]
                sz = cuadruplos[ip][2][0][0] * cuadruplos[ip][2][0][1]

                for i in range(sz):
                    valor = self.getValue(matAddress + i)
                    self.setValue(matDestAddress + i, valor)


            if cuadruplos[ip][0] == '=21': # quiere asignar un arreglo a una matriz
                print('asignar un arreglo a una matriz no esta implementado')
                exit(-1)

            if cuadruplos[ip][0] == '=20': # quiere asignar un valor unico a una matriz
                matAddress = cuadruplos[ip][3]
                matrows = cuadruplos[ip][2][1][0]
                matcols = cuadruplos[ip][2][1][1]
                vUnico = self.getValue(cuadruplos[ip][1])

                for i in range(matrows):
                    for j in range(matcols):
                        self.setValue(matAddress + i*matcols + j, vUnico)

            if cuadruplos[ip][0] == '=10': # quiere asignar un valor unico a un arreglo
                arrAddress = cuadruplos[ip][3]
                arrSize = cuadruplos[ip][2][1][0]
                vUnico = self.getValue(cuadruplos[ip][1])

                for i in range(arrSize):
                    self.setValue(arrAddress + i, vUnico)




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
                output = self.getValue(cuadruplos[ip][1])
                if isinstance(output, str):
                    outputList = output.split("\\n")
                    for out in outputList:
                        print(out)
                else:
                    if cuadruplos[ip][2][1] == 1:
                        matcols = cuadruplos[ip][2][0]
                        matrows = 1
                    else:
                        matrows = cuadruplos[ip][2][0]
                        matcols = cuadruplos[ip][2][1]

                    if matrows+matcols > 2:
                        for j in range(matcols):
                            print('{:4}'.format(j),end=" ")
                        print()
                        for i in range(matrows):
                            print(i,end=" ")
                            for j in range(matcols):
                                print('{:4}'.format(self.getValue(cuadruplos[ip][1] + i*matcols + j)),end=" ")
                            print()
                    else:
                        print(output)


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
                self.isParam = True
                tam = cuadruplos[ip][2][0]*cuadruplos[ip][2][1]

                for i in range(tam):
                    valor = self.getValue(cuadruplos[ip][1]+i)
                    self.setValue(cuadruplos[ip][3]+i, valor)

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
                if self.getValue(cuadruplos[ip][1]) < 0 or self.getValue(cuadruplos[ip][1]) >= cuadruplos[ip][3]:
                    print("RUNTIME ERROR: el indice de acceso excede el tamano de la variable")
                    exit(-1)

            if cuadruplos[ip][0] == '?': #inversa
                matAddress = cuadruplos[ip][1]
                matrows = cuadruplos[ip][2][0][0]
                matcols = cuadruplos[ip][2][0][1]
                mat = []
                for i in range(matrows):
                    mat.append([])
                    for j in range(matcols):
                        mat[-1].append(self.getValue(matAddress + i*matcols + j))

                matInv = np.linalg.inv(mat)

                for i in range(matrows):
                    for j in range(matcols):
                        self.setValue(cuadruplos[ip][3] + i*matcols + j, matInv[i][j])


            if cuadruplos[ip][0] == '$': #determinante

                matAddress = cuadruplos[ip][1]
                matrows = cuadruplos[ip][2][0][0]
                matcols = cuadruplos[ip][2][0][1]
                mat = []
                for i in range(matrows):
                    mat.append([])
                    for j in range(matcols):
                        mat[-1].append(self.getValue(matAddress + i*matcols + j))


                det = np.linalg.det(mat)

                self.setValue(cuadruplos[ip][3], det)

            if cuadruplos[ip][0] == '¡': #transpuesta
                matAddress = cuadruplos[ip][1]
                matrows = cuadruplos[ip][2][0][0]
                matcols = cuadruplos[ip][2][0][1]
                mat = []

                for i in range(matrows):
                    mat.append([])
                    for j in range(matcols):
                        mat[-1].append(self.getValue(matAddress + i*matcols + j))

                matRes = np.transpose(mat)

                for i in range(matcols):
                    for j in range(matrows):
                        self.setValue(cuadruplos[ip][3] + i*matrows + j, matRes[i][j])


            # INCREMENTA INSTRUCTION POINTER
            ip += 1

    def getValue(self, address):
        if isinstance(address,str):
            return address
        else:
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

    def getAddressFromPointer(self, pointer):
        return self.heap[pointer]
