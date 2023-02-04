@echo off

call activate myenv
pyinstaller.exe^
 --onefile^
 --clean^
 --windowed^
 --specpath ./bin^
 --workpath ./bin^
 --distpath ./bin^
 --paths %~dp0^
 --paths %~dp0/lib^
 --paths %~dp0/lib/ui^
 main_tray.py

robocopy %~dp0/resources %~dp0/bin/resources /E

call conda deactivate

pause