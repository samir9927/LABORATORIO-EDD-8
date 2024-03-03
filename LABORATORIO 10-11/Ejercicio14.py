"""Implementar un sistema simple de "deshacer" utilizando 
dos pilas, una para las acciones y otra para los 
deshaceres"""

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()


class SistemaDeshacer:
    def __init__(self):
        self.acciones = Pila()     # Pila para almacenar las acciones realizadas
        self.deshaceres = Pila()   # Pila para almacenar las acciones deshechas

    def registrar_accion(self, accion):
        """
        Registra una nueva acción en la pila de acciones.

        Parameters:
            accion (str): La acción a registrar.
        """
        self.acciones.apilar(accion)  # Registrar una nueva acción
        print(f"Acción registrada: {accion}")

    def deshacer_accion(self):
        """
        Deshace la última acción realizada.
        """
        if self.acciones.esta_vacia():
            print("No hay acciones para deshacer")
            return
        accion = self.acciones.desapilar()  # Obtener la última acción realizada
        self.deshaceres.apilar(accion)      # Almacenar la acción en la pila de deshaceres
        print(f"Deshaciendo acción: {accion}")

    def rehacer_accion(self):
        """
        Rehace la última acción deshecha.
        """
        if self.deshaceres.esta_vacia():
            print("No hay acciones para rehacer")
            return
        accion = self.deshaceres.desapilar()  # Obtener la última acción deshecha
        self.acciones.apilar(accion)          # Almacenar la acción en la pila de acciones
        print(f"Rehaciendo acción: {accion}")


# Ejemplo de uso
sistema_deshacer = SistemaDeshacer()
sistema_deshacer.registrar_accion("Añadir elemento A")
sistema_deshacer.registrar_accion("Añadir elemento B")
sistema_deshacer.registrar_accion("Quitar elemento B")
sistema_deshacer.deshacer_accion()  # Deshacer la última acción
sistema_deshacer.rehacer_accion()  # Rehacer la última acción deshecha
