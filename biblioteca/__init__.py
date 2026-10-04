import os
import glob

# Pega todos os arquivos .py da pasta (menos __init__.py)
modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
__all__ = []

for m in modules:
    nome = os.path.basename(m)[:-3]  # tira extensão .py
    if nome != "__init__":
        __all__.append(nome)
        __import__(f"biblioteca.{nome}")
