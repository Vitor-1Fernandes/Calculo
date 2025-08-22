import matplotlib.pyplot as plt  # Usado para criar gráficos e visualizações
import numpy as np  # Numpy é uma biblioteca fundamental para operações matemáticas e manipulação de arrays

dadosiniciais = np.array([1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000])

migracao = np.array([30.4,
26.4,
23.6,
21.1,
19.0,
17.1,
15.0, 
13.0,
11.7,
10.5])

anosnovos = np.array([1988, 2002])

coeficientes = np.polyfit(anos,migracao, 6)
print(coeficientes)

modelo = np.poly1d(coeficientes)
migracaonova = modelo(anosnovos)

print(migracaonova)


x_fit = np.linspace(min(anos), max(anos), 400)
y_fit = modelo(x_fit)

plt.figure(figsize=(10, 6))
plt.plot(anosnovos, migracaonova, 'o', label='Dados Originais')
# plt.plot(x_fit, y_fit, 'r--', label=f'Modelo: {modelo}')
plt.title('Migracao por ano')
plt.xlabel('Ano')
plt.ylabel('Migracao')
plt.legend()
plt.grid(True)
plt.show()
