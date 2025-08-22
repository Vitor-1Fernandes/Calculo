import matplotlib.pyplot as plt  # Usado para criar gráficos e visualizações
import numpy as np  # Numpy é uma biblioteca fundamental para operações matemáticas e manipulação de arrays

# Entrada da função
entradas = np.array([1, 2, 3, 4, 5, 6])

#Saidas da função
saidas = np.array([1, 4, 6, 8, 10, 12])

# polyfit é um objeto usada para descobrir a função polinominal que corresponde as entradas e saidas apresentadas. Estrutura: (valores de entrada, valores de saida, numero de polinômios)
coeficientes = np.polyfit(entradas, saidas, 2)

# o objeto poly1d tem a capacidade de aplicar baseado nos coeficientes que vão dentro dos (). Logo, atribuir essa função a uma variável a torna capaz de devolver o valor de y para qualquer x
modelo = np.poly1d(coeficientes)

#O linspace utiliza o valor mais baixo e o mais alto entre as entradas para criar números igualmente espaçados, utilizaremos esses valores para criar a linha de tendência
x_fit = np.linspace(min(entradas), max(entradas), 400)
y_fit = modelo(x_fit)

# Função para criar o gráfico
def plotGraph (entradas_x, saidas_y): 

    # Define o tamanho da figura
    plt.figure(figsize=(10, 6))
    
    # plt.plot coloca os pontos no gráfico (valores de x, valores de y, "tipo de marcação", label="legenda")
    plt.plot(entradas_x, saidas_y, 'o', label='Dados Originais')

    # Utilizaremos o plt.plot novamente, dessa vez usando a marcação "r--" para criar uma linha de tendência
    plt.plot(x_fit, y_fit, 'r--', label=f'Modelo: {modelo}')
    # Titulo do gráfico
    plt.title('Migracao por ano')
    # Legenda X
    plt.xlabel('Ano')
    # Legenda Y
    plt.ylabel('Migracao')
    # Ativa a legenda
    plt.legend()
    # Ativa o fundo grid
    plt.grid(True)
    # exibe o gráfico
    plt.show()

# Executa a função baseado nos valores recebidos
plotGraph(entradas, saidas)