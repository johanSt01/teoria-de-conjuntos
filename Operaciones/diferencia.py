# Operacione entre conjuntos

# ----------Función de diferencia----------- 

# Recibe cualquier cantidad de listas gracias al *(args)
def diferencia(*listas):
    # Si no se proporcionan listas, se devuelve una lista vacía
    if not listas:
        return []
    
    # Convertimos las listas en conjuntos y realizamos la diferencia
    diferencia = set(listas[0])

    # Iteramos sobre las listas restantes
    for lista in listas[1:]:
        nueva_diferencia = set()  # Conjunto temporal para almacenar la diferencia
        for elemento in diferencia:
            if elemento not in lista:
                nueva_diferencia.add(elemento)
        diferencia = nueva_diferencia  # Actualizamos la diferencia
    
    return diferencia

# Ingresar el numero de conjuntos
num_conjuntos = int(input("Ingresa el número de conjuntos (mínimo 3): "))

# Validar que el número de conjuntos esté en el rango permitido
while num_conjuntos < 3:
    print("El número de conjuntos debe ser entre 3 o más.")
    num_conjuntos = int(input("Ingresa el número de conjuntos (mínimo 3): "))

# Almacenar las listas ingresadas
listas = []

# Ingresar las listas por consola
for i in range(num_conjuntos):
    entrada = input(f"Ingresa la lista de números {i+1} separados por comas: ")
    lista = [int(numero) for numero in entrada.split(",")]
    listas.append(lista)

# Llamada a la función con las listas
valores_respuesta = diferencia(*listas)

# Imprimimos la lista resultante ordenada de valores únicos
print(f"La diferencia de los conjuntos es: {sorted(valores_respuesta)}")
