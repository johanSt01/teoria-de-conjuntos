import matplotlib.pyplot as plt
from matplotlib_venn import venn3

def graficar(conjuntoA, conjuntoB, conjuntoC, titulo):
    # Crear un diagrama de Venn de 3 conjuntos
    plt.figure(figsize=(8, 8))
    venn = venn3([set(conjuntoA), set(conjuntoB), set(conjuntoC)], ('Conjunto A', 'Conjunto B', 'Conjunto C'))

    # Asignar etiquetas personalizadas con el contenido de los conjuntos
    venn.get_label_by_id('100').set_text('\n'.join(map(str, set(conjuntoA) - set(conjuntoB) - set(conjuntoC))))
    venn.get_label_by_id('010').set_text('\n'.join(map(str, set(conjuntoB) - set(conjuntoA) - set(conjuntoC))))
    venn.get_label_by_id('001').set_text('\n'.join(map(str, set(conjuntoC) - set(conjuntoA) - set(conjuntoB))))
    venn.get_label_by_id('110').set_text('\n'.join(map(str, set(conjuntoA) & set(conjuntoB) - set(conjuntoC))))
    venn.get_label_by_id('101').set_text('\n'.join(map(str, set(conjuntoA) & set(conjuntoC) - set(conjuntoB))))
    venn.get_label_by_id('011').set_text('\n'.join(map(str, set(conjuntoB) & set(conjuntoC) - set(conjuntoA))))
    venn.get_label_by_id('111').set_text('\n'.join(map(str, set(conjuntoA) & set(conjuntoB) & set(conjuntoC))))

    plt.title(titulo)
    plt.show()

