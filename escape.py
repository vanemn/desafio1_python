# Actividad 1 - escape  
from math import sqrt  
# nota de advertencia  
print("Advertencia: Asegúrese de ingresar valores válidos.")  
print("El radio del planeta y la gravedad deben ser números positivos.")  

# Se solicita crear un script escape.py que permita calcular la velocidad de escape
# ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
# deben ingresarse de manera interactiva utilizando a función input().El programa debe especificar claramente el formato en el que se deben entregar los
# datos de entrada con instrucciones apropiadas
# lo multiplico por 1000 para pasar km a metros 

r = float(input("Ingrese el radio del planeta (en kilometros): ")) * 1000
g = float(input("Ingrese la gravedad en la superficie del planeta (en m/s^2): "))  

# Calcular la velocidad de escape uso sqrt es para raiz o (2 * g * r) ** 0.5   
velocidad_escape = sqrt(2 * g * r)  

# Resultado :.1f me indica la cantidad de decimales .2f serían 2 decimales  
print(f"La velocidad de escape es: {velocidad_escape:.1f} m/s")