""" Asegurar que un ciclo while se ejecuta al menos una vez."""

def ciclo_al_menos_una_vez():
    seguir = True  # Establecer una bandera para controlar el ciclo
    while seguir:
        # Aquí va el código que quieres ejecutar al menos una vez
        print("Este código se ejecutará al menos una vez.")

        # Preguntar al usuario si quiere continuar
        respuesta = input("¿Quieres continuar? (s/n): ")
        if respuesta.lower() != 's':
            seguir = False  # Si la respuesta no es 's', establecer la bandera en False para salir del ciclo

# Llamar a la función para ejecutar el ciclo al menos una vez
ciclo_al_menos_una_vez()
