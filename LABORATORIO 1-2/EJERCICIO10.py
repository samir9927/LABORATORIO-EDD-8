"""Genera los primeros 10 números de la serie Fibonacci."""

def fibonacci(n):
    secuencia_fibonacci = [0, 1]
    for i in range(2, n):
        siguiente_numero = secuencia_fibonacci[-1] + secuencia_fibonacci[-2]
        secuencia_fibonacci.append(siguiente_numero)
    return secuencia_fibonacci[:n]

# Generar los primeros 10 números de Fibonacci
primeros_10_fibonacci = fibonacci(10)
print("Los primeros 10 números de la serie Fibonacci son:")
print(primeros_10_fibonacci)

