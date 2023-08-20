# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def ordenarDiccionario(diccionario_par, clave, descendente=True):
    '''
    Esta función recibe como parámetro un diccionario, cuyas listas de valores tienen el mismo
    tamaño y sus elementos enésimos están asociados. Y otros dos parámetros que indican
    la clave por la cual debe ordenarse y si es descendente o ascendente.
    La función debe devolver el diccionario ordenado, teniendo en cuenta de no perder la
    relación entre los elementos enésimos.
    Recibe tres argumentos:
        diccionario:    Diccionario a ordenar.
        clave:          Clave del diccionario recibido, por la cual ordenar.
        descendente:    Un valor booleano, que al ser verdadero indica ordenamiento ascendente y 
                        descendente si es falso. 
                        Debe tratarse de un parámetro por defecto en True.
    Si el parámetro diccionario no es un tipo de dato diccionario ó el parámetro clave no 
    se encuentra dentro de las claves del diccionario, debe devolver nulo.
    Ej:
        dicc = {'clave1':['c','a','b'],
                'clave2':['casa','auto','barco'],
                'clave3':[1,2,3]}
        OrdenarDiccionario(dicc, 'clave1')          debe retornar {'clave1':['a','b','c'],
                                                                'clave2':['auto','barco','casa'],
                                                                'clave3':[2,3,1]}
        OrdenarDiccionario(dicc, 'clave3', False)   debe retornar {'clave1':['b','a','c'],
                                                                'clave2':['barco','auto','casa'],
                                                                'clave3':[3,2,1]}
    '''
    #Tu código aca:
    dicc = ('clave1':['c','a','b'],'clave2':['casa','auto','barco'],'clave3':[1,2,3])
    lista_valores = dicc[clave]
    
   
    indices_ordenados = sorted(range(len(lista_valores)), key=lambda i: lista_valores[i], reverse=descendente)
    
   
    diccionario_ordenado = {}
    for key, values in dicc.items():
        diccionario_ordenado[key] = [values[i] for i in indices_ordenados]
    
    return diccionario_ordenado

print(ordenarDiccionario(dicc, 'clave1'))  
print(ordenarDiccionario(dicc, 'clave3', False))  






def listaEnteros(inicio, tamanio):
    '''
    Esta función devuelve una lista de números enteros
    Recibe dos argumentos:
        inicio: Numero entero donde inicia la lista
        tamanio: Cantidad de números enteros consecutivos
    Ej:
        ListaEnteros(10,5) debe retornar [10,11,12,13,14]
    '''
    #Tu código aca:
def ListaEnteros(inicio, tamaño):
    if not isinstance(inicio, int) or not isinstance(tamaño, int) or tamaño <= 0:
        return None
    enteros = [inicio + i for i in range(tamaño)]
    return enteros
print(ListaEnteros)

def dividirDosNumeros(dividendo, divisor):
    '''
    Esta función devuelve dos valores, la parte entera de la división y su resto
    Recibe dos argumentos:
        dividendo: El número que va a ser dividido
        divisor: El número que va a dividir
    Ej:
        DividirDosNumeros(10,3) debe retornar 3, 1
    '''
    #Tu código aca:
    return 'Funcion incompleta'
def divisionyresto(10,3):
    parte_entera = 10 // 3
    resto = 10 % 3
    return parte_entera, resto



def claseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    def  __init__(self, especie, color):
        self.Edad = 0
        self.Especie = especie
        self.Color = color
        
    def CumplirAnios(self):
        self.Edad += 1
        return self.Edad

def crear_animal(especie, color):
    return claseAnimal(especie, color)

a = crear_animal('perro', 'blanco')

print(a.CumplirAnios())  
print(a.CumplirAnios())  
print(a.CumplirAnios())  

def exponente(numero, exponente):
    '''
    Esta función devuelve el resultado de elevar el parámetro "numero" al parámetro "exponente"
    Recibe dos argumentos:
        numero: El número base en la operación exponencial
        exponente: El número exponente en la operación exponencial
    Ej:
        Exponente(10,3) debe retornar 1000
    '''
    #Tu código aca:
  def exponente(numero, exponente):
    return numero**exponente



def listaPrimos(desde, hasta):
    '''
    Esta función devuelve una lista con los números primos entre los valores "desde" y "hasta"
    pasados como argumento, siendo ambos inclusivos.
    En caso de que alguno de los parámetros no sea de tipo entero y/o no sea mayor a cero, debe retornar nulo.
    En caso de que el segundo parámetro sea mayor al primero, pero ambos mayores que cero,
    debe retornar una lista vacía.
    Recibe un argumento:
        desde: Será el número a partir del cual se toma el rango
        hasta: Será el número hasta el cual se tome el rango
    Ej:
        ListaPrimos(7,15) debe retornar [7,11,13]
        ListaPrimos(100,99) debe retornar []
        ListaPrimos(1,7) debe retonan [1,2,3,5,7]
    '''
    #Tu código aca:
    def ListaPrimos(desde, hasta):
        if not isinstance(desde, int) or not isinstance(hasta, int):
            return None
        
        if hasta < desde: 
            return []
        def es_primo(numero):
            if numero < 2:
                return False
            for i in range(2, int(numero**0.5)+ 1):
                if numero % i == 0:
                    return False
                return True
            primos = [num for num in range(desde, hasta + 1)if es_primo(num)]
            return primos
        
        print(ListaPrimos)

def listaRepetidos(lista):
    '''
    Esta función recibe como argumento una lista y devuelve una lista de tuplas donde cada 
    tupla contiene un valor de la lista original y las veces que se repite. Los valores 
    de la lista original no deben estar repetidos. 
    Debe respetarse el orden original en el que aparecen los elementos.
    En caso de que el parámetro no sea de tipo lista debe retornar nulo.
    Recibe un argumento:
        lista: Será la lista que se va a evaluar.
    Ej:
        ListaRepetidos([]) debe retornar []
        ListaRepetidos(['hola', 'mundo', 'hola', 13, 14]) 
            debe retornar [('hola',2),('mundo',1),(13,1),(14,1)]
        ListaRepetidos([1,2,2,4]) debe retornar [(1,1),(2,2),(4,1)]
    '''
    #Tu código aca:
    def listarepetidos(lista):
        if not isinstance(lista, list):
            return None
        
        resultados = []
        valores_unicos = set()

        for elemento in lista:
            if elemento not in valores_unicos:
                valores_unicos.add(elemento)
                repeticiones = lista.count(elemento)
                resultados.append((elemento, repeticiones))

                return resultados
            
            print(listarepetidos([]))


   
    
