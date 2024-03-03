"""Implementa un sistema de gestión de tareas que 
permita agregar tareas, marcar tareas como 
completadas y mostrar la próxima tarea pendiente"""

class SistemaGestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        """
        Agrega una nueva tarea a la lista de tareas.
        """
        self.tareas.append({"descripcion": tarea, "completada": False})
        print(f"Tarea agregada: {tarea}")

    def marcar_completada(self, indice):
        """
        Marca una tarea como completada basándose en su índice en la lista.
        """
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True
            print(f"Tarea '{self.tareas[indice]['descripcion']}' marcada como completada")
        else:
            print("Índice de tarea fuera de rango")

    def mostrar_proxima_pendiente(self):
        """
        Muestra la próxima tarea pendiente en la lista.
        """
        for tarea in self.tareas:
            if not tarea["completada"]:
                print(f"Próxima tarea pendiente: {tarea['descripcion']}")
                return
        print("No hay tareas pendientes")

# Ejemplo de uso
sistema_tareas = SistemaGestionTareas()
sistema_tareas.agregar_tarea("Hacer la compra")
sistema_tareas.agregar_tarea("Preparar informe")
sistema_tareas.agregar_tarea("Llamar al cliente")
sistema_tareas.mostrar_proxima_pendiente()
sistema_tareas.marcar_completada(0)
sistema_tareas.mostrar_proxima_pendiente()
