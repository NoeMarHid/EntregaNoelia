import math
from typing import Callable, Optional

# 1. Función para calcular el producto ∏ (𝑛 − 𝑖 + 1) de i=0 hasta k
def producto(n: int, k: int) -> int:
    """
    Calcula el producto de la secuencia ∏ (𝑛 − 𝑖 + 1) desde i=0 hasta k.

    :param n: Número entero mayor que k.
    :param k: Límite superior del sumatorio.
    :return: Producto calculado.
    """
    producto_total: int = 1  # Inicializamos el producto en 1 (elemento neutro del producto)
    for i in range(k + 1):  # Iteramos desde i=0 hasta i=k (incluye k)
        producto_total *= (n - i + 1)  # Realizamos la operación de multiplicación
    return producto_total


# 2. Función para calcular el producto de una secuencia geométrica
def producto_secuencia_geometrica(a1: float, r: float, k: int) -> float:
    """
    Calcula el producto de los primeros k términos de una secuencia geométrica.

    :param a1: Primer término de la secuencia.
    :param r: Razón de la secuencia.
    :param k: Número de términos de la secuencia a considerar.
    :return: Producto de los primeros k términos.
    """
    producto: float = 1.0  # Inicializamos el producto en 1
    for n in range(1, k + 1):  # Iteramos desde n = 1 hasta n = k
        an = a1 * r**(n - 1)  # Calcula el n-ésimo término de la secuencia
        producto *= an  # Multiplica el producto por el n-ésimo término
    return producto


# 3. Función para calcular el número combinatorio (𝑛 𝑘)
def numero_combinatorio(n: int, k: int) -> int:
    """
    Calcula el número combinatorio C(n, k).

    :param n: Número total de elementos.
    :param k: Número de elementos en el subconjunto.
    :return: El valor del número combinatorio.
    """
    if k > n:
        return 0  # El número combinatorio no está definido si k > n
    return math.comb(n, k)  # math.comb se usa para calcular el combinatorio en Python 3.8+


# 4. Función para calcular S(n, k) dado por un sumatorio
def S(n: int, k: int) -> float:
    """
    Calcula la suma de la fórmula S(n, k) basada en un sumatorio.

    :param n: Número entero.
    :param k: Número entero.
    :return: El valor del sumatorio S(n, k).
    """
    suma = 0  # Inicializamos la suma
    for i in range(k + 1):  # Sumatorio desde i=0 hasta k
        signo = (-1) ** i  # Alterna el signo según el valor de i
        combinatorio_val = numero_combinatorio(k, i)  # Calculamos el combinatorio C(k sobre i)
        potencia = (k - i) ** n  # Calculamos (k - i)^n
        suma += signo * combinatorio_val * potencia  # Añadimos el término al sumatorio

    # Dividimos el resultado por k!
    resultado = suma / math.factorial(k)
    return resultado


# 5. Método de Newton para encontrar una raíz
def newton_metodo(f: Callable[[float], float], f_prime: Callable[[float], float], 
                  x0: float, epsilon: float, max_iter: int = 1000) -> Optional[float]:
    """
    Aplica el método de Newton para encontrar una raíz de la función f(x).

    :param f: La función a la cual buscamos encontrar la raíz.
    :param f_prime: Derivada de la función f.
    :param x0: Valor inicial para la búsqueda de la raíz.
    :param epsilon: Valor mínimo de error permitido.
    :param max_iter: Máximo número de iteraciones.
    :return: El valor de la raíz si se encuentra, None si no se encuentra.
    """
    xn = x0
    for n in range(max_iter):
        fxn = f(xn)
        if abs(fxn) <= epsilon:  # Si el valor absoluto de f(xn) es menor que epsilon, hemos encontrado la raíz
            print(f"Raíz encontrada después de {n + 1} iteraciones: x = {xn}")
            return xn
        fpxn = f_prime(xn)
        if fpxn == 0:  # Si la derivada es cero, el método falla
            print("La derivada es cero. No se puede continuar con el método de Newton.")
            return None
        xn = xn - fxn / fpxn  # Actualizamos xn usando el método de Newton
    
    print("Se alcanzó el número máximo de iteraciones sin encontrar la raíz.")
    return None  # Si no se encontró una raíz después de max_iter iteraciones

