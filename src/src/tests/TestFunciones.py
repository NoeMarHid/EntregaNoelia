import math
from typing import Callable, Optional

#funciones

def producto(n: int, k: int) -> int:

    producto_total: int = 1 
    for i in range(k + 1): 
        producto_total *= (n - i + 1) 
    return producto_total

def producto_secuencia_geometrica(a1: float, r: float, k: int) -> float:
  
    producto: float = 1.0  
    for n in range(1, k + 1):  
        an = a1 * r**(n - 1)  
        producto *= an  
    return producto

def numero_combinatorio(n: int, k: int) -> int:
    
    if k > n:
        return 0  
    return math.comb(n, k) 

def S(n: int, k: int) -> float:
    
    suma = 0  
    for i in range(k + 1):  
        signo = (-1) ** i 
        combinatorio_val = numero_combinatorio(k, i)  
        potencia = (k - i) ** n  
        suma += signo * combinatorio_val * potencia  
    
    resultado = suma / math.factorial(k)
    return resultado

def newton_metodo(f: Callable[[float], float], f_prime: Callable[[float], float], 
                  x0: float, epsilon: float, max_iter: int = 1000) -> Optional[float]:
    
    xn = x0
    for n in range(max_iter):
        fxn = f(xn)
        if abs(fxn) <= epsilon:  
            print(f"Raíz encontrada después de {n + 1} iteraciones: x = {xn}")
            return xn
        fpxn = f_prime(xn)
        if fpxn == 0:  
            print("La derivada es cero. No se puede continuar con el método de Newton.")
            return None
        xn = xn - fxn / fpxn  
        
    print("Se alcanzó el número máximo de iteraciones sin encontrar la raíz.")
    return None  


#pruebas

if __name__ == "__main__":
    # Función 1: Producto ∏ (n - i + 1)
    n = 4
    k = 2
    resultado_funcion1 = producto(n, k)
    print(f"Producto para n={n}, k={k} es: {resultado_funcion1}")

    # Función 2: Producto de una secuencia geométrica
    a1 = 1
    r = 2
    k = 2
    resultado_funcion2 = producto_secuencia_geometrica(a1, r, k)
    print(f"Producto de la secuencia geométrica es: {resultado_funcion2}")

    # Función 3: Número combinatorio (n sobre k)
    n = 5
    k = 2
    resultado_funcion3 = numero_combinatorio(n, k)
    print(f"El número combinatorio ({n} sobre {k}) es: {resultado_funcion3}")

    # Función 4: Cálculo de S(n, k)
    n = 3
    k = 2
    resultado_funcion4 = S(n, k)
    print(f"S({n}, {k}) = {resultado_funcion4}")

    # Función 5: Método de Newton para encontrar una raíz
    def f(x):
        return x**2 - 2  # Función f(x) = x^2 - 2

    def f_prime(x):
        return 2 * x  # Derivada de f(x), f'(x) = 2x

    x0 = 1.0
    epsilon = 1e-6
    raiz = newton_metodo(f, f_prime, x0, epsilon)
    print(f"Raíz aproximada: {raiz}")
    
