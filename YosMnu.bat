@echo off

Set AplNom=YosMnu
Set ApDir=%~dp0

:: Pongo os Path temporales
call %ApDir%Lib\Yos\YosAccDirPth.bat %ApDir%

:: Accedo a disco/directorio 
cd /d %ApDir%%AplNom%\

:: Ejecuto Python
echo Python - %AplNom%

python Main.py

echo.
echo Python - %AplNom% - Script Finalizado
timeout /t 8
exit