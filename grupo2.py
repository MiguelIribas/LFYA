
""" GRUPO 2: IRIBAS, MORENO, RAINERO"""

""" EJERCICIO 1 - GRAMATICAS DE CHOMSKY """

ErrorG3 = []
ErrorG2 = []
ErrorG1 = []
MensajeG3=[("No pertenece a ninguna de las formas: NT -> t, NT -> NT t, NT-> t NT")]
MensajeG2=[("No pertenece a ninguna de las formas: NT -> Combinacion de T NT ")]
MensajeG1=[("No cumple la condicion de: Antecedente < Consecuente")]

diccionario={3:[],2:[],1:[],0:[]}

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
            global ErrorG3
            ErrorG3.append(y[0]+":"+y[1])
            global ErrorG2
            ErrorG2.append(y[0]+":"+y[1])
            return False
    return True                                         #Si el antecedente es un solo elemento y es NT.

def ConsecuenteG3(list): #True si es G3.
    derivaciones=list
    for y in derivaciones:
        consecuente= len(y[1])
        if consecuente >2:
            if y[1]!="lambda":                      #No se admiten mas de 2 elementos en el consecuente.
                #diccionario[3][0:0]=[y[0]+":"+y[1]] #Agregar al diccionario el error.
                global ErrorG3
                ErrorG3.append(y[0]+":"+y[1])
                return False 
        else:
            if consecuente==1:
                if y[1].isupper() is True:      #Si es NT.
                    ErrorG3.append(y[0]+":"+y[1])
                    return False
            else:
                if y[1].islower() is True:      #Si los dos son T.
                    ErrorG3.append(y[0]+":"+y[1])
                    return False
                else:
                    if y[1].isupper() is True:  #Si los dos son NT.
                        ErrorG3.append(y[0]+":"+y[1])
                        return False
    return True

def AntecedentesConsecuentesG1(list): #Cantidad simbolos izquierda < cantidad simbolos derecha (G1)
    derivaciones=list
    for y in derivaciones:
        antecedente=  len(y[0])
        consecuente= len(y[1])
        if antecedente > consecuente:
            ErrorG1.append(y[0]+":"+y[1])
            return False
    return True

def clasificar_gramatica(string):
    derivaciones = crear_derivaciones(string)
    """if AntecedenteG2G3(derivaciones) is True:
        if ConsecuenteG3(derivaciones) is True:
            #es g3
            print("G3")
            print(diccionario)
        else:
            #es g2
            print("G2")
            diccionario[3]=ErrorG3+MensajeG3
            print(diccionario)
    else:
        if AntecedentesConsecuentesG1(derivaciones) is True:
            #es g1
            print("G1")
            diccionario[3]=ErrorG3+MensajeG3
            diccionario[2]=ErrorG2+MensajeG2
            print(diccionario)
        else:
            #es g0
            print("G0")"""
    AntecedenteG2G3(derivaciones)
    ConsecuenteG3(derivaciones)
    AntecedentesConsecuentesG1(derivaciones)
    if ErrorG3!=[]:
        diccionario[3]=ErrorG3+MensajeG3
    if ErrorG2!=[]:
        diccionario[2]=ErrorG2+MensajeG2
    if ErrorG1!=[]:
        diccionario[1]=ErrorG1+MensajeG1
    print(diccionario)

#GRAMATICA ORIGINAL --> "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
#clasificar_gramatica("A:b A\nA:a\nA:A B c\nA:lambda\nB:b")

#G3 --> "S:aB\nS:c\nC:c A\nB:b c\nB:b\nA:a A\nA:a"
#clasificar_gramatica("S:aB\nS:c\nC:c A\nB:b C\nB:b\nA:a A\nA:a")

#G2 --> "S:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:Aa"
#clasificar_gramatica("S:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:Aa")

#G1 --> "S:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:lambda"
clasificar_gramatica("SA:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:lambda")


""" EJERCICIO 2 - AUTOMATA DE PILA """
class AutomataPila:
    """ Esta clase implementa un automáta de pila a partir de la definición de
    estados y transiciones que lo componen, pudiendo validar si una cadena dada
    puede ser reconocida por el mismo.
    """

    def __init__(self, estados, estados_aceptacion):
        """ Constructor de la clase.
        Args
        ----
        estados: dict
            Diccionario de estados que especifica en las claves los nombres de los
            estados y como valores una lista de transiciones salientes de dicho estado.
            Cada transición se compone de: (s,p,a,e) siendo
            s -> símbolo que se consume de la entrada para aplicar la transición.
            p -> símbolo que se consume del tope de la pila para aplicar la transición.
            a -> lista de símbolo/s que se apila una vez aplicada la transición.
            e -> estado de destino.

            Ejemplo:
            {'a': [('(', 'Z0', ['Z0'], 'a'), 
                   ('(', '(', ['(', '('], 'a'), 
                   (')', '(', [''], 'b')],
             'b': [(')', '(', [''], 'b'), 
                   ('$', 'Z0', ['Z0'], 'b')]}    
        
        estados_aceptacion: array-like
            Estados que admiten fin de cadena.

            Ejemplo: 
            ['b']
        """

        self.estados = estados
        self.estado_actual = None
        self.cadena_restante = ''

        a=validar_cadena(self,cadena)

    def validar_cadena(self, cadena):
        """ Se valida si una determinada cadena puede ser reconocida por el autómata.
        Args
        ----
        cadena: string
            Cadena de entrada a reconocer.
        Returns
        -------
        resultado: bool
            Indica si la cadena pudo se reconocida o no.
        """
        for x in cadena:
            x=true

estados={'a': [('(', 'Z0', ['Z0'], 'a'),('(', '(', ['(', '('], 'a'),(')', '(', [''], 'b')],'b': [(')', '(', [''], 'b'),('$', 'Z0', ['Z0'], 'b')]} 

ap = AutomataPila(estados,['b'])
ap.validar_cadena()