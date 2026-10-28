import os
import shutil
from pathlib import Path

# 1. Define la carpeta que quieres limpiar (puedes cambiar esta ruta)
# Usa '.' para la carpeta actual, o una ruta completa como 'C:/Users/TuUsuario/Downloads'
CARPETA_A_ORGANIZAR = Path('.')

# 2. Diccionario que asocia cada tipo de archivo con su carpeta destino
EXTENSIONES_CARPETAS = {
    # Documentos
    '.pdf': 'Documentos',
    '.docx': 'Documentos',
    '.txt': 'Documentos',
    '.xlsx': 'Documentos',
    '.pptx': 'Documentos',
    # Imágenes
    '.jpg': 'Imagenes',
    '.jpeg': 'Imagenes',
    '.png': 'Imagenes',
    '.gif': 'Imagenes',
    # Videos
    '.mp4': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    # Música
    '.mp3': 'Musica',
    '.wav': 'Musica',
    # Archivos comprimidos
    '.zip': 'Comprimidos',
    '.rar': 'Comprimidos',
    '.tar': 'Comprimidos',
}

def organizar_carpeta():
    print(f"Iniciando la organización en: {CARPETA_A_ORGANIZAR.resolve()}\n")
    
    # Validar si la carpeta existe
    if not CARPETA_A_ORGANIZAR.exists():
        print("La carpeta especificada no existe.")
        return

    CONTEO_MOVIDOS = 0

    # 3. Recorrer los elementos dentro de la carpeta
    for elemento in CARPETA_A_ORGANIZAR.iterdir():
        # Ignorar si es una carpeta o si es el propio script de python
        if elemento.is_dir() or elemento.name == 'organizador.py':
            continue
            
        # Obtener la extensión del archivo en minúsculas
        extension = elemento.suffix.lower()
        
        # Verificar si conocemos la extensión para saber a dónde moverlo
        if extension in EXTENSIONES_CARPETAS:
            nombre_carpeta_destino = EXTENSIONES_CARPETAS[extension]
            ruta_carpeta_destino = CARPETA_A_ORGANIZAR / nombre_carpeta_destino
            
            # Crear la carpeta de destino si no existe todavía
            ruta_carpeta_destino.mkdir(exist_ok=True)
            
            # Mover el archivo a su nueva ubicación
            try:
                shutil.move(str(elemento), str(ruta_carpeta_destino / elemento.name))
                print(f"Movido: {elemento.name} -> {nombre_carpeta_destino}/")
                CONTEO_MOVIDOS += 1
            except Exception as e:
                print(f"No se pudo mover {elemento.name}. Error: {e}")

    print(f"\n¡Organización completada! Se movieron {CONTEO_MOVIDOS} archivos.")

if __name__ == '__main__':
    organizar_carpeta()
