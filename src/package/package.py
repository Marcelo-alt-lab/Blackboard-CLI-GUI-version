"""
Script para empaquetar de forma segura Blackboard CLI en un archivo ZIP limpio.
Excluye credenciales, cookies, entorno virtual y materiales privados.
"""
import sys
import zipfile
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from src.config.config import VERSION

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ZIP_NAME = BASE_DIR / f"Blackboard-CLI-v{VERSION}.zip"

# Archivos base del proyecto
FILES_TO_INCLUDE = [
    "src/",
    "requirements.txt",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
]

# Lanzadores multiplataforma (en git tienen nombre fijo, pero en el ZIP se nombran con la versión automáticamente)
LAUNCHERS = {
    "BlackboardCLI-Windows.bat": f"BlackboardCLI-v{VERSION}-Windows.bat",
    "BlackboardCLI-macOS.command": f"BlackboardCLI-v{VERSION}-macOS.command",
    "BlackboardCLI-Linux.sh": f"BlackboardCLI-v{VERSION}-Linux.sh",
}

def create_package():
    print(f"[*] Empaquetando Blackboard CLI v{VERSION}...")
    if ZIP_NAME.exists():
        ZIP_NAME.unlink()

    with zipfile.ZipFile(ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as zipf:
        for item in FILES_TO_INCLUDE:
            p = BASE_DIR / item
            if p.exists():
                if p.is_dir():
                    for f in p.rglob("*"):
                        if "__pycache__" not in str(f) and f.is_file():
                            arcname = f"Blackboard-CLI-v{VERSION}/{f.relative_to(BASE_DIR)}"
                            zipf.write(f, arcname=arcname)
                    print(f"  + Incluido directorio: {item}")
                else:
                    zipf.write(p, arcname=f"Blackboard-CLI-v{VERSION}/{item}")
                    print(f"  + Incluido: {item}")
            else:
                print(f"  - No encontrado: {item}")

        for src_name, target_name in LAUNCHERS.items():
            p = BASE_DIR / src_name
            if p.exists():
                zipf.write(p, arcname=f"Blackboard-CLI-v{VERSION}/{target_name}")
                print(f"  + Lanzador ({target_name}): {src_name}")
            else:
                print(f"  - No encontrado: {src_name}")

    print(f"\n[✓] Paquete de versión listo: {ZIP_NAME.name}")
    print("[✓] Totalmente seguro: no contiene tus contraseñas, cookies ni archivos personales.")

if __name__ == "__main__":
    create_package()
