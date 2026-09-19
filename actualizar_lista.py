import json
import os

ARCHIVO_JSON = "links.json"

def actualizar():
    nuevos_links = [
        "https://vm.tiktok.com/ZSqnyLYLA/"
    ]
    
    data = {"videos": nuevos_links}
    
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print("[Éxito] Lista de enlaces actualizada en la nube.")

if __name__ == "__main__":
    actualizar()
