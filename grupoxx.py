
#diccionario = {3:[,"no es g3"],2:[,],1:[,],0:[,]}

ErrorG3 = ""
ErrorG2 = ""
ErrorG1 = ""

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
         
def CantSimbolos(list): #Cantidad simbolos izquierda < cantidad simbolos derecha (G0 - G1)
    derivaciones=list
    for y in derivaciones:
        antecedente=  len(y[0])
        consecuente= len(y[1])
        if antecedente < consecuente:
            return True
    return False

def CantSimbolosConsecuente(list): #Cantidad simbolos consecuente <= 2 (G3)
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
    CantidadSimbolosIzq = CantSimbolos(derivaciones) #TRUE si el antecedente es < al consecuente. Debe ser TRUE.
    CantidadSimbolosCons = CantSimbolosConsecuente(derivaciones) #TRUE si es G3.
    if Terminalizquierda is False and CantidadSimbolosIzq is True and CantidadSimbolosCons is True:
        return True
    else:
        return False

def clasificar_gramatica(string):
    derivaciones = crear_derivaciones(string)
    
    G3 = AveriguarG3(derivaciones)



  #Lambda = DerivacionLambda(derivaciones)          #TRUE si existe una derivacion en lambda.
  #  IF G3 =True
  #      G3
  #  ELSE:
  #      IF G2=TRUE:
  #          G2:

    return derivaciones

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

clasificar_gramatica("A:b A\nA:a\nA:A B c\nA:lambda\nB:b")

#GRAMATICA ORIGINAL --> "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"