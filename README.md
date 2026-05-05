# apelido-ml
Automação de processos e ferramentas para acessar o apelido oficial do cliente no mercado livre.

# 🔍 Localizador de Nickname ML

Sistema de automação desenvolvido para otimizar a busca de Nicknames do Mercado Livre. O sistema integra os dados do **Shopping de Preços** com a **API do Mercado Livre**, eliminando a necessidade de navegação manual entre múltiplas abas e JSONs.

## 🚀 Como Rodar no Serviço

1.  **Certifique-se de ter o Python instalado** no Windows.
2.  **Abra a pasta `Apelido Ml` no VS Code**.
3.  **Instale as dependências** (bibliotecas) rodando o comando abaixo no terminal do VS Code (`Ctrl + '`):
    pip install -r requirements.txt
    _> Dica: Se o computador tiver restrições, use: `pip install -r requirements.txt --user`_

Inicie a aplicação:
python -m streamlit run app.py

## 🛠️ Configurações e Arquivos

- **app.py**: Código principal com as credenciais de API fixas e lógica de integração.
- **requirements.txt**: Arquivo de dependências contendo `streamlit` e `requests`.
- **Token ML**: O Token configurado no código é estático e possui validade estendida.

## 🐍 Guia de Instalação (Caso necessário)

### 1. Motor do Python (Essencial)

O VS Code é apenas um editor e não instala o Python sozinho. Se o computador não tiver o Python instalado:

- Baixe o instalador oficial em [python.org](https://www.python.org/).
- **IMPORTANTE**: Durante a instalação, marque a caixa **"Add Python to PATH"**.

### 2. Extensão no VS Code

1.  Abra o VS Code e aperte `Ctrl + Shift + X`.
2.  Busque por **"Python"** (desenvolvido pela Microsoft).
3.  Clique em **Install**.

### 3. Selecionar o Interpretador

Se o VS Code não reconhecer o Python automaticamente:

1.  Clique em **"Select Interpreter"** no canto inferior direito da barra de status.
2.  Escolha a versão do Python instalada na lista que aparecer no topo da tela.

---

_Desenvolvido para agilizar processos de Customer Experience e Suporte Técnico._

