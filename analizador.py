currentIndex = 0
currentChar = ''
fileText = open("fuente.txt", "r").read()
output_file = open("output_file.txt", "w")
def getChar():
    global currentChar
    global currentIndex
    if(currentIndex < len(fileText)-1):
        currentChar = fileText[currentIndex]
        currentIndex += 1
        return True
    else:
        currentChar = ''
        return False


def tmatch (spectedChar):
    if(not spectedChar == currentChar):
        print("error en la posicion:" + currentIndex + ",simbolo no esperado")
    getChar()

def stringrp():
    if (currentChar == '"'):
        tmatch('"')
        output_file.write('STRING ')
    else:
        getChar()
        stringrp()

def stringr():

    if (currentChar == '"'):
        tmatch('"')
        stringr()
    else:
        stringrp()

def list():
    if (currentChar == '['):
        tmatch('[')
        output_file.write('L_CORCHETE \n\t')
        attr()
    elif (currentChar == ','):
        attr()
    elif (currentChar == ']'):
        tmatch(']')
        output_file.write('L_CORCHETE\n\t')
        attr()

def truer():
    if (currentChar == 't'):
        trueString = currentChar
        for number in range(3):
            getChar()
            trueString += currentChar
        if (trueString.lower() == 'true'):
            output_file.write('PR_TRUE ')
            attr()

def falser():
    if (currentChar == 'f'):
        trueString = currentChar
        for number in range(4):
            getChar()
            trueString += currentChar
        if (trueString.lower() == 'false'):
            output_file.write('PR_FALSE ')
            attr()

def numberr():
    if (currentChar.isnumeric()):
        getChar()
        numberr()
    else:
        attr()

def attr():
    if (currentChar == '"'):
        stringr()
        attr()
    elif (currentChar == ':'):
        tmatch(':')
        output_file.write('DOS_PUNTOS ')
        attr()
    elif (currentChar == '{'):
        obj()
    elif (currentChar == '['):
        list()
    elif (currentChar == ']'):
        tmatch(']')
        output_file.write('R_CORCHETE \n')
        attr()
    elif (currentChar == 't'):
        truer()
    elif (currentChar == 'f'):
        falser()
    elif (currentChar.isnumeric()):
        output_file.write('NUMBER ')
        getChar()
        numberr()
    elif (currentChar == '}'):
        obj()
    elif (currentChar == ','):
        tmatch(',')
        output_file.write('COMA \n\t')
        attr()
    elif(getChar()):
        attr()


def obj():
    if (currentChar == '{'):
        tmatch('{')
        output_file.write('L_LLAVE \n\t')
    if (currentChar == '}'):
        tmatch('}')
        output_file.write('R_LLAVE\n')
    attr()



def json():
    getChar()
    obj()
    output_file.close()
    print("Proceso terminado... Archivo generado en el mismo directorio que este programa.")


def main():
    json()

if __name__ == '__main__':
    main()