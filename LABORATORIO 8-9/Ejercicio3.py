""" Validar el rango de una calificación."""

def validar_calificacion():
    while True:
        try:
            calificacion = float(input("Por favor, ingresa tu calificación: "))  # Solicitar al usuario que ingrese la calificación
            if 0 <= calificacion <= 10:  # Verificar si la calificación está dentro del rango de 0 a 10
                return calificacion  # Devolver la calificación si está dentro del rango
            else:
                print("La calificación debe estar dentro del rango de 0 a 10. Inténtalo de nuevo.")  # Mensaje de error si la calificación está fuera del rango
        except ValueError:
            print("Por favor, ingresa un número válido.")  # Mensaje de error si el usuario no ingresa un número válido

# Llamada a la función para validar la calificación del usuario
calificacion_usuario = validar_calificacion()
print("Calificación válida ingresada:", calificacion_usuario)
