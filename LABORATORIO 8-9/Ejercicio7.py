"""Asegurar que una función retorna un valor específico"""

def obtener_entero_positivo():
    while True:
        valor = int(input("Por favor, ingresa un entero positivo: "))
        if valor > 0:
            return valor  # Si el valor es positivo, retornar el valor y salir del ciclo
        else:
            print("El valor ingresado no es un entero positivo. Inténtalo de nuevo.")

# Llamar a la función y asegurarse de que retorne un valor positivo
entero_positivo = obtener_entero_positivo()
print("El entero positivo ingresado es:", entero_positivo)
