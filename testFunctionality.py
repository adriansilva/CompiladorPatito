if cuadruplos[ip][0] == 'PRINT':
    #print(cuadruplos[ip][1]," print.")
    outputTemp = self.getValue(cuadruplos[ip][1]))
    if isinstance(outputTemp,str):
        outputLista = outputTemp.split("\n")
        for out in outputLista:
            print(out)
    else:
        print(outputTemp)
