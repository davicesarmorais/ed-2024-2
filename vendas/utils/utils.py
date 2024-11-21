import pickle
import platform
import subprocess
import os

def salvar(path: str, obj) -> None:
    with open(path, "wb") as f:
        pickle.dump(obj, f)
        
def carregar(path: str) -> dict:
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def limpar_tela() -> None:
    """Limpa a tela do terminal."""
    if platform.system() == "Windows" and os.getenv("TERM") != "xterm":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def prosseguir() -> None:
    input("Aperte qualquer tecla para prosseguir...")
