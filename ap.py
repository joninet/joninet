import matplotlib.pyplot as plt

# Datos del Profesor B
datos_profesor_b = [10.5, 11.3, 11.9, 12, 12.3, 12.3, 12.5, 12.7, 13.4, 13.7, 13.8, 14.2, 14.8, 15.1, 15.3, 16.7, 16.8, 18.8, 20.8]

# Crear el boxplot
plt.boxplot(datos_profesor_b)
plt.title('Diagrama de caja de los tiempos de sueño - Profesor B')
plt.ylabel('Tiempo en minutos')
plt.xticks([1], ['Profesor B'])
plt.show()
