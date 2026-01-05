@echo off
chcp 65001 >nul
title Party Limit Begone - Instalador

echo.
echo ============================================================
echo   Party Limit Begone - Instalador Automático
echo   Para Baldur's Gate 3
echo ============================================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python não encontrado!
    echo.
    echo Python é necessário para executar este instalador.
    echo.
    echo Por favor, instale Python:
    echo 1. Acesse: https://www.python.org/downloads/
    echo 2. Baixe a versão mais recente para Windows
    echo 3. Durante a instalação, marque "Add Python to PATH"
    echo 4. Execute este arquivo novamente após instalar
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado!
python --version
echo.

REM Verifica se os arquivos do mod estão presentes
if not exist "PartyLimitBegone.pak" (
    echo [AVISO] PartyLimitBegone.pak não encontrado!
    echo.
    echo Baixe os arquivos do mod em:
    echo https://www.nexusmods.com/baldursgate3/mods/327
    echo.
    echo Arquivos necessários:
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
    echo [AVISO] PartyLimitBegonePatcher.bat não encontrado!
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
    echo [ERRO] Ocorreu um erro durante a instalação.
    echo.
    pause
    exit /b 1
)

exit /b 0
