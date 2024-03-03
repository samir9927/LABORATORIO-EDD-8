"""Crear una calculadora que pueda realizar 
operaciones básicas (+, -, *, /) utilizando una pila para evaluar 
expresiones"""

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


def evaluar_expresion(expresion):
    pila = Pila()  # Creamos una pila para realizar la evaluación
    operadores = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

    # Dividimos la expresión en tokens
    tokens = expresion.split()

    for token in tokens:
        if token.isdigit():  # Si el token es un número, lo apilamos en la pila
            pila.apilar(float(token))
        elif token in operadores:  # Si el token es un operador, realizamos la operación correspondiente
            if len(pila.items) < 2:  # Verificamos que haya al menos dos operandos en la pila
                return "Expresión inválida: no hay suficientes operandos para el operador"
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            resultado = operadores[token](operando1, operando2)
            pila.apilar(resultado)
        else:
            return f"Token no reconocido: {token}"

    if len(pila.items) == 1:  # Verificamos que haya un único resultado en la pila
        return pila.desapilar()
    else:
        return "Expresión inválida: hay operandos sin operadores"


# Ejemplo de uso
expresion = "3 4 + 2 *"
resultado = evaluar_expresion(expresion)
print(f"Resultado de la expresión '{expresion}': {resultado}")
