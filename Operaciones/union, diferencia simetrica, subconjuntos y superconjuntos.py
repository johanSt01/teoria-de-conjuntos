import itertools

#ENTRADA AL USUARIO

def entrada(conjuntoA):
    entrada = input("Ingrese los elementos para el conjunto A separados por comas: ")
    conjunto = list(map(int, entrada.split(',')))
    return conjunto

def entrada2(conjuntoB):
    entrada2 = input("Ingrese los elementos para el conjunto B separados por comas: ")
    conjunto = list(map(int, entrada2.split(',')))
    return conjunto

def entrada3(conjuntoC):
    entrada3 = input("Ingrese los elementos para el conjunto C separados por comas: ")
    conjunto = list(map(int, entrada3.split(',')))
    return conjunto

def entrada4(universal):
    entrada4 = input("Ingrese los elementos para el conjunto universal separados por comas: ")
    conjunto = list(map(int, entrada4.split(',')))
    return conjunto



#DECLARACION DE CONJUNTOS

conjuntoA = entrada("Conjunto A")
conjuntoB = entrada2("Conjunto B")
conjuntoC = entrada3("Conjunto C")
universal = entrada4("Conjunto universal")

#DEFINICIONES DE LAS FUNCIONES

def superconjunto():
    superconjuntos = []
    
    # Encontrar todos los subconjuntos del universo
    for r in range(len(conjuntoA), len(universal) + 1):
        for subset in itertools.combinations(universal, r):
            if set(conjuntoA).issubset(set(subset)):
                superconjuntos.append(list(subset))
                
    print('Superconjuntos de A son ', superconjuntos)
    return superconjuntos

def superconjunto2():
    superconjuntos = []
    
    # Encontrar todos los subconjuntos del universo
    for r in range(len(conjuntoB), len(universal) + 1):
        for subset in itertools.combinations(universal, r):
            if set(conjuntoB).issubset(set(subset)):
                superconjuntos.append(list(subset))
                
    print('Superconjuntos de B son ', superconjuntos)
    return superconjuntos

def superconjunto():
    superconjuntos = []
    
    # Encontrar todos los subconjuntos del universo
    for r in range(len(conjuntoC), len(universal) + 1):
        for subset in itertools.combinations(universal, r):
            if set(conjuntoC).issubset(set(subset)):
                superconjuntos.append(list(subset))
                
    print('Superconjuntos de C son ', superconjuntos)
    return superconjuntos

def subconjunto():
    subconjuntos = []
    for r in range(len(conjuntoA) + 1):
        subconjuntos.extend(itertools.combinations(conjuntoA, r))
    subconjuntos = [list(subconjunto) for subconjunto in subconjuntos]
    print('Subconjuntos de A son ', subconjuntos)

def subconjunto2():
    subconjuntos = []
    for r in range(len(conjuntoB) + 1):
        subconjuntos.extend(itertools.combinations(conjuntoB, r))
    subconjuntos = [list(subconjunto) for subconjunto in subconjuntos]
    print('Subconjuntos de B son ', subconjuntos)

def subconjunto3():
    subconjuntos = []
    for r in range(len(conjuntoC) + 1):
        subconjuntos.extend(itertools.combinations(conjuntoC, r))
    subconjuntos = [list(subconjunto) for subconjunto in subconjuntos]
    print('Subconjuntos de C son ', subconjuntos)


def simetrica():
    soloA = [element for element in conjuntoA if element not in conjuntoB]
    soloB = [element for element in conjuntoB if element not in conjuntoA]
    simetrica = soloA + soloB
    simetrica.sort()
    print('La diferencia simetrica entre A y B es ', simetrica)

def simetrica2():
    soloA = [element for element in conjuntoA if element not in conjuntoC]
    soloC = [element for element in conjuntoC if element not in conjuntoA]
    simetrica2 = soloA + soloC
    simetrica2.sort()
    print('La diferencia simetrica entre A y C es ', simetrica2)

def simetrica3():
    soloB = [element for element in conjuntoB if element not in conjuntoC]
    soloC = [element for element in conjuntoC if element not in conjuntoB]
    simetrica3 = soloB + soloC
    simetrica3.sort()
    print('La diferencia simetrica entre B y C es ', simetrica3)

def simetrica4():
    soloA = [element for element in conjuntoA if element not in conjuntoB and element not in conjuntoC]
    soloB = [element for element in conjuntoB if element not in conjuntoA and element not in conjuntoC]
    soloC = [element for element in conjuntoC if element not in conjuntoA and element not in conjuntoB]
    simetrica4 = soloA + soloB + soloC
    simetrica4.sort()
    print('La diferencia simetrica entre los tres conjuntos es ', simetrica4)

def union1():
    union = conjuntoA[:]
    union.extend([element for element in conjuntoB if element not in union])
    union.sort()
    print('La unión entre Conjunto A y B es ', union)

def union2():
    union = conjuntoA[:]
    union.extend([element for element in conjuntoC if element not in union])
    union.sort()
    print('La unión entre Conjunto A y C es ', union)

def union3():
    union = conjuntoB[:]
    union.extend([element for element in conjuntoC if element not in union])
    union.sort()
    print('La unión entre Conjunto B y C es ', union)

def union4():
    union = conjuntoA[:]
    union.extend([element for element in conjuntoB if element not in union])
    union.extend([element for element in conjuntoC if element not in union])
    union.sort()
    print('La unión de los tres conjuntos es ', union)

def salir():
    print('Saliendo...')

# Opciones
opciones = {
    '1': ('La union entre Conjunto A y B ', union1),
    '2': ('La diferencia simetrica entre Conjunto A y B ', simetrica),
    '3': ('La union entre Conjunto A y C ', union2),
    '4': ('La diferencia simetrica entre Conjunto A y C ', simetrica2),
    '5': ('La union entre Conjunto B y C ', union3),
    '6': ('La diferencia simetrica entre Conjunto B y C ', simetrica3),
    '7': ('La union de los tres conjuntos ', union4),
    '8': ('La diferencia simetrica de los tres conjuntos ', simetrica4),
    '9': ('Subconjuntos de A ', subconjunto),
    '10': ('Subconjuntos de B ', subconjunto2),
    '11': ('Subconjuntos de C ', subconjunto3),
    '12': ('Superconjuntos de A ', superconjunto),
    '13': ('Superconjuntos de A ', superconjunto),
    '14': ('Superconjuntos de A ', superconjunto),
    '15': ('Salir', salir)
}

#LLAMADO
while True:
    print("\nOpciones:")
    for key in opciones:
        print(f"{key}. {opciones[key][0]}")
    
    seleccion = input("Selecciona una opción: ")

    if seleccion in opciones:
        if seleccion == '15':
            opciones[seleccion][1]()  # Llamar a la función 'salir'
            break
        else:
            opciones[seleccion][1]()  # Llamar a la función correspondiente
    else:
        print("Opción no válida, intenta de nuevo.")