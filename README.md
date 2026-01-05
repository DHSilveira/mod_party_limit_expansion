# 🎮 Party Limit Begone - Instalador Automático

Instalador automático para o mod **Party Limit Begone** do Baldur's Gate 3. Jogue com mais de 4 jogadores facilmente!

## 📋 O que este mod faz?

O **Party Limit Begone** remove o limite de 4 jogadores do Baldur's Gate 3, permitindo que você jogue com 5, 6, 8 ou mais amigos simultaneamente!

## ✨ Recursos do Instalador

- ✅ Detecção automática da instalação do BG3
- ✅ Instalação automática do mod
- ✅ Aplicação automática do patch multiplayer
- ✅ Interface simples e intuitiva
- ✅ Suporte para Steam e GOG
- ✅ Verificação de arquivos necessários
- ✅ Criação automática de backup

## 🚀 Como usar

### Requisitos

- Windows 10/11
- Python 3.7 ou superior
- Baldur's Gate 3 instalado

### Instalação Rápida

1. **Baixe este repositório**
   ```bash
   git clone https://github.com/SEU_USUARIO/party-limit-begone-installer.git
   cd party-limit-begone-installer
   ```

2. **Baixe os arquivos do mod**
   
   Você precisa baixar manualmente os seguintes arquivos do [Nexus Mods](https://www.nexusmods.com/baldursgate3/mods/327):
   - `PartyLimitBegone.pak` (arquivo do mod)
   - `Party Limit Begone Multiplayer Patch` (arquivo .rar com o patcher)
   
   Extraia o conteúdo do patch e coloque os seguintes arquivos na mesma pasta do instalador:
   - `PartyLimitBegone.pak`
   - `PartyLimitBegonePatcher.bat`
   - Pasta `PatchFiles`

3. **Execute o instalador**
   ```bash
   python party_limit_begone_installer.py
   ```
   
   Ou simplesmente clique duas vezes no arquivo `party_limit_begone_installer.py`

4. **Siga as instruções na tela!** 🎉

### Estrutura de Arquivos

Sua pasta deve ficar assim antes de executar:

```
party-limit-begone-installer/
├── party_limit_begone_installer.py
├── PartyLimitBegone.pak
├── PartyLimitBegonePatcher.bat
├── PatchFiles/
│   └── (arquivos do patch)
└── README.md
```

## 🎯 Como jogar com mais de 4 jogadores

Após a instalação:

1. **Inicie o Baldur's Gate 3 normalmente**

2. **Configure o multiplayer:**
   - Vá em **Opções → Gameplay**
   - Ative **"Conexão LAN"**

3. **Para jogadores 5+:**
   
   Existem duas opções:
   
   **Opção A: Modo LAN (Recomendado para iniciantes)**
   - Instale um programa como [Hamachi](https://www.vpn.net/) ou [Radmin VPN](https://www.radmin-vpn.com/)
   - Todos os jogadores devem estar na mesma rede virtual
   - O host cria a partida
   - Jogadores 5+ se conectam normalmente

   **Opção B: IP Direto**
   - O host precisa abrir a porta **23253** no roteador
   - Jogadores 5+ digitam o IP do host no campo "Código Direto"

4. **Ordem de entrada (importante!):**
   - Se houver jogadores de console, eles devem entrar **primeiro**
   - Máximo de 3 jogadores de console
   - Jogadores de PC podem entrar depois

5. **Continuar saves antigos:**
   - Crie um novo lobby
   - Todos entram
   - Inicie um novo jogo
   - Carregue o save antigo
   - (O host deve limpar saves duplicados ocasionalmente)

## 🛠️ O que o instalador faz?

1. **Detecta automaticamente** onde o BG3 está instalado (Steam/GOG)
2. **Copia o mod** para a pasta correta de mods
3. **Cria o arquivo de configuração** para ativar o mod
4. **Aplica o patch multiplayer** no executável do jogo
5. **Cria backup automático** do executável original

## ❓ Solução de Problemas

### O instalador não encontrou o BG3
- Digite manualmente o caminho quando solicitado
- Exemplo: `C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3`

### Antivírus bloqueou o patcher
- Isso é normal (falso positivo)
- Adicione uma exceção para a pasta do BG3
- Todos os arquivos do Nexus Mods são escaneados

### O mod não aparece no jogo
- Verifique se o arquivo `modsettings.lsx` foi criado em:
  `%LOCALAPPDATA%\Larian Studios\Baldur's Gate 3\PlayerProfiles\Public\`
- Reinicie o jogo completamente

### Não consigo conectar mais de 4 jogadores
- Certifique-se de que o **patch multiplayer** foi aplicado
- Verifique se existe o arquivo `bg3.exe.backup` na pasta `bin`
- Habilite "Conexão LAN" nas opções do jogo

## 🔄 Como desinstalar

### Remover o patch multiplayer:
1. Vá para: `C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\bin`
2. Delete o arquivo `bg3.exe`
3. Renomeie `bg3.exe.backup` para `bg3.exe`

### Remover o mod:
1. Delete o arquivo em: `%LOCALAPPDATA%\Larian Studios\Baldur's Gate 3\Mods\PartyLimitBegone.pak`
2. Delete ou edite: `%LOCALAPPDATA%\Larian Studios\Baldur's Gate 3\PlayerProfiles\Public\modsettings.lsx`

## 📝 Créditos

- **Mod original:** [Sildur](https://www.nexusmods.com/baldursgate3/mods/327) - Party Limit Begone
- **Instalador:** Criado para facilitar a instalação do mod

## ⚠️ Aviso Legal

- Este é um mod não oficial
- Use por sua conta e risco
- Faça backup dos seus saves antes de usar
- Não suportado oficialmente pela Larian Studios

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

## 📜 Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

O mod Party Limit Begone tem sua própria licença - confira no [Nexus Mods](https://www.nexusmods.com/baldursgate3/mods/327).

---

**Divirta-se jogando com seus amigos! 🎮✨**

Se este instalador te ajudou, deixe uma ⭐ no repositório!
