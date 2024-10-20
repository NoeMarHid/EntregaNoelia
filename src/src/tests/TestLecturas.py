import string
import csv
from typing import Optional, List, Set

def contar_palabra(fichero: str, cad: str) -> int: 
     
    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            contenido: str = file.read()
            contenido = contenido.translate(str.maketrans('', '', string.punctuation)).lower()
            palabras: List[str] = contenido.split()
            return palabras.count(cad.lower())
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero}' no fue encontrado.")
        return 0

def lineas_con_cadena(fichero: str, cad: str) -> List[str]:  
      
    lineas_encontradas: List[str] = []
    
    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            for linea in file:
                if cad.lower() in linea.lower():  
                    lineas_encontradas.append(linea.strip())  
        return lineas_encontradas
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero}' no fue encontrado.")
        return []

def palabras_unicas(fichero: str) -> List[str]:
    
    palabras_unicas: Set[str] = set() 
    
    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            for linea in file:
               
                linea = linea.translate(str.maketrans('', '', string.punctuation)).lower()
                palabras: List[str] = linea.split()
                palabras_unicas.update(palabras)  
        
        return list(palabras_unicas) 
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero}' no fue encontrado.")
        return []

def longitud_promedio_lineas(file_path: str, sep: str = ',') -> Optional[float]:
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=sep)
            
            longitudes: List[int] = []
            for row in reader:
                linea: str = sep.join(row)
                longitudes.append(len(linea))
            
            if not longitudes:
                return None 
            
            longitud_promedio: float = sum(longitudes) / len(longitudes)
            return longitud_promedio
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no fue encontrado.")
        return None
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return None


# pruebas

if __name__ == "__main__":
    
    # 6. Prueba para contar palabra 
    fichero_palabra = "lin_quijote.txt"
    cad = "quijote"
    cantidad = contar_palabra(fichero_palabra, cad)
    print(f"La palabra '{cad}' aparece {cantidad} veces en el archivo '{fichero_palabra}'.")

    # 7. Prueba para buscar líneas con una cadena específica
    fichero_quijote = "lin_quijote.txt"
    palabra = "quijote"
    lineas = lineas_con_cadena(fichero_quijote, palabra)
    print(f"Las líneas en las que aparece la palabra '{palabra}' son: {lineas}")

    # 8. Prueba para encontrar palabras únicas
    fichero_palabras = "archivo_palabras.txt"
    palabras = palabras_unicas(fichero_palabras)
    print(f"Las palabras únicas en el fichero {fichero_palabras} son: {palabras}")

    # 9. Prueba para calcular la longitud promedio de las líneas en un CSV
    fichero_csv = "palabras_random.csv"
    promedio = longitud_promedio_lineas(fichero_csv)
    if promedio is not None:
        print(f"La longitud promedio de las líneas del fichero {fichero_csv} es: {promedio:.1f}")
    else:
        print(f"No se pudo calcular la longitud promedio del archivo '{fichero_csv}'.")
        
        