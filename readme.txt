# linkedin_auto_app

Bot de automação para LinkedIn — captura descrição da primeira vaga.

---

## Estrutura do projeto:

- linkedin_auto_apply.py  → código principal do bot
- requirements.txt        → dependências para instalar Selenium e WebDriver Manager
- README.txt              → este arquivo (documentação básica)

---

## Requisitos:

- Python 3.11 ou superior (adicionado ao PATH)
- Navegador Google Chrome instalado
- Acesso à internet

---

## Como instalar dependências:

1️⃣ Abra o terminal (cmd ou PowerShell)

2️⃣ Vá para a pasta do projeto:

    cd caminho/para/linkedin_auto_app

3️⃣ Rode o comando:

    pip install -r requirements.txt

---

## Como rodar o bot:

No terminal, estando na pasta do projeto:

    python linkedin_auto_apply.py

---

## Fluxo do bot:

1️⃣ Abre o Chrome e acessa a página de login do LinkedIn
2️⃣ Você faz o login manualmente
3️⃣ Após o login, o bot acessa a página de vagas
4️⃣ Clica na primeira vaga da lista
5️⃣ Captura e exibe a descrição da vaga no terminal
6️⃣ Pausa para você poder inspecionar o navegador (ENTER para fechar o navegador)

---

## Observações importantes:

⚠️ NÃO usar com a conta principal do LinkedIn em larga escala → risco de bloqueio.

⚠️ Este é um bot **para estudo e automação controlada**.

⚠️ LinkedIn muda o layout com frequência → se o bot parar de capturar a descrição, será necessário atualizar o seletor no código:

    CLASS_NAME: "jobs-description-content__text"

---

## Reinstalando em outro computador:

1️⃣ Instalar Python + Chrome
2️⃣ Copiar a pasta linkedin_auto_app para o novo PC
3️⃣ Rodar:

    pip install -r requirements.txt

4️⃣ Executar o bot normalmente.

---

## Contato:

Gepeto GPT + Lucas — automação personalizada 🚀

---

FIM
