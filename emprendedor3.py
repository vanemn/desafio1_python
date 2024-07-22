# Actividad 2 - Rentabilidad con comparación de utilidades  

# nota de advertencia  
print("Advertencia: Asegúrese de ingresar valores válidos.")  
print("todos los datos deben ser números positivos.") 
# Solicitar datos de entrada uso int para  personas por entero
P = float(input("Ingrese el precio de suscripción P: "))  
U = int(input("Ingrese el número de usuarios normales U: "))  
GT = float(input("Ingrese los gastos totales GT: "))  
U_anterior = float(input("Ingrese las utilidades del año anterior Uanterior: "))  

# Calcular utilidades actuales  
U_actuales = P * U - GT  
# Calcular la razón entre las utilidades actuales y las del año anterior PODRIA SER  valor_si_verdadero if condicion else valor_si_falso . El signo ! en != es un operador de comparación que significa "no igual", float('inf') representa infinito positivo. ESTA SERIA LA FUNCION razon = U_actuales / U_anterior if U_anterior != 0 else float('inf')   
razon = U_actuales / U_anterior 
# Resultados  
print(f"Las utilidades actuales son: {U_actuales:.2f}")  
print(f"La razón entre las utilidades actuales y las del año anterior es: {razon:.1f}")