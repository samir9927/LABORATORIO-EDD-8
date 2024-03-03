""" Asegurar que un módulo se ha importado correctamente.
"""

try:
    import math  # Intenta importar el módulo
    print("El módulo se ha importado correctamente.")  # Si la importación tiene éxito, imprime un mensaje indicando que el módulo se ha importado correctamente
except ImportError:
    print("Error: No se pudo importar el módulo.")  # Si ocurre un error durante la importación (por ejemplo, si el módulo no existe o hay algún otro problema), maneja la excepción ImportError e imprime un mensaje de error indicando que no se pudo importar el módulo
