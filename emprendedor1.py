# Actividad 2 - Rentabilidad  
# libreria no ocupo
# nota de advertencia  
print("Advertencia: Asegúrese de ingresar valores válidos.")  
print("todos los datos deben ser números positivos.") 
# Solicitar datos de entrada  
P = float(input("Ingrese el precio de suscripción (P): "))  
U = int(input("Ingrese el número de usuarios (U): "))  
GT = float(input("Ingrese los gastos totales (GT): "))  

# Calcular utilidades  
utilidades = (P * U - GT)

# Mostrar el resultado  
print(f"Las utilidades del proyecto son: {utilidades:.2f}")