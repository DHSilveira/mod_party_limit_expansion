# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2026-01-03

### Adicionado
- 🎉 Lançamento inicial do instalador automático
- ✨ Detecção automática da instalação do BG3 via registro do Windows
- ✨ Suporte para múltiplos caminhos de instalação (Steam, GOG, drives alternativos)
- ✨ Instalação automática do arquivo .pak do mod
- ✨ Criação automática do arquivo modsettings.lsx
- ✨ Aplicação automática do patch multiplayer
- ✨ Criação automática de backup do executável original
- ✨ Interface colorida no terminal para melhor UX
- ✨ Verificação de requisitos e arquivos necessários
- ✨ Entrada manual de caminho caso detecção automática falhe
- 📝 README.md completo com instruções
- 📝 MANUAL.md com guia detalhado
- 📝 CONTRIBUTING.md para orientar contribuidores
- 📝 LICENSE (MIT)
- 🔧 Script .bat para usuários que não conhecem Python
- 🔧 Arquivo .gitignore configurado
- 🔧 requirements.txt (mesmo sem dependências externas)

### Segurança
- ✅ Validação de caminhos antes de operações de arquivo
- ✅ Verificação de existência de arquivos necessários
- ✅ Tratamento de erros robusto
- ✅ Criação automática de backups antes de modificar executáveis

## [Futuro] - Planejado

### A Adicionar
- [ ] Interface gráfica (GUI) opcional com tkinter
- [ ] Suporte para Epic Games Store
- [ ] Desinstalador automático
- [ ] Verificação de integridade dos arquivos do mod
- [ ] Download automático dos arquivos do Nexus Mods (se possível)
- [ ] Detecção e gerenciamento de outros mods instalados
- [ ] Atualização automática do mod quando nova versão disponível
- [ ] Logs detalhados salvos em arquivo
- [ ] Modo silencioso para instalação automatizada
- [ ] Tradução para inglês e espanhol
- [ ] Suporte para Steam Deck / Linux
- [ ] Instalador portátil (sem necessidade de Python)
- [ ] Verificação de compatibilidade com versão do BG3
- [ ] Restauração de backups via interface

### A Melhorar
- [ ] Detecção mais robusta de instalações do BG3
- [ ] Melhor tratamento de permissões (UAC)
- [ ] Feedback visual durante operações longas
- [ ] Testes automatizados
- [ ] Otimização de performance
- [ ] Documentação em vídeo

---

## Tipos de Mudanças

- `Adicionado` para novas funcionalidades
- `Modificado` para mudanças em funcionalidades existentes
- `Depreciado` para funcionalidades que serão removidas em breve
- `Removido` para funcionalidades removidas
- `Corrigido` para correção de bugs
- `Segurança` para correções de vulnerabilidades

## Links

- [Unreleased]: https://github.com/SEU_USUARIO/party-limit-begone-installer/compare/v1.0.0...HEAD
- [1.0.0]: https://github.com/SEU_USUARIO/party-limit-begone-installer/releases/tag/v1.0.0
