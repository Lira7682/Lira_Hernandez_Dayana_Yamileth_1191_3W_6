print (" ") #espacio a agregar
print ("Lira Hernandez Dayana Yamileth:")
print ("determina si el valor ingresado es o no divisible entre 7 y mayor a 40")
print (" ") #espacio a agregar

n = int(input("Ingresa un número entero: "))#Solicita al que ingrese un número entero

# Verificar si el número es mayor a 40 y divisible por 7
if n > 40 and n % 7 == 0:
    print(f"El número {n} es mayor a 40 y es divisible por 7.")#imprime si es verdadero
else: #verifica si el valor es falso 
    print(f"El número {n} no cumple con las condiciones.")#imprime si es falso

print (" ") #espacio a agregar