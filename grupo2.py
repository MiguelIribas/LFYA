
""" GRUPO 2: IRIBAS, MORENO, RAINERO"""

""" EJERCICIO 1 - GRAMATICAS DE CHOMSKY """

ErrorG3 = []
ErrorG2 = []
ErrorG1 = []
MensajeG3=[("No pertenece a ninguna de las formas: NT -> t, NT -> NT t, NT-> t NT")]
MensajeG2=[("No pertenece a ninguna de las formas: NT -> Combinacion de T NT ")]
MensajeG1=[("No cumple las condiciones de: Antecedente < Consecuente, el distinguido deriva en lambda y tiene recursion, un NT deriva en lambda y no es el distinguido")]

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
        if y[1]=="lambda":
            if y[0] != derivaciones[0][0]:
                ErrorG1.append(y[0]+":"+y[1])
                return False
            else:
                for z in derivaciones:
                    for j in z[1]:
                        if j == derivaciones[0][0]:
                            ErrorG1.append(y[0]+":"+y[1])
                            return False
    return True

def clasificar_gramatica(string):
    derivaciones = crear_derivaciones(string)
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
#clasificar_gramatica("SA:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:Aa")

#G1 CON LAMBDA--> "S:lambda\nS:a B\nB:cb"
#clasificar_gramatica("S:lambda\nS:a B\nB A:cb")

#G1 SIN LAMBDA--> "S:lambda\nS:a B\nB:cb"
#clasificar_gramatica("S:lambda\nS:a S\nS:Ab\nA B: c c")

#G0 --> "SAAAA:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:lambda"
#clasificar_gramatica("SAAAA:Cba\nS:C\nC:Bc\nB:Cb\nB:b\nA:Ba\nA:lambda")


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
            {'a': [('(', 'Z0', ['Z0','('], 'a'),
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
        self.estados_aceptacion = estados_aceptacion

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

        self.pila = []
        self.pila.append('Z0')    #Nueva pila con primer elemento Z0
        self.cadena_creada = []   #Cadena a comparar con la cadena de entrada

        for x in self.estados:
            self.estado_actual=x    #Establecer primer estado
            break

        for x in cadena:
            for y in list(self.estados[self.estado_actual]):  #Recorrer las transiciones del estado actual
                if x == '$': 
                    for z in list(self.estados_aceptacion):
                        if z == self.estado_actual: #Si la entrada es $ y el estado actual es de aceptacion
                            self.cadena_creada.append(x)
                            if self.cadena_creada==list(cadena) and self.pila==['Z0']:
                                return True
                            else:
                                return False
                else:
                    if x == y[0]:   #Si la entrada es igual al primer elemento de la transicion
                        if y[2] != ['']: #Si no se apila nada
                            if y[1] != '': 
                                if y[1]==self.pila[-1]: #Compara si el elemento es igual al ultimo de la pila
                                    self.cadena_creada.append(x)
                                    self.pila.pop()
                                    for z in y[2]:
                                        self.pila.append(z)
                                    break
                        else: #Si se apila algo
                            if y[1] != '':
                                if y[1]==self.pila[-1]: #Compara si el elemento es igual al ultimo de la pila
                                    self.cadena_creada.append(x)
                                    self.pila.pop()
                            else:
                                self.cadena_creada.append(x)
                        if y[3]!=self.estado_actual: #Cambio de estado
                            self.estado_actual=y[3]


"""
#EJEMPLO 1 -- Parentesis balanceados

estados={'a': [('(', 'Z0', ['Z0','('], 'a'),('(', '(', ['(', '('], 'a'),(')', '(', [''], 'b')],'b': [(')', '(', [''], 'b'),('$', 'Z0', ['Z0'], 'b')]} 
estados_aceptacion= ['b']

ap = AutomataPila(estados,estados_aceptacion)

print (ap.validar_cadena("(())$")) #T
print (ap.validar_cadena("((()))$")) #T
print (ap.validar_cadena("((((()))))$")) #T
print (ap.validar_cadena("((((((()))$")) #F
"""
"""
#EJEMPLO 2 -- Misma cantidad de A que de B

estados={'a': [('a', 'a', ['a','a'], 'a'),('a', 'Z0', ['Z0', 'a'], 'a'),('b', 'a', [''], 'b')],'b': [('b', 'a', [''], 'b'),('$', 'Z0', ['Z0'], 'b')]}
estados_aceptacion= ['b']

ap = AutomataPila(estados,estados_aceptacion)

print (ap.validar_cadena("ab$")) #T
print (ap.validar_cadena("aaabbb$")) #T
print (ap.validar_cadena("aabb$")) #T
print (ap.validar_cadena("aaaaaaaaaaaaaaabbbb$")) #F
print (ap.validar_cadena("abb$")) #F
"""
"""
#EJEMPLO 3 -- Mas cantidad de A que de B -- NO SE PUEDE RESOLVER POR AUTOMATA DE PILA

estados={'a': [('a', 'b', [''], 'b'),('b', 'Z0', ['Z0', 'b'], 'a'),('b', 'b', ['b','b'], 'a')],'b': [('a', 'b', [''], 'b'),('a', 'Z0', ['Z0'], 'c')],'c': [('a', 'Z0', ['Z0'], 'c'),('$', 'Z0', ['Z0'], 'c')]}

ap = AutomataPila(estados,estados_aceptacion)

print (ap.validar_cadena("aaab$"))
print (ap.validar_cadena("baaa$"))
"""
"""
# EJEMPLO 4 -- MISMA CANTIDAD DE A QUE DE C

estados={'a': [('a', 'Z0', ['Z0','a'], 'a'),('a', 'a', ['a', 'a'], 'a'),('b','', [''], 'b')],'b': [('b', '', [''], 'b'),('c', 'a', [''], 'c')],'c': [('c', 'a', [''], 'c'),('$', 'Z0', ['Z0'], 'c')]}
estados_aceptacion= ['c']

ap = AutomataPila(estados,estados_aceptacion)

print (ap.validar_cadena("aaabbccc$")) #T
print (ap.validar_cadena("abbbbbbbbbbbccccc$")) #F
print (ap.validar_cadena("aaabbc$")) #F
print (ap.validar_cadena("abc$")) #T
"""
"""
# EJEMPLO 5 -- C ES EL DOBLE DE A + 1, B SIEMPRE ES 1

estados={'a': [('a', 'Z0', ['Z0','a'], 'a'),('a', 'a', ['a','a'], 'a'),('b','', [''], 'b')],'b': [('c', '', [''], 'c')],'c': [('c', 'a', ['c'], 'c'),('c', 'c', [''], 'c'),('$', 'Z0', [''], 'c')]}
estados_aceptacion= ['c']

ap = AutomataPila(estados,estados_aceptacion)

print (ap.validar_cadena("bc$")) #T 
print (ap.validar_cadena("abc$"))  #F
print (ap.validar_cadena("abccc$")) #T
print (ap.validar_cadena("aaabccccccc$")) #T
"""
