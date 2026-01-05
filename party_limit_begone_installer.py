#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Party Limit Begone - Instalador Automático
Instalador automático para o mod Party Limit Begone do Baldur's Gate 3
"""

import os
import sys
import shutil
import subprocess
import winreg
from pathlib import Path
from typing import Optional, List

class Colors:
    """Cores para o terminal"""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header():
    """Imprime o cabeçalho do instalador"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}  Party Limit Begone - Instalador Automático{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}  Para Baldur's Gate 3{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}\n")

def print_success(msg: str):
    """Imprime mensagem de sucesso"""
    print(f"{Colors.GREEN}✓ {msg}{Colors.RESET}")

def print_error(msg: str):
    """Imprime mensagem de erro"""
    print(f"{Colors.RED}✗ {msg}{Colors.RESET}")

def print_info(msg: str):
    """Imprime mensagem informativa"""
    print(f"{Colors.YELLOW}ℹ {msg}{Colors.RESET}")

def print_step(step: int, total: int, msg: str):
    """Imprime o passo atual"""
    print(f"\n{Colors.BOLD}[Passo {step}/{total}] {msg}{Colors.RESET}")

def find_steam_path() -> Optional[Path]:
    """Tenta encontrar o caminho do Steam via registro do Windows"""
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                            r"SOFTWARE\WOW6432Node\Valve\Steam")
        steam_path, _ = winreg.QueryValueEx(key, "InstallPath")
        winreg.CloseKey(key)
        return Path(steam_path)
    except:
        return None

def find_bg3_installation() -> Optional[Path]:
    """Procura a instalação do BG3 em locais comuns"""
    print_info("Procurando instalação do Baldur's Gate 3...")
    
    possible_paths = []
    
    # Tenta encontrar via Steam
    steam_path = find_steam_path()
    if steam_path:
        bg3_steam = steam_path / "steamapps" / "common" / "Baldurs Gate 3"
        possible_paths.append(bg3_steam)
    
    # Caminhos padrão do Steam
    possible_paths.extend([
        Path(r"C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3"),
        Path(r"C:\Program Files\Steam\steamapps\common\Baldurs Gate 3"),
        Path(r"D:\Steam\steamapps\common\Baldurs Gate 3"),
        Path(r"E:\Steam\steamapps\common\Baldurs Gate 3"),
    ])
    
    # GOG paths
    possible_paths.extend([
        Path(r"C:\Program Files (x86)\GOG Galaxy\Games\Baldurs Gate 3"),
        Path(r"C:\GOG Games\Baldurs Gate 3"),
    ])
    
    for path in possible_paths:
        bin_path = path / "bin" / "bg3.exe"
        if bin_path.exists():
            print_success(f"BG3 encontrado em: {path}")
            return path
    
    return None

def get_bg3_path_manual() -> Optional[Path]:
    """Pede ao usuário para inserir o caminho manualmente"""
    print_info("Não foi possível encontrar o BG3 automaticamente.")
    print("Por favor, digite o caminho completo da pasta do Baldur's Gate 3:")
    print("Exemplo: C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3")
    
    while True:
        user_path = input("\nCaminho: ").strip().strip('"')
        path = Path(user_path)
        
        if not path.exists():
            print_error("Caminho não existe. Tente novamente.")
            continue
        
        bin_path = path / "bin" / "bg3.exe"
        if not bin_path.exists():
            print_error("bg3.exe não encontrado neste caminho. Verifique se é a pasta correta.")
            continue
        
        return path

def get_larian_appdata() -> Path:
    """Retorna o caminho para a pasta de mods do BG3"""
    localappdata = Path(os.environ['LOCALAPPDATA'])
    mods_path = localappdata / "Larian Studios" / "Baldur's Gate 3" / "Mods"
    mods_path.mkdir(parents=True, exist_ok=True)
    return mods_path

def install_mod_file(repo_path: Path) -> bool:
    """Instala o arquivo .pak do mod"""
    print_info("Instalando arquivo do mod...")
    
    # Procura pelo arquivo .pak no repositório
    pak_files = list(repo_path.glob("*.pak"))
    
    if not pak_files:
        print_error("Arquivo .pak não encontrado no repositório!")
        print_info("Certifique-se de que o arquivo PartyLimitBegone.pak está na pasta.")
        return False
    
    pak_file = pak_files[0]
    mods_path = get_larian_appdata()
    dest_file = mods_path / pak_file.name
    
    try:
        shutil.copy2(pak_file, dest_file)
        print_success(f"Mod copiado para: {dest_file}")
        return True
    except Exception as e:
        print_error(f"Erro ao copiar mod: {e}")
        return False

def create_modsettings(mods_path: Path) -> bool:
    """Cria o arquivo modsettings.lsx para ativar o mod"""
    print_info("Criando arquivo de configuração do mod...")
    
    profiles_path = mods_path.parent / "PlayerProfiles" / "Public"
    profiles_path.mkdir(parents=True, exist_ok=True)
    
    modsettings_path = profiles_path / "modsettings.lsx"
    
    # Template básico do modsettings.lsx com Party Limit Begone
    modsettings_content = '''<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="0" revision="9" build="331"/>
    <region id="ModuleSettings">
        <node id="root">
            <children>
                <node id="ModOrder">
                    <children>
                        <node id="Module">
                            <attribute id="UUID" type="FixedString" value="3ac7afaa-d96c-4a2b-ac16-f5d3c4a7e31f"/>
                        </node>
                    </children>
                </node>
                <node id="Mods">
                    <children>
                        <node id="ModuleShortDesc">
                            <attribute id="Folder" type="LSString" value="PartyLimitBegone"/>
                            <attribute id="MD5" type="LSString" value=""/>
                            <attribute id="Name" type="LSString" value="Party Limit Begone"/>
                            <attribute id="UUID" type="FixedString" value="3ac7afaa-d96c-4a2b-ac16-f5d3c4a7e31f"/>
                            <attribute id="Version64" type="int64" value="144115188075855872"/>
                        </node>
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>'''
    
    try:
        with open(modsettings_path, 'w', encoding='utf-8') as f:
            f.write(modsettings_content)
        print_success(f"Arquivo de configuração criado: {modsettings_path}")
        return True
    except Exception as e:
        print_error(f"Erro ao criar modsettings.lsx: {e}")
        return False

def apply_multiplayer_patch(bg3_path: Path, repo_path: Path) -> bool:
    """Aplica o patch multiplayer"""
    print_info("Aplicando patch multiplayer...")
    
    bin_path = bg3_path / "bin"
    bg3_exe = bin_path / "bg3.exe"
    backup_exe = bin_path / "bg3.exe.backup"
    
    # Verifica se já foi aplicado
    if backup_exe.exists():
        print_info("Patch já foi aplicado anteriormente.")
        resposta = input("Deseja reaplicar? (s/n): ").strip().lower()
        if resposta != 's':
            return True
    
    # Procura pelo arquivo .bat do patcher
    bat_files = list(repo_path.glob("*Patcher*.bat"))
    
    if not bat_files:
        print_error("Arquivo do patcher não encontrado!")
        print_info("Certifique-se de que PartyLimitBegonePatcher.bat está na pasta.")
        return False
    
    patcher_bat = bat_files[0]
    
    try:
        # Copia o patcher e PatchFiles para a pasta bin
        patcher_dest = bin_path / patcher_bat.name
        shutil.copy2(patcher_bat, patcher_dest)
        
        # Copia a pasta PatchFiles se existir
        patch_files_src = repo_path / "PatchFiles"
        if patch_files_src.exists():
            patch_files_dest = bin_path / "PatchFiles"
            if patch_files_dest.exists():
                shutil.rmtree(patch_files_dest)
            shutil.copytree(patch_files_src, patch_files_dest)
        
        # Executa o patcher
        print_info("Executando o patcher... (isso pode demorar alguns segundos)")
        
        # Usa subprocess para executar o .bat com o .exe como argumento
        result = subprocess.run(
            [str(patcher_dest), str(bg3_exe)],
            cwd=str(bin_path),
            capture_output=True,
            text=True
        )
        
        # Verifica se o backup foi criado
        if backup_exe.exists():
            print_success("Patch multiplayer aplicado com sucesso!")
            # Remove o patcher temporário
            if patcher_dest.exists():
                patcher_dest.unlink()
            return True
        else:
            print_error("Patch pode não ter sido aplicado corretamente.")
            print_info("Verifique se há algum antivírus bloqueando.")
            return False
            
    except Exception as e:
        print_error(f"Erro ao aplicar patch: {e}")
        return False

