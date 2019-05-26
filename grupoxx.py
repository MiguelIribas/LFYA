
#diccionario= {3: [(" A:A B c ", "no pertenece a ninguna de las formas NT -> t, NT -> NT t, NT-> t NT"]),
#2: [],
#1: [],
#0: [] }

ErrorG3 = ""
ErrorG2 = ""
ErrorG1 = ""

def crear_derivaciones(string):
    cadena = string
    cadena = cadena.replace(" ","")          #Eliminar espacios.
    separadorfilas = "\n"
    cadena = cadena.split(separadorfilas)    #Separar la gramatica en una lista.
    derivaciones = []
    separadorderivaciones = ":"
    for x in cadena:
        derivaciones.append(x.split(separadorderivaciones))
    return derivaciones

def AntecedenteG2G3(list): #G2 y G3. True si existe un solo antecedente NT.
    derivaciones=list
    for y in derivaciones:
        cantidadantecedente= len(y[0])
        antecedente= y[0]
        if cantidadantecedente!=1 or antecedente.islower():   #Si el antecedente tiene mas de un elemento o es un T.
            return False
    return True                                         #Si el antecedente es un solo elemento y es NT.

def ConsecuenteG3(list): #True si es G3.
    derivaciones=list
    for y in derivaciones:
        consecuente= len(y[1])
        if consecuente >2:                      #No se admiten mas de 2 elementos en el consecuente.
            return False
        else:
            if consecuente==1:
                if y[1].isupper() is True:      #Si es NT.
                    return False
            else:
                if y[1].islower() is True:      #Si los dos son T.
                    return False
                else:
                    if y[1].isupper() is True:  #Si los dos son NT.
                        return False
                #agregar caso lambda
    return True

def AntecedentesConsecuentesG1(list): #Cantidad simbolos izquierda < cantidad simbolos derecha (G1)
    derivaciones=list
    for y in derivaciones:
        antecedente=  len(y[0])
        consecuente= len(y[1])
        if antecedente > consecuente:
            return False
    return True

def clasificar_gramatica(string):
    derivaciones = crear_derivaciones(string)
    if AntecedenteG2G3(derivaciones) is True:
        if ConsecuenteG3(derivaciones) is True:
            #es g3
            print("G3")
        else:
            #es g2
            print("G2")
    else:
        if AntecedentesConsecuentesG1(derivaciones) is True:
            #es g1
            print("G1")
        else:
            #es g0
            print("G0")

    

#GRAMATICA ORIGINAL --> "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
#clasificar_gramatica("A:b A\nA:a\nA:A B c\nA:lambda\nB:b")

#G3 --> "S:aB\nS:c\nC:c A\nB:b c\nB:b\nA:a A\nA:a"
#clasificar_gramatica("S:aB\nS:c\nC:c A\nB:b C\nB:b\nA:a A\nA:a")

#G2 --> "S:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:Aa"
#clasificar_gramatica("S:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:Aa")

#G1 --> "S:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:lambda"
#clasificar_gramatica("SA:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:lambda")