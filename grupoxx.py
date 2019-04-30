
diccionario = {3:[],2:[],1:[],0:[]}

def DerivacionLambda(list): #Derivacion en lambda (G0 - G3)
    consecuentes = list
    listaconsecuentes =[]
    separadorconsecuentes = ":"
    for x in consecuentes:
        listaconsecuentes.append(x.split(separadorconsecuentes))
    for y in listaconsecuentes:
        if y[1] =="lambda":
            return True
    return False

#def NTIzquierda(list) #No terminal a la izquierda (G2 - G3)

#def CantSimbolos(list) #Cantidad simbolos izquierda < cantidad simbolos derecha (G0 - G1)

def clasificar_gramatica(string):
    derivaciones = crear_derivaciones(string)
    a = DerivacionLambda(derivaciones)
    print(a)

def crear_derivaciones(string):
    cadena = string
    cadena = cadena.replace(" ","") #Eliminar espacios
    separadorfilas = "\n"
    derivaciones = cadena.split(separadorfilas) #Separar la gramatica en una lista.
    return derivaciones

clasificar_gramatica("A:b A \nA:a\nA:A B c\nA:s\nB:b")