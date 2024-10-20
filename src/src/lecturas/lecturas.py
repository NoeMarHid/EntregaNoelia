import string
import csv
from typing import Optional, List, Set


# 6. Función para contar cuántas veces aparece una palabra en un fichero
def contar_palabra(fichero: str, cad: str) -> int:
    """
    Cuenta cuántas veces aparece una palabra específica en un fichero.

    :param fichero: Ruta del archivo de texto.
    :param cad: Palabra a buscar en el archivo.
    :return: Número de veces que aparece la palabra.
    """
    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            contenido: str = file.read()
            # Eliminar puntuación y convertir todo a minúsculas
            contenido = contenido.translate(str.maketrans('', '', string.punctuation)).lower()
            palabras: List[str] = contenido.split()
            return palabras.count(cad.lower())
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero}' no fue encontrado.")
        return 0


# 7. Función para encontrar líneas que contengan una cadena específica
def lineas_con_cadena(fichero: str, cad: str) -> List[str]:
    """
    Busca todas las líneas que contienen una cadena específica en un fichero.

    :param fichero: Ruta del archivo de texto.
    :param cad: Cadena a buscar en las líneas del archivo.
    :return: Lista de líneas que contienen la cadena.
    """
    lineas_encontradas: List[str] = []
    
    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            for linea in file:
                if cad.lower() in linea.lower():  # Ignorar mayúsculas/minúsculas
                    lineas_encontradas.append(linea.strip())  # Eliminar espacios extra
        return lineas_encontradas
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero}' no fue encontrado.")
        return []


# 8. Función para encontrar palabras únicas en un fichero
def palabras_unicas(fichero: str) -> List[str]:
    """
    Encuentra todas las palabras únicas en un fichero de texto.

    :param fichero: Ruta del archivo de texto.
    :return: Lista de palabras únicas encontradas en el archivo.
    """
    palabras_unicas: Set[str] = set()  # Utilizamos un conjunto para evitar repeticiones
    
    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            for linea in file:
                # Eliminar puntuación y convertir todo a minúsculas
                linea = linea.translate(str.maketrans('', '', string.punctuation)).lower()
                palabras: List[str] = linea.split()
                palabras_unicas.update(palabras)  # Añadir palabras al conjunto
        
        return list(palabras_unicas)  # Convertir el conjunto en lista
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero}' no fue encontrado.")
        return []


# 9. Función para calcular la longitud promedio de las líneas en un fichero CSV
def longitud_promedio_lineas(file_path: str, sep: str = ',') -> Optional[float]:
    """
    Calcula la longitud promedio de las líneas en un fichero CSV.

    :param file_path: Ruta del archivo CSV.
    :param sep: Separador usado en el CSV (por defecto es coma).
    :return: Longitud promedio de las líneas o None si el archivo está vacío o no existe.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=sep)
            
            longitudes: List[int] = []
            for row in reader:
                linea: str = sep.join(row)
                longitudes.append(len(linea))
            
            if not longitudes:
                return None  # Si no hay líneas en el archivo
            
            longitud_promedio: float = sum(longitudes) / len(longitudes)
            return longitud_promedio
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no fue encontrado.")
        return None
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return None
    
    