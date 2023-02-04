@echo off
@echo on
set target_dir=bin

call activate myenv

pyinstaller.exe^
 --onefile^
 --clean^
 --windowed^
 --specpath ./%target_dir%^
 --workpath ./%target_dir%^
 --distpath ./%target_dir%^
 --paths %~dp0^
 --paths %~dp0lib^
 --paths %~dp0lib\ui^
 main_tray.py

robocopy %~dp0resources %~dp0%target_dir%\resources /E

call conda deactivate

pause