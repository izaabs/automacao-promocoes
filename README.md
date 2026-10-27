
# 🛍️ Automação de Monitoramento de Promoções

Projeto desenvolvido em Python para monitorar mensagens de promoções no WhatsApp, identificar produtos de interesse a partir de uma lista de desejos (*wishlist*) e enviar notificações por e-mail quando uma promoção relevante é encontrada.

A proposta é automatizar a identificação de ofertas, reduzir o acompanhamento manual de mensagens e manter um histórico das promoções encontradas.

## 🎯 Objetivos

- Monitorar mensagens de um grupo do WhatsApp Web.
- Identificar produtos cadastrados em uma lista de desejos.
- Extrair preços originais, preços promocionais e cupons.
- Calcular o percentual de desconto.
- Registrar promoções em um histórico local.
- Evitar o registro duplicado de promoções.
- Enviar notificações por e-mail para ofertas identificadas.

## ⚙️ Funcionalidades

- **Monitoramento automatizado:** utiliza Playwright para interagir com o WhatsApp Web.
- **Identificação de produtos:** compara palavras-chave das mensagens com os produtos cadastrados na wishlist.
- **Extração de informações:** identifica preços e cupons promocionais.
- **Cálculo de descontos:** calcula a diferença percentual entre o preço original e o promocional.
- **Histórico de promoções:** armazena os resultados em um arquivo JSON.
- **Prevenção de duplicidade:** verifica se uma promoção já foi registrada.
- **Notificações por e-mail:** utiliza SMTP para enviar alertas sobre novas promoções.

## 🧰 Tecnologias utilizadas

- Python
- Playwright
- python-dotenv
- Expressões regulares (`re`)
- JSON
- SMTP
- Git e GitHub

## 📁 Estrutura do projeto

```text
automacao-promocoes/
├── .env.example
├── .gitignore
├── analisador.py
├── main.py
├── notificacao.py
├── requirements.txt
├── teste_integracao.py
├── teste_whatsapp.py
└── wishlist.json
```

Arquivos gerados durante a execução, como `historico.json` e o perfil persistente do WhatsApp, são mantidos localmente e não fazem parte do repositório.

## 🚀 Instalação e configuração

### 1. Pré-requisitos

- Python instalado.
- Git instalado.
- Conta do Gmail para envio de notificações.
- Acesso ao WhatsApp Web.

### 2. Clone o repositório

```bash
git clone https://github.com/izaabs/automacao-promocoes.git
cd automacao-promocoes
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Instale o navegador do Playwright

```bash
python -m playwright install chromium
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, utilizando o `.env.example` como referência.

Adicione a senha de aplicativo do Gmail:

```env
GMAIL_SENHA=sua_senha_de_aplicativo
```

Substitua o valor de exemplo pela sua senha de aplicativo. Nunca compartilhe ou publique esse arquivo.

> A autenticação do Gmail deve estar configurada para permitir o envio por SMTP. Quando necessário, utilize uma senha de aplicativo, não a senha normal da sua conta.

## 📝 Personalização da wishlist

Os produtos monitorados são definidos no arquivo `wishlist.json`.

Cada produto possui um nome e uma lista de palavras-chave utilizadas na identificação das promoções.

Exemplo:

```json
{
  "produtos": [
    {
      "nome": "Epidrat Calm B5 50ml",
      "palavras_chave": [
        "hidratante facial",
        "epidrat",
        "calm B5",
        "50ml"
      ]
    }
  ]
}
```

Você pode adicionar outros produtos seguindo a mesma estrutura.

## ▶️ Como executar

### Teste de integração

Para testar o processamento de uma mensagem de exemplo:

```bash
python teste_integracao.py
```

### Monitoramento do WhatsApp

Execute:

```bash
python teste_whatsapp.py
```

O navegador será aberto para acessar o WhatsApp Web. Na primeira execução, pode ser necessário escanear o QR Code.

Após acessar o grupo configurado no código, o script verifica periodicamente as mensagens disponíveis e processa as novas mensagens detectadas.

Para encerrar o monitoramento, pressione `Ctrl + C` no terminal.

## 🔄 Fluxo de funcionamento

1. O script acessa o grupo configurado no WhatsApp Web.
2. As mensagens disponíveis são verificadas periodicamente.
3. O analisador compara o conteúdo com as palavras-chave da wishlist.
4. Quando um produto é identificado, são extraídos os preços e o cupom, quando disponíveis.
5. O percentual de desconto é calculado.
6. A promoção é comparada com o histórico para evitar duplicidade.
7. Quando uma nova promoção válida é registrada, uma notificação por e-mail é enviada.

## 🔐 Segurança

- Credenciais são armazenadas em variáveis de ambiente.
- O arquivo `.env` não deve ser enviado ao GitHub.
- O perfil autenticado do WhatsApp deve permanecer local.
- O histórico local de promoções não precisa ser publicado.
- Nunca compartilhe senhas, tokens ou dados de autenticação.

## 🧪 Testes

O projeto inclui um script de teste de integração para verificar o processamento de mensagens e um script para executar o monitoramento pelo WhatsApp Web.

Os resultados podem variar conforme o formato das mensagens, as palavras-chave cadastradas e a disponibilidade do WhatsApp Web.

## 📌 Melhorias futuras

- Aprimorar a identificação de produtos semelhantes.
- Melhorar a extração de preços em diferentes formatos de mensagem.
- Expandir a cobertura de testes automatizados.
- Implementar logs estruturados e tratamento de falhas.
- Aprimorar o gerenciamento do histórico de promoções.
- Explorar formas adicionais de análise e classificação de ofertas.

## 👩‍💻 Autora

Desenvolvido por **izaabs** como projeto de estudo e prática em Python, automação de processos, processamento de texto e integração com serviços externos.

[GitHub: @izaabs](https://github.com/izaabs)
