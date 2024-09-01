from Operaciones.operaciones import union, interseccion, diferencia, simetrica, subconjunto, subconjunto2, subconjunto3, superconjunto2, superconjunto, superconjunto3

# Ingresar los conjuntos
def ingresar_conjuntos():
    # Almacenar las listas ingresadas
    conjuntos = []
    for i in range(3):
        entrada = input(f"Ingresa la lista de números {i+1} separados por comas: ")
        conjunto = [int(numero) for numero in entrada.split(",")]
        conjuntos.append(conjunto)
    return conjuntos

def entradaUniversal(universal):
    entrada = input("Ingrese los elementos para el conjunto universal separados por comas: ")
    conjunto = list(map(int, entrada.split(',')))
    return conjunto

# Ingresar los conjuntos
conjuntos = ingresar_conjuntos()
# Ingresar el conjunto universal
universal = entradaUniversal("Conjunto universal")

# Separa la lista de conjuntos
conjuntoA, conjuntoB, conjuntoC = conjuntos

# Definir funciones para cada operación
def mostrar_union():
    resultado = union(conjuntoA, conjuntoB, conjuntoC)
    print("Resultado de la Unión:", resultado)

def mostrar_interseccion():
    resultado = interseccion(conjuntoA, conjuntoB, conjuntoC)
    print("Resultado de la Intersección:", resultado)

def mostrar_diferencia():
    resultado = diferencia(conjuntoA, conjuntoB, conjuntoC)
    print("Resultado de la Diferencia:", resultado)

def mostrar_diferencia_simetrica():
    resultado = simetrica(conjuntoA, conjuntoB, conjuntoC)
    print("Resultado de la Diferencia Simétrica:", resultado)

def mostrar_subconjuntoA():
    resultado = subconjunto(conjuntoA)
    print("Subconjuntos de A:", resultado)

def mostrar_subconjuntoB():
    resultado = subconjunto2(conjuntoB)
    print("Subconjuntos de B:", resultado)

def mostrar_subconjuntoC():
    resultado = subconjunto3(conjuntoC)
    print("Subconjuntos de C:", resultado)

def mostrar_superconjuntoA():
    resultado = superconjunto(conjuntoA, universal)
    print("Superconjuntos de A:", resultado)

def mostrar_superconjuntoB():
    resultado = superconjunto2(conjuntoB, universal)
    print("Superconjuntos de B:", resultado)

def mostrar_superconjuntoC():
    resultado = superconjunto3(conjuntoC, universal)
    print("Superconjuntos de C:", resultado)

def salir():
    print('Saliendo...')

# Opciones de menu
opciones = {
    '1': ('Union', mostrar_union),
    '2': ('Interseccion', mostrar_interseccion),
    '3': ('Diferencia', mostrar_diferencia),
    '4': ('Diferencia simetrica', mostrar_diferencia_simetrica),
    '5': ('Subconjuntos de A', mostrar_subconjuntoA),
    '6': ('Subconjuntos de B', mostrar_subconjuntoB),
    '7': ('Subconjuntos de C', mostrar_subconjuntoC),
    '8': ('Superconjuntos de A', mostrar_superconjuntoA),
    '9': ('Superconjuntos de B', mostrar_superconjuntoB),
    '10': ('Superconjuntos de C', mostrar_superconjuntoC),
    '11': ('Salir', salir)
}

#LLAMADO
while True:
    print("\nOpciones:")
    for key in opciones:
        print(f"{key}. {opciones[key][0]}")
    
    seleccion = input("Selecciona una opción: ")

    if seleccion in opciones:
        opciones[seleccion][1]()  # Llamar a la función correspondiente
        if seleccion == '11':
            break
    else:
        print("Opción no válida, intenta de nuevo.")