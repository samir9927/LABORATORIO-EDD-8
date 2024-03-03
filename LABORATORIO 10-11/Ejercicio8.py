"""Crear un programa que evalúe una expresión matemática 
en notación posfija utilizando una pila."""

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


def evaluar_expresion_posfija(expresion):
    pila = Pila()  # Creamos una pila para realizar las operaciones

    for caracter in expresion.split():  # Dividimos la expresión en elementos separados
        if caracter.isdigit():  # Si el caracter es un dígito, lo apilamos en la pila
            pila.apilar(int(caracter))
        else:
            # Si el caracter es un operador, desapilamos los dos últimos operandos
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            # Realizamos la operación correspondiente y apilamos el resultado
            if caracter == '+':
                pila.apilar(operando1 + operando2)
            elif caracter == '-':
                pila.apilar(operando1 - operando2)
            elif caracter == '*':
                pila.apilar(operando1 * operando2)
            elif caracter == '/':
                pila.apilar(operando1 / operando2)

    # Al final, el resultado de la expresión estará en el tope de la pila
    return pila.desapilar()


# Ejemplo de uso
expresion_posfija = "3 4 + 2 *"
resultado = evaluar_expresion_posfija(expresion_posfija)
print("El resultado de la expresión posfija es:", resultado)
