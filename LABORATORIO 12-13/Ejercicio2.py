""" Crea un sistema de gestión de pedidos que utilice una 
cola para procesar los pedidos en el orden en que 
fueron recibidos. Implementa funciones para agregar 
pedidos, procesar pedidos y mostrar el estado 
actual de la cola."""

class ColaPedidos:
    def __init__(self):
        self.pedidos = []

    def agregar_pedido(self, pedido):
        """
        Agrega un pedido a la cola.
        """
        self.pedidos.append(pedido)
        print(f"Pedido agregado a la cola: {pedido}")

    def procesar_pedido(self):
        """
        Procesa el pedido más antiguo en la cola.
        """
        if self.pedidos:
            pedido = self.pedidos.pop(0)
            print(f"Procesando pedido: {pedido}")
        else:
            print("No hay pedidos para procesar")

    def mostrar_estado(self):
        """
        Muestra el estado actual de la cola de pedidos.
        """
        if self.pedidos:
            print("Estado actual de la cola de pedidos:")
            for i, pedido in enumerate(self.pedidos, start=1):
                print(f"Pedido {i}: {pedido}")
        else:
            print("La cola de pedidos está vacía")


# Ejemplo de uso
cola_pedidos = ColaPedidos()
cola_pedidos.agregar_pedido("Pizza")
cola_pedidos.agregar_pedido("Hamburguesa")
cola_pedidos.mostrar_estado() #Tenemos dos Pedidos (Pizza y Hamburguesa)
cola_pedidos.procesar_pedido() #Atendemos la Pizza
cola_pedidos.mostrar_estado()   #Solo nos mostrara ya la Hamburguesa
cola_pedidos.procesar_pedido()  #Atendemos la Hamburguesa
cola_pedidos.mostrar_estado()   #Muestra vacia (sin pedidos)
