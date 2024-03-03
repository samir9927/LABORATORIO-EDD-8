"""Verificar si los operadores en una expresión
 matemática están correctamente anidados utilizando una 
pila."""

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


def operadores_anidados(expresion):
    pila = Pila()  # Creamos una pila para realizar el seguimiento de los operadores

    for caracter in expresion:
        if caracter in '([{':  # Si encontramos un operador de apertura, lo apilamos
            pila.apilar(caracter)
        elif caracter in ')]}':  # Si encontramos un operador de cierre, verificamos su pareja correspondiente
            if pila.esta_vacia():  # Si la pila está vacía, significa que hay un error de anidación
                return False
            # Verificamos si el operador de cierre coincide con su pareja de apertura
            operador_anterior = pila.desapilar()
            if (caracter == ')' and operador_anterior != '(') or \
               (caracter == ']' and operador_anterior != '[') or \
               (caracter == '}' and operador_anterior != '{'):
                return False

    # Si la pila está vacía al final, significa que los operadores están correctamente anidados
    return pila.esta_vacia()


# Ejemplo de uso
expresion = "((3 + 4) * 2)"
if operadores_anidados(expresion):
    print("Los operadores en la expresión están correctamente anidados.")
else:
    print("Los operadores en la expresión NO están correctamente anidados.")
