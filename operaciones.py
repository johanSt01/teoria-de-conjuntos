# Operacione entre conjuntos

# ----------Función de intersección-----------

# Recibe cualquier cantidad de listas gracias al *(args)
def interseccion(*listas):
    # Si no se proporcionan listas, se devuelve una lista vacía
    if not listas:
        return []
    
    # Convertimos las listas en conjuntos y realizamos la intersección
    interseccion = set(listas[0])

    # Iteramos sobre las listas restantes
    for lista in listas[1:]:
        nueva_interseccion = set()  # Conjunto temporal para almacenar la intersección
        for elemento in interseccion:
            if elemento in lista:
                nueva_interseccion.add(elemento)
        interseccion = nueva_interseccion  # Actualizamos la intersección
    
    # Convertimos el resultado de nuevo a lista para obtener los valores únicos
    return list(interseccion)

# Ingresar el numero de conjuntos
num_conjuntos = int(input("Ingresa el número de conjuntos (mínimo 2 y máximo 4): "))

# Validar que el número de conjuntos esté en el rango permitido
while num_conjuntos < 2 or num_conjuntos > 4:
    print("El número de conjuntos debe ser entre 2 y 4.")
    num_conjuntos = int(input("Ingresa el número de conjuntos (mínimo 2 y máximo 4): "))


# Almacenar las listas ingresadas
listas = []

# Ingresar las listas por consola
for i in range(num_conjuntos):
    entrada = input(f"Ingresa la lista de números {i+1} separados por comas: ")
    lista = [int(numero) for numero in entrada.split(",")]
    listas.append(lista)

# Llamada a la función con las listas
valoresUnicos = interseccion(*listas)

# Imprimimos la lista resultante ordenada de valores únicos
print(f"La intersección de los conjuntos es: {sorted(valoresUnicos)}")