def check_requirements() -> bool:
    """Verifica se todos os arquivos necessários estão presentes"""
    print_step(1, 5, "Verificando arquivos necessários")
    
    repo_path = Path(__file__).parent
    
    required_files = {
        "PartyLimitBegone.pak": "Arquivo do mod",
        "PartyLimitBegonePatcher.bat": "Patcher multiplayer",
        "PatchFiles": "Arquivos do patch"
    }
    
    missing = []
    for file_name, description in required_files.items():
        file_path = repo_path / file_name
        if not file_path.exists():
            missing.append(f"{description} ({file_name})")
            print_error(f"{description} não encontrado: {file_name}")
        else:
            print_success(f"{description} encontrado")
    
    if missing:
        print_error("\nArquivos faltando! Baixe-os e coloque na mesma pasta do instalador:")
        for item in missing:
            print(f"  - {item}")
        return False
    
    return True

def main():
    """Função principal do instalador"""
    print_header()
    
    # Verifica se está no Windows
    if sys.platform != 'win32':
        print_error("Este instalador funciona apenas no Windows!")
        input("\nPressione Enter para sair...")
        return
    
    # Verifica arquivos necessários
    if not check_requirements():
        input("\nPressione Enter para sair...")
        return
    
    repo_path = Path(__file__).parent
    
    # Passo 2: Encontrar BG3
    print_step(2, 5, "Localizando Baldur's Gate 3")
    bg3_path = find_bg3_installation()
    
    if not bg3_path:
        bg3_path = get_bg3_path_manual()
        if not bg3_path:
            print_error("Não foi possível localizar o BG3. Instalação cancelada.")
            input("\nPressione Enter para sair...")
            return
    
    # Passo 3: Instalar mod
    print_step(3, 5, "Instalando arquivo do mod")
    if not install_mod_file(repo_path):
        print_error("Falha ao instalar o mod.")
        input("\nPressione Enter para sair...")
        return
    
    # Passo 4: Criar modsettings
    print_step(4, 5, "Configurando mod")
    mods_path = get_larian_appdata()
    if not create_modsettings(mods_path):
        print_error("Falha ao configurar o mod.")
        input("\nPressione Enter para sair...")
        return
    
    # Passo 5: Aplicar patch multiplayer
    print_step(5, 5, "Aplicando patch multiplayer")
    if not apply_multiplayer_patch(bg3_path, repo_path):
        print_error("Falha ao aplicar patch multiplayer.")
        input("\nPressione Enter para sair...")
        return
    
    # Sucesso!
    print(f"\n{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}  ✓ INSTALAÇÃO CONCLUÍDA COM SUCESSO!{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.RESET}\n")
    
    print("O mod Party Limit Begone foi instalado e está pronto para usar!")
    print("\nInstruções para jogar:")
    print("1. Inicie o Baldur's Gate 3 normalmente")
    print("2. Crie ou carregue um save multiplayer")
    print("3. Para jogadores 5+:")
    print("   - Use modo LAN (requer Hamachi ou similar)")
    print("   - OU abra a porta 23253 e use IP direto")
    print("4. Habilite 'Conexão LAN' em Opções → Gameplay")
    
    print("\nPara desinstalar:")
    print(f"- Renomeie 'bg3.exe.backup' para 'bg3.exe' em:")
    print(f"  {bg3_path / 'bin'}")
    
    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInstalação cancelada pelo usuário.")
        input("\nPressione Enter para sair...")
    except Exception as e:
        print_error(f"\nErro inesperado: {e}")
        import traceback
        traceback.print_exc()
        input("\nPressione Enter para sair...")
