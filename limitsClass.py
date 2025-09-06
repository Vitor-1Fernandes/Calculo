import sympy as sp
import matplotlib.pyplot as plt  # Usado para criar gráficos e visualizações
import numpy as np  # Numpy é uma biblioteca fundamental para operações matemáticas e manipulação de arrays

# Entrada da função
entradas = np.linspace(0.5 ,2 , 15)

#Saidas da função
saidas = []


for i in entradas:
    x = i
    y = ((x**2 - 1)/(x - 1))
    if x > 0.5 and x < 1.5:
        print(f'entrada {x}, saida {y}')
    saidas.append(y)

print(y)

# x = sp.symbols('x', real=True)
# print("Exemplo:", sp.limit((x**2 - 1)/(x - 1), x, 1))  # 2

def plotGraph(entradas, saidas):

    plt.figure(figsize=(10,6))
    plt.plot(entradas, saidas, "o-", label="valores de y")

    plt.title('Limites')
    plt.xlabel('Números de Entrada')
    plt.ylabel('Números de Saída')

    plt.legend()
    plt.grid(True)
    plt.show()

plotGraph(entradas, saidas)