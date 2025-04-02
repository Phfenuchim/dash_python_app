# 📊 Aplicação de Dashboards com Autenticação

Esta aplicação tem como objetivo disponibilizar dashboards personalizados a partir de um sistema com áreas logadas e não logadas, respeitando a hierarquia de acesso dos usuários.

Foi utilizado um ambiente de desenvolvimento com **Docker Compose** e **venv**, além de um script `init.sql` para a inicialização e testes do banco de dados.

---

## 🚀 Funcionalidades

- Autenticação de usuários com senhas criptografadas
- Controle de acesso baseado em perfis/hierarquias
- Visualização de dashboards dinâmicos e interativos
- Estrutura modular para facilitar manutenção e escalabilidade

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **Python** – Linguagem principal da aplicação
- **Flask / Dash / HTML / DCC** – Criação do serviço web e dashboards
- **Plotly** (`plotly.io`, `plotly.graph_objects`, `plotly.express`) – Criação de gráficos interativos
- **Pandas** – Manipulação e tratamento de dados
- **PyODBC** – Conexão com banco de dados
- **Bcrypt** – Criptografia de senhas
- **dotenv / os** – Gerenciamento de variáveis de ambiente
- **JavaScript** – Ajustes no comportamento do frontend
- **Docker Compose** – Criação de containers para testes com banco de dados
- **init.sql** – Script de inicialização do banco de dados

---

## 📦 Instalação

Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate     # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🐳 Banco de Dados com Docker Compose

Para subir o banco de dados localmente com o script de inicialização (`init.sql`):

```bash
docker-compose up -d
```

Certifique-se de que o `init.sql` está corretamente configurado no volume do container do banco.

---

## ▶️ Como Rodar Localmente

Após instalar as dependências e iniciar o banco de dados:

```bash
python main.py
```

Acesse a aplicação no navegador:

```
http://127.0.0.1:5000
```

---

## 📁 Estrutura do Projeto

```
.
├── app/
│   ├── controllers/
│   │   └── auth_controller.py
│   ├── services/
│   │   └── db_service.py
│   └── templates/
│       ├── base.html
│       ├── home.html
│       └── login.html
├── dash_app/
│   ├── utils/
│   │   └── export_service.py
│   ├── callbacks.py
│   └── layout.py
├── static/
│   └── js/
│       └── fullscreen.js
├── .env.example
├── .gitignore
├── docker-compose.yml
├── init.sql
├── main.py
├── README.md
└── requirements.txt
```
---

## 🧪 Exemplo de Uso

1. Acesse a aplicação e realize o login.
2. O sistema direciona para o dashboard conforme o nível de acesso do usuário.
3. Dashboards interativos exibem os dados de forma personalizada.
4. Cada usuário visualiza apenas os dados permitidos pela sua hierarquia.

---

## 📬 Contato

Dúvidas ou sugestões? Entre em contato via [email@example.com](mailto:email@example.com)

---
