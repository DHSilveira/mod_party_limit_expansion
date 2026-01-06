# 📖 Manual Completo - Party Limit Begone Installer

Guia detalhado para instalação e uso do mod Party Limit Begone.

## 📑 Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Download dos Arquivos](#download-dos-arquivos)
3. [Instalação Passo a Passo](#instalação-passo-a-passo)
4. [Configuração do Multiplayer](#configuração-do-multiplayer)
5. [Solução de Problemas Detalhada](#solução-de-problemas-detalhada)
6. [Perguntas Frequentes](#perguntas-frequentes)

## Pré-requisitos

### Sistema Operacional
- ✅ Windows 10 (64-bit)
- ✅ Windows 11

### Software Necessário
- ✅ Baldur's Gate 3 (Steam ou GOG)
- ⚡ Python **não é necessário** - o instalador funciona sem ele!

### Espaço em Disco
- Aproximadamente 50 MB livres para os arquivos do mod

### Permissões
- Direitos de administrador podem ser necessários
- Acesso de escrita nas pastas do jogo

## Download dos Arquivos

### 1. Baixar o Instalador (Este Repositório)

**Opção A: Git**
```bash
git clone https://github.com/DHSilveira/mod_party_limit_expansion.git
cd mod_party_limit_expansion
```

**Opção B: Download Direto**
1. Clique em "Code" → "Download ZIP"
2. Extraia o arquivo ZIP
3. Entre na pasta extraída

### 2. Baixar os Arquivos do Mod

Acesse: [Party Limit Begone no Nexus Mods](https://www.nexusmods.com/baldursgate3/mods/327)

**Você precisará de:**

#### Arquivo 1: Mod Principal
- Nome: `Party Limit Begone SE v3.3-327-3-3-XXXXXXXX.zip`
- Dentro dele tem: `PartyLimitBegone.pak`
- **Extraia** o arquivo `.pak`

#### Arquivo 2: Patch Multiplayer
- Nome: `Party Limit Begone Multiplayer Patch v1.6-327-1-6-XXXXXXXX.rar`
- Dentro dele tem:
  - `PartyLimitBegonePatcher.bat`
  - Pasta `PatchFiles`
  - `Readme.txt`
- **Extraia** todos os arquivos

### 3. Organizar os Arquivos

Coloque todos os arquivos na mesma pasta do instalador:

```
mod_party_limit_expansion/
│
├── instalar.bat                          ← Execute este!
├── party_limit_begone_installer.py
├── README.md
├── LICENSE
│
├── PartyLimitBegone.pak                  ← Do mod principal
├── PartyLimitBegonePatcher.bat          ← Do patch multiplayer
└── PatchFiles/                           ← Do patch multiplayer
    ├── (vários arquivos .dll e .patch)
```

## Instalação Passo a Passo

### Método 1: Usando o Arquivo .BAT (Recomendado para Iniciantes)

1. **Clique duas vezes** em `instalar.bat`

2. **Aguarde** a verificação automática:
   - ✅ Python instalado
   - ✅ Arquivos do mod presentes

3. **O instalador vai:**
   - Procurar automaticamente o BG3
   - Se não encontrar, pedirá o caminho manualmente
   - Instalar o mod
   - Aplicar o patch multiplayer

4. **Pronto!** Quando ver "INSTALAÇÃO CONCLUÍDA", está tudo certo!

### Método 2: Usando Python Diretamente

1. Abra o **PowerShell** ou **CMD** na pasta do instalador

2. Execute:
   ```bash
   python party_limit_begone_installer.py
   ```

3. Siga as instruções na tela

### Entrada Manual de Caminho

Se o instalador não encontrar o BG3 automaticamente:

**Para Steam (padrão):**
```
C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3
```

**Para Steam (outras unidades):**
```
D:\Steam\steamapps\common\Baldurs Gate 3
E:\SteamLibrary\steamapps\common\Baldurs Gate 3
```

**Para GOG:**
```
C:\Program Files (x86)\GOG Galaxy\Games\Baldurs Gate 3
C:\GOG Games\Baldurs Gate 3
```

## Configuração do Multiplayer

### Passo 1: Configurar o Jogo

1. **Inicie o Baldur's Gate 3**

2. **Vá em:** Menu → Opções → Gameplay

3. **Ative:** "Conexão LAN"

4. **Salve** as configurações

### Passo 2: Escolher o Método de Conexão

#### Método A: Hamachi/Radmin VPN (Mais Fácil)

**Vantagens:**
- ✅ Não precisa mexer no roteador
- ✅ Funciona em qualquer rede
- ✅ Fácil de configurar

**Instalação:**

1. **Download:**
   - Hamachi: https://www.vpn.net/
   - Radmin VPN: https://www.radmin-vpn.com/ (grátis)

2. **Host cria uma rede:**
   - Abra o Hamachi/Radmin
   - Crie uma nova rede
   - Defina nome e senha

3. **Jogadores entram na rede:**
   - Abra o Hamachi/Radmin
   - Entre na rede do host
   - Use nome e senha fornecidos

4. **No jogo:**
   - Host cria a partida multiplayer normalmente
   - Jogadores 1-4 entram pelo código normal
   - Jogadores 5+ também entram pelo código normal
   - Todos devem estar na mesma rede virtual!

#### Método B: IP Direto (Avançado)

**Requisitos:**
- Host precisa saber seu IP público
- Host precisa abrir porta no roteador

**Configuração:**

1. **Descobrir IP público:**
   - Acesse: https://www.whatismyip.com/
   - Anote o número

2. **Abrir porta 23253:**
   
   **No Windows Firewall:**
   ```
   Painel de Controle → Sistema e Segurança → Firewall do Windows
   → Configurações Avançadas → Regras de Entrada → Nova Regra
   → Porta → TCP → 23253 → Permitir conexão
   ```

   **No Roteador** (varia por modelo):
   ```
   1. Acesse o painel do roteador (geralmente 192.168.1.1)
   2. Procure "Port Forwarding" ou "Encaminhamento de Portas"
   3. Adicione regra:
      - Porta Externa: 23253
      - Porta Interna: 23253
      - Protocolo: TCP
      - IP Local: (seu IP na rede local)
   ```

3. **Jogadores 5+ conectam:**
   - No menu multiplayer do BG3
   - Clique em "Código Direto"
   - Digite: `IP_DO_HOST:23253`
   - Exemplo: `203.0.113.1:23253`

### Passo 3: Ordem de Entrada

**IMPORTANTE!** A ordem importa:

1. **Primeiro:** Jogadores de console (máximo 3)
2. **Depois:** Jogadores de PC (1-4)
3. **Por último:** Jogadores 5+ (PC apenas)

**Exemplo com 6 jogadores:**
```
1. Console Player 1 (PS5)
2. Console Player 2 (Xbox)
3. PC Player (Host)
4. PC Player
5. PC Player (via LAN/IP)
6. PC Player (via LAN/IP)
```

### Passo 4: Carregando Saves Existentes

Para continuar um save com mais jogadores:

1. **Crie um novo lobby** (não carregue diretamente)
2. **Todos os jogadores entram** no novo lobby
3. **Inicie um novo jogo** qualquer
4. **Depois de carregar,** pause e carregue o save antigo
5. **Pronto!** Todos continuam no save existente

**Nota:** Isso criará novas cópias de save. Limpe ocasionalmente.

## Solução de Problemas Detalhada

### Python Não Encontrado

**Erro:** `'python' não é reconhecido como comando...`

**Solução:**
1. Instale Python: https://www.python.org/downloads/
2. Durante instalação, **marque "Add Python to PATH"**
3. Reinicie o computador
4. Teste: abra CMD e digite `python --version`

### Arquivos do Mod Não Encontrados

**Erro:** `PartyLimitBegone.pak não encontrado`

**Solução:**
1. Baixe novamente do Nexus Mods
2. Extraia corretamente os arquivos .rar/.zip
3. Coloque na mesma pasta do `instalar.bat`
4. Verifique os nomes dos arquivos (sem espaços extras)

### BG3 Não Encontrado Automaticamente

**Solução:**
1. Encontre manualmente a pasta do BG3:
   - Abra Steam
   - Clique direito em BG3
   - "Gerenciar" → "Procurar arquivos locais"
   - Copie o caminho da barra de endereços

2. Cole o caminho quando solicitado pelo instalador

### Antivírus Bloqueou o Patcher

**Erro:** Windows Defender bloqueia `PartyLimitBegonePatcher.bat`

**Solução:**
1. Isso é um **falso positivo** comum
2. **Adicione exceção:**
   - Windows Security → Proteção contra vírus
   - Configurações de proteção contra vírus
   - Adicionar ou remover exclusões
   - Adicionar exclusão → Pasta
   - Selecione a pasta `bin` do BG3

3. **Execute novamente** o instalador

### Mod Não Aparece no Jogo

**Verificações:**

1. **Arquivo modsettings.lsx existe?**
   - Pressione `Win + R`
   - Digite: `%LOCALAPPDATA%\Larian Studios\Baldur's Gate 3\PlayerProfiles\Public`
   - Procure `modsettings.lsx`

2. **Arquivo .pak está no lugar certo?**
   - Pressione `Win + R`
   - Digite: `%LOCALAPPDATA%\Larian Studios\Baldur's Gate 3\Mods`
   - Procure `PartyLimitBegone.pak`

3. **Reinicie o jogo completamente**

### Não Consigo Conectar Mais de 4 Jogadores

**Verificações:**

1. **Patch foi aplicado?**
   - Vá para: `C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\bin`
   - Procure por `bg3.exe.backup`
   - Se existe, o patch foi aplicado ✅

2. **"Conexão LAN" está ativa?**
   - No jogo: Opções → Gameplay
   - Verifique se está marcado

3. **Todos estão na mesma rede virtual?** (se usando Hamachi)
   - Todos devem aparecer verdes no Hamachi

4. **Porta está aberta?** (se usando IP direto)
   - Teste em: https://www.yougetsignal.com/tools/open-ports/
   - Digite sua porta 23253

### Erro "Acesso Negado" ao Aplicar Patch

**Solução:**
1. Feche o Steam completamente
2. Feche o BG3 se estiver aberto
3. Execute o instalador **como Administrador:**
   - Clique direito em `instalar.bat`
   - "Executar como administrador"

### Jogo Não Inicia Após Patch

**Solução de Emergência:**

1. Restaure o backup:
   ```
   C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\bin\
   ```

2. Delete `bg3.exe`

3. Renomeie `bg3.exe.backup` para `bg3.exe`

4. Verifique integridade dos arquivos no Steam:
   - Steam → Biblioteca
   - Clique direito em BG3
   - Propriedades → Arquivos locais
   - "Verificar integridade dos arquivos"

## Perguntas Frequentes

### O mod funciona com saves de campanha solo?

**Sim!** Você pode continuar qualquer save, mas:
- Novos companheiros só aparecem se houver espaço
- Algumas cutscenes podem ter problemas com 5+ personagens
- Salve frequentemente por precaução

### Posso usar com outros mods?

**Sim!** Party Limit Begone é compatível com a maioria dos mods. Porém:
- Evite mods que também modificam o limite de party
- Use o BG3 Mod Manager para gerenciar ordem de load
- Teste em um save separado primeiro

### O mod funciona em multiplayer crossplay?

**Parcialmente:**
- ✅ 3 jogadores console + host PC
- ✅ PC players 5+ podem se juntar
- ❌ Mais de 3 jogadores console não funciona
- Console players devem entrar primeiro!

### Vou ser banido por usar este mod?

**Não!** O BG3 não tem sistema anti-cheat e:
- Mods são permitidos
- Larian Studios apoia modding
- Este mod só afeta seu jogo local
- Não é trapaça ou hack

### O mod afeta conquistas (achievements)?

**Não** para a maioria das conquistas. Algumas observações:
- Conquistas da Steam/GOG funcionam normalmente
- Algumas conquistas relacionadas a party podem bugar
- Salve antes de tentar conquistas importantes

### Posso desinstalar sem problemas?

**Sim!** Para desinstalar completamente:

1. Remova o patch:
   - Delete `bg3.exe` na pasta `bin`
   - Renomeie `bg3.exe.backup` para `bg3.exe`

2. Remova o mod:
   - Delete `PartyLimitBegone.pak` da pasta Mods
   - Delete ou edite `modsettings.lsx`

3. Seus saves funcionarão normalmente, mas:
   - O jogo voltará ao limite de 4 players
   - Companheiros extras ficarão no camp

### Preciso reinstalar após atualizações do jogo?

**Geralmente sim:**
- Atualizações do BG3 podem sobrescrever o patch
- O mod `.pak` geralmente continua funcionando
- Reaplique apenas o patch multiplayer se necessário

### Quantos jogadores realmente funciona?

**Testado até:**
- ✅ 6 jogadores: Funciona perfeitamente
- ✅ 8 jogadores: Funciona bem
- ⚠️ 10+ jogadores: Funcional mas pode ter bugs
- ❓ 16+ jogadores: Não recomendado (instabilidade)

**Limitações técnicas:**
- Performance depende do hardware do host
- Mais jogadores = mais lag potencial
- Combate pode ficar confuso com 10+ players

### Funciona no Steam Deck?

**Sim, mas requer trabalho extra:**
- Linux/ProtonDB compatível
- Precisa adaptar o instalador para Linux
- Instruções específicas virão em breve

### Posso fazer stream/vídeo usando o mod?

**Sim!** Não há restrições:
- Mencione que está usando mods
- Dê crédito ao criador (Sildur)
- Monetização é permitida
- Link do mod na descrição é apreciado

---

## 🆘 Ainda com Problemas?

Se nada disso resolveu:

1. **Abra uma issue** no GitHub com:
   - Descrição detalhada do problema
   - Capturas de tela
   - Log de erro (se houver)
   - Sistema operacional
   - Versão do Python

2. **Ou consulte:**
   - [Nexus Mods - Seção de Posts](https://www.nexusmods.com/baldursgate3/mods/327?tab=posts)
   - [Reddit - r/BaldursGate3](https://www.reddit.com/r/BaldursGate3/)

---

**Boa sorte e divirta-se! 🎮✨**
