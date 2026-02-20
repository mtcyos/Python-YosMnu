#import os
import sys
import importlib
import subprocess
import platform

# Modulos que necesita la aplicYos.acion
Mdl=("pip",) #,"psutil","pytimedinput","pyfiglet")

# pip uninstall dbfread
#python3 -m pip uninstall dbfread --break-system-packages

# Verifico que Existen los modulos necesarios
for Dat in Mdl:
#    input(f"Verificando Modulo {Dat}")
    try:
        importlib.import_module(Dat)
    except ImportError:
        print(f"\nEl módulo '{Dat}' no está instalado o no se encuentra.")
        if input("Instalar (S=Instalar) : " ).upper()=="S":
            print(f"Instalando {Dat}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", Dat, "--break-system-packages"])
    except Exception as e:
        print(f"Ocurrió otro error al importar: {e}")
