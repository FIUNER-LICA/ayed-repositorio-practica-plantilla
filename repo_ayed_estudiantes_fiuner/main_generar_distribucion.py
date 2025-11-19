import os
import sys
import subprocess
from pathlib import Path


# Si está en Windows: abre una nueva terminal, activa el entorno virtual y corre "python -m build". 
# Si build no está instalado, lo instala primero.


def find_venv():
    # Prioriza VIRTUAL_ENV, luego carpetas comunes .venv/venv en el repo.
    venv = os.environ.get("VIRTUAL_ENV")
    if venv:
        return Path(venv)
    for name in (".venv", "venv"):
        p = Path.cwd() / name
        if p.exists():
            return p
    return None

def main_win():
    print(">>> Ejecutando en Windows...")
        
    venv_path = find_venv()
    print(f">>> Entorno virtual detectado en: {venv_path}" if venv_path else "No se detectó entorno virtual.")
    
    print(">>> Obteniendo ruta a intérprete de entorno virtual...")
    python_exe = venv_path.joinpath("Scripts", "python.exe")
    
    print(">>> Verificando si build está instalado en el entorno virtual...")
    try:
        subprocess.run([str(python_exe), "-m", "build", "--version"], check=True)
        print(">>> build está instalado correctamente.")
    except subprocess.CalledProcessError:
        print(">>> build no está instalado en el entorno virtual.", file=sys.stderr)
        print(">>> Instalar build en el entorno virtual...")
        subprocess.run([str(python_exe), "-m", "pip", "install", "--upgrade", "build"], check=True)
                
    print(">>> Ejecutando 'python -m build'...")
    subprocess.run([str(python_exe), "-m", "build"], check=True)
    
    print(">>> Proceso completado.")


if __name__ == "__main__":    
    if sys.platform.startswith("win"):
        main_win()