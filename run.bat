@echo off
REM Run the Year Planner generator
REM Usage: run.bat [options]
REM   -c, --config FILE   Path to YAML configuration file
REM   -o, --output FILE   Output path for generated document

cls
.venv\Scripts\python.exe -X utf8 src/main.py %*
