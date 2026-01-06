@echo off
chcp 65001 >nul
title Party Limit Begone - Instalador

echo.
echo ============================================================
echo   Party Limit Begone - Instalador Automatico
echo   Para Baldur's Gate 3
echo ============================================================
echo.

REM Verifica se o executável existe (preferido)
if exist "InstalarMod.exe" (
    echo [OK] Executavel encontrado!
    echo.
    echo Iniciando instalador...
    echo.
    InstalarMod.exe
    goto :end
)

if exist "dist\InstalarMod.exe" (
    echo [OK] Executavel encontrado!
    echo.
    echo Iniciando instalador...
    echo.
    dist\InstalarMod.exe
    goto :end
)

REM Se não tem exe, tenta Python
echo [INFO] Executavel nao encontrado, tentando Python...
echo.

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado e executavel nao disponivel!
    echo.
    echo Para usar este instalador, voce precisa de uma das opcoes:
    echo.
    echo   1. Baixar o InstalarMod.exe do repositorio
    echo   2. Instalar Python: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado!
python --version
echo.

REM Verifica se os arquivos do mod estão presentes
if not exist "PartyLimitBegone.pak" (
    echo [AVISO] PartyLimitBegone.pak nao encontrado!
    echo.
    echo Baixe os arquivos do mod em:
    echo https://www.nexusmods.com/baldursgate3/mods/327
    echo.
    echo Arquivos necessarios:
    echo - PartyLimitBegone.pak
    echo - PartyLimitBegonePatcher.bat
    echo - Pasta PatchFiles
    echo.
    echo Coloque-os na mesma pasta deste instalador.
    echo.
    pause
    exit /b 1
)

if not exist "PartyLimitBegonePatcher.bat" (
    echo [AVISO] PartyLimitBegonePatcher.bat nao encontrado!
    echo.
    echo Baixe o patch multiplayer em:
    echo https://www.nexusmods.com/baldursgate3/mods/327
    echo.
    echo Extraia e coloque PartyLimitBegonePatcher.bat e
    echo a pasta PatchFiles na mesma pasta deste instalador.
    echo.
    pause
    exit /b 1
)

echo [OK] Arquivos do mod encontrados!
echo.
echo Iniciando instalador...
echo.

REM Executa o instalador Python
python party_limit_begone_installer.py

if %errorlevel% neq 0 (
    echo.
    echo [ERRO] Ocorreu um erro durante a instalacao.
    echo.
    pause
    exit /b 1
)

:end
exit /b 0
