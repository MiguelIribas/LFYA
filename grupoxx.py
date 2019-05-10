
#diccionario = {3:[,"no es g3"],2:[,],1:[,],0:[,]}

ErrorG3 = ""
ErrorG2 = ""
ErrorG1 = ""

def crear_derivaciones(string):
    cadena = string
    cadena = cadena.replace(" ","") #Eliminar espacios
    separadorfilas = "\n"
    cadena = cadena.split(separadorfilas) #Separar la gramatica en una lista.
    derivaciones =[]
    separadorderivaciones = ":"
    for x in cadena:
        derivaciones.append(x.split(separadorderivaciones))
    return derivaciones

def DerivacionLambda(list): #Derivacion en lambda (G0 - G3)
    derivaciones = list
    for y in derivaciones:
        if y[1] =="lambda":
            return True
    return False

def TIzquierda(list): #Terminal a la izquierda (G1 - G0)
    derivaciones=list
    for y in derivaciones:
        terminal=  y[0].islower()
        if terminal is True:
            return True
    return False
         
def AntecedentesConsecuentesG1(list): #Cantidad simbolos izquierda < cantidad simbolos derecha (G1)
    derivaciones=list
    for y in derivaciones:
        antecedente=  len(y[0])
        consecuente= len(y[1])
        if antecedente < consecuente:
            return True
    return False

def AntecedenteG2(list):
    derivaciones=list
    for y in derivaciones:
        antecedente=  len(y[0])
        if antecedente >2:
            return False
    return True

def AntecedenteG3(list): #Para G3 solo debe haber un antecedente. True si existe un solo antecedente.
    derivaciones=list
    for y in derivaciones:
        antecedente=  len(y[0])
        if antecedente!=1:
            return False
    return True

def ConsecuenteG3(list): #Cantidad simbolos consecuente <= 2 (G3). True si es G3.
    derivaciones=list
    for y in derivaciones:
        consecuente= len(y[1])
        if consecuente >2:   #No se admiten mas de 2 elementos en el consecuente.
            return False
        else:
            if consecuente==1:
                if y[1].isupper() is True: #Si es terminal.
                    return False
            else:
                if y[1].islower() is True: #Si los dos son terminales.
                    return False
                else:
                    if y[1].isupper() is True: #Si los dos son no terminales.
                        return False
    return True

def AveriguarG3(list):
    derivaciones = list
    Terminalizquierda=TIzquierda(derivaciones)   #TRUE si existe un terminal a la izquierda. Debe ser FALSE.
    #CantidadSimbolosIzq = CantSimbolos(derivaciones) #TRUE si el antecedente es < al consecuente. Debe ser TRUE.
    Antecedente = AntecedenteG3(derivaciones) # TRUE si el antecedente=1. Debe ser TRUE
    Consecuente = ConsecuenteG3(derivaciones) #TRUE si permite los consecuentes de G3. Debe ser TRUE.
    if Terminalizquierda is False and Antecedente is True and Consecuente is True:
        return True
    else:
        return False

def AveriguarG2(list):
    derivaciones=list
    Antecedente = AntecedenteG2(derivaciones)
    if Antecedente==True:
        return True
    else:
        return False

def AveriguarG1(list):
    derivaciones=list
    AntecedenteConsecuente = AntecedentesConsecuentesG1(derivaciones)
    derivacionlambda=DerivacionLambda(derivaciones)
    if derivacionlambda==False and AntecedenteConsecuente==True:
        return True
    else:
        return False

def clasificar_gramatica(string):
    derivaciones = crear_derivaciones(string)
    
    G3 = AveriguarG3(derivaciones)

    G2 = AveriguarG2(derivaciones)

    G1 = AveriguarG1(derivaciones)

    if G3 == True:
        print("G3")
    if G2 == True:
        print("G2")
    if G1 == True:
        print("G1")
    if G3==False and G2==False and G1==False:
        print("G0")

#GRAMATICA ORIGINAL --> "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
#clasificar_gramatica("A:b A\nA:a\nA:A B c\nA:lambda\nB:b")

#G3 --> "S:aB\nS:c\nC:c A\nB:b c\nB:b\nA:a A\nA:a"
#clasificar_gramatica("S:aB\nS:c\nC:c A\nB:b C\nB:b\nA:a A\nA:a")

#G2 --> "S:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:Aa"
#clasificar_gramatica("S:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:Aa")

#G1 --> "S:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:lambda"
#clasificar_gramatica("S:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:lambda")