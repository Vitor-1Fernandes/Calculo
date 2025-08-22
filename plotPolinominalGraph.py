import matplotlib.pyplot as plt  # Usado para criar gráficos e visualizações
import numpy as np  # Numpy é uma biblioteca fundamental para operações matemáticas e manipulação de arrays

# Entrada da função
entradas = np.array([2, 6 ,7 ,9, 14, 20, 18])

#Saidas da função
saidas = np.array([5 ,7 ,10 , 9, -4, 22, 20])

# polyfit é um objeto usada para descobrir a função polinominal que corresponde as entradas e saidas apresentadas. Estrutura: (valores de entrada, valores de saida, numero de polinômios)
coeficientes = np.polyfit(entradas, saidas, 6)

# o objeto poly1d tem a capacidade de aplicar uma função baseado nos coeficientes que vão dentro dos (). Logo, atribuir esse valor a uma variável a torna capaz de devolver o valor de y para qualquer valor de x
modelo = np.poly1d(coeficientes)

#O linspace utiliza o valor mais baixo e o mais alto entre as entradas para criar números igualmente espaçados, utilizaremos esses valores para criar a linha de tendência
x_fit = np.linspace(min(entradas), max(entradas), 400)
# Utiliza função com os coeficientes mais próximos obtidos para gerar um valor aproximado de y para cada valor de x. A exatidão da função é refletida pela proximidade da linha de tendência vermelha com os pontos azuis no gráfico
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
    plt.title('Altos e Baixos')
    # Legenda X
    plt.xlabel('Números de Entrada')
    # Legenda Y
    plt.ylabel('Números de Saída')
    # Ativa a legenda
    plt.legend()
    # Ativa o fundo grid
    plt.grid(True)
    # exibe o gráfico
    plt.show()

# Executa a função baseado nos valores recebidos
plotGraph(entradas, saidas)