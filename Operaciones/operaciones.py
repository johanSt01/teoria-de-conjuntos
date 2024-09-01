import itertools

# DEFINICIONES DE LAS FUNCIONES

def union(conjuntoA, conjuntoB, conjuntoC):
    union = conjuntoA[:]
    union.extend([element for element in conjuntoB if element not in union])
    union.extend([element for element in conjuntoC if element not in union])
    union.sort()
    # print('La unión de los tres conjuntos es ', union)

    return union

def interseccion(conjuntoA, conjuntoB, conjuntoC):
    # Convertimos los conjuntos en un conjunto de intersección inicial
    interseccion = conjuntoA

    # Realizamos la intersección con los otros dos conjuntos
    for conjunto in [conjuntoB, conjuntoC]:
        nueva_interseccion = set()  # Conjunto temporal para almacenar la intersección
        for elemento in interseccion:
            if elemento in conjunto:
                nueva_interseccion.add(elemento)
        interseccion = nueva_interseccion  # Actualizamos la intersección
    
    # Convertimos el resultado a un conjunto para mantener los valores únicos
    return interseccion

def diferencia(conjuntoA, conjuntoB, conjuntoC):
    # Convertimos los conjuntos en un conjunto de diferencia inicial
    diferencia = conjuntoA

    # Realizamos la diferencia con los otros dos conjuntos
    for conjunto in [conjuntoB, conjuntoC]:
        nueva_diferencia = set()  # Conjunto temporal para almacenar la diferencia
        for elemento in diferencia:
            if elemento not in conjunto:
                nueva_diferencia.add(elemento)
        diferencia = nueva_diferencia  # Actualizamos la diferencia
    
    return diferencia

def simetrica(conjuntoA, conjuntoB, conjuntoC):
    soloA = [element for element in conjuntoA if element not in conjuntoB and element not in conjuntoC]
    soloB = [element for element in conjuntoB if element not in conjuntoA and element not in conjuntoC]
    soloC = [element for element in conjuntoC if element not in conjuntoA and element not in conjuntoB]
    simetrica = soloA + soloB + soloC
    simetrica.sort()
    #print('La diferencia simetrica entre los tres conjuntos es ', simetrica4)

    return simetrica

def subconjunto(conjuntoA):
    subconjuntos = []
    for r in range(len(conjuntoA) + 1):
        subconjuntos.extend(itertools.combinations(conjuntoA, r))
    subconjuntos = [list(subconjunto) for subconjunto in subconjuntos]
    #print('Subconjuntos de A son ', subconjuntos)

    return subconjuntos

def subconjunto2(conjuntoB):
    subconjuntos = []
    for r in range(len(conjuntoB) + 1):
        subconjuntos.extend(itertools.combinations(conjuntoB, r))
    subconjuntos = [list(subconjunto) for subconjunto in subconjuntos]
    #print('Subconjuntos de B son ', subconjuntos)

    return subconjuntos

def subconjunto3(conjuntoC):
    subconjuntos = []
    for r in range(len(conjuntoC) + 1):
        subconjuntos.extend(itertools.combinations(conjuntoC, r))
    subconjuntos = [list(subconjunto) for subconjunto in subconjuntos]
    #print('Subconjuntos de C son ', subconjuntos)

    return subconjuntos

def superconjunto(conjuntoA, universal):
    superconjuntos = []
    
    # Encontrar todos los subconjuntos del universo
    for r in range(len(conjuntoA), len(universal) + 1):
        for subset in itertools.combinations(universal, r):
            if set(conjuntoA).issubset(set(subset)):
                superconjuntos.append(list(subset))
                
    #print('Superconjuntos de A son ', superconjuntos)
    return superconjuntos

def superconjunto2(conjuntoB, universal):
    superconjuntos = []
    
    # Encontrar todos los subconjuntos del universo
    for r in range(len(conjuntoB), len(universal) + 1):
        for subset in itertools.combinations(universal, r):
            if set(conjuntoB).issubset(set(subset)):
                superconjuntos.append(list(subset))
                
    #print('Superconjuntos de B son ', superconjuntos)
    return superconjuntos

def superconjunto3(conjuntoC, universal):
    superconjuntos = []
    
    # Encontrar todos los subconjuntos del universo
    for r in range(len(conjuntoC), len(universal) + 1):
        for subset in itertools.combinations(universal, r):
            if set(conjuntoC).issubset(set(subset)):
                superconjuntos.append(list(subset))
                
    #print('Superconjuntos de C son ', superconjuntos)
    return superconjuntos