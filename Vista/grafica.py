from matplotlib_venn import venn3
import matplotlib.pyplot as plt

def graficar(conjuntoA, conjuntoB, conjuntoC, titulo):
    # Crear un diagrama de Venn de 3 conjuntos
    plt.figure(figsize=(8, 8))
    venn = venn3([set(conjuntoA), set(conjuntoB), set(conjuntoC)], ('Conjunto A', 'Conjunto B', 'Conjunto C'))
    plt.title(titulo)
    plt.show()
