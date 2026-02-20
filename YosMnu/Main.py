#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
   YosCtr.py
   Control central entorno Yos

   Copyright (c) 2026 Miguel Tortosa

   Licenciado bajo la Licencia MIT.

   Consulte el archivo LICENCIA en la raíz del proyecto para más información.
"""
import sys
import subprocess
import os
import platform
import importlib
import importlib.util

# Verifico el Sistema Operativo

match platform.system():
    case "Windows":
        script_path = os.path.join(os.path.dirname(__file__), 'Script')
        sys.path.append(os.getcwd()+"\\Script\\")
        sys.path.append(os.path.abspath("..")+"\\Lib\\")
    case "Linux":
        script_path = os.getcwd()+"/Script/"
        sys.path.append(os.getcwd()+"/Script/")
        sys.path.append(os.path.abspath("..")+os.path.abspath("/Lib/"))
#   case "Darwin": # macOS
#       sys.path.append(os.path.abspath("..")+os.path.abspath("/Lib/"))
#   case "iOS": # iOS or iPadOS
#       sys.path.append(os.path.abspath("..")+os.path.abspath("/Lib/"))
#   case "Android": # macOS
#       sys.path.append(os.path.abspath("..")+os.path.abspath("/Lib/"))
#   case "Java": # Java
#       sys.path.append(os.path.abspath("..")+os.path.abspath("/Lib/"))
    case _:
        print("YosCtr.36")
        print(f"Sistema Operativo {platform.system()} no implementado.")
        sys.exit(0)

# Configuracion del Script
import Ini
import Yos

YosCfg["Dbg"]="" # MODO DEPURACION S="Completo"

Yos.AplIni()    # Inicio el Entorno

# Importo TODOS los .py de ./Script
if script_path not in sys.path:
    sys.path.append(script_path)
    for filename in os.listdir(script_path):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            spec = importlib.util.spec_from_file_location(module_name, os.path.join(script_path, filename))
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                sys.modules[module_name] = module
                globals()[module_name] = module
                #print(f"Bin > Módulo '{module_name}' cargado con éxito.")
else:
    print(f"Yos > Error: No se encuentra la carpeta {script_path}")
# FIN - Los Scrpt de trabajo

def main():
    # DEFINO EL MENU A USAR

    # INICIO - Proceso del menu
    while True:
        # Capturamos la entrada del usuario
        MnuFnc = Yos.Mnu()

        if MnuFnc == "YosMnuCag":
            Yos.MnuRec("Main")
            continue

        # Lanzamos la magia! exec() convierte el texto en código real)
        if MnuFnc[:7]=="YosCmd:":
            MnuFnc=MnuFnc.replace("YosCmd:", "")

            if YosCfg["Etn"] == "Windows":
                subprocess.Popen(['cmd', '/c', 'start', '', MnuFnc], shell=True)
            elif YosCfg["Etn"] == "Darwin": # Mac
                subprocess.Popen(['open', MnuFnc])
            else: # Linux y otros
                subprocess.Popen(['xdg-open', MnuFnc])

            continue

        try:
            exec(MnuFnc)
        except Exception as e:
            input(f"Error al ejecutar: {e}")
# FIN - Proceso del menu

if __name__ == '__main__':
    main()

