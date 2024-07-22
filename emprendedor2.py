# Actividad 2 - Rentabilidad 
# Actividad- Rentabilidad con usuarios diferenciados  
# No necesito formulas de libreria 
# Mensaje de advertencia  
print("Advertencia: Asegúrese de ingresar valores válidos.")  
print("todos los datos deben ser números positivos.")   

# Solicitar datos de entrada  
P_normal = float(input("Ingrese el precio de suscripción para usuarios normales (P): "))  
U_normal = int(input("Ingrese el número de usuarios normales (U): "))  
U_premium = int(input("Ingrese el número de usuarios premium (U): "))  
GT = float(input("Ingrese los gastos totales (GT): "))  

# Calcular precio para usuarios premium (50% mayor)  
P_premium = P_normal * 1.5  

# Calcular utilidades  
utilidades = (P_normal * U_normal) + (P_premium * U_premium) - GT  

# Resultado  
print(f"Las utilidades del proyecto con usuarios diferenciados son: {utilidades:.2f}")