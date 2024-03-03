""" Validar la edad de un usuario."""

def validar_edad():
    while True:  # Bucle para solicitar la edad hasta que sea válida
        try:
            edad = int(input("Por favor, ingresa tu edad: "))  # Solicitar al usuario que ingrese su edad como un número entero
            if edad >= 0:  # Comprobar si la edad ingresada es un número positivo
                return edad  # Devolver la edad si es válida
            else:
                print("La edad no puede ser un número negativo. Inténtalo de nuevo.")  # Mensaje de error si la edad es negativa
        except ValueError:  # Capturar una excepción si el usuario ingresa algo que no es un número entero
            print("Por favor, ingresa un número válido.")  # Mensaje de error si el usuario no ingresa un número entero válido

# Llamada a la función para validar la edad del usuario
edad_usuario = validar_edad()
print("Edad válida ingresada:", edad_usuario)