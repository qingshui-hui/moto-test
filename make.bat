@echo off
if "%1" == "init" goto init
if "%1" == "venv" goto venv
if "%1" == "pip-list" goto pip-list
echo syntax: make [init^|venv^|pip-list]
goto end

:init
rem Create venv
py -3.9 -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\activate
goto end

:venv
rem Activate venv
.venv\Scripts\activate
goto end

:pip-list
rem List installed python packages
pip list --format freeze --not-required --exclude pip --exclude setuptools
goto end

:end
rem End
