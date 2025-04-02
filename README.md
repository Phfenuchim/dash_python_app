# 📊 Aplicação de Dashboards com Autenticação

Esta aplicação tem como objetivo disponibilizar dashboards personalizados a partir de um sistema com áreas logadas e não logadas, respeitando a hierarquia de acesso dos usuários.

Foi utilizado um ambiente de desenvolvimento com **Docker Compose** e **venv**, além de um script `init.sql` para a inicialização e testes do banco de dados.

## 🚀 Funcionalidades

- Autenticação de usuários com senhas criptografadas
- Controle de acesso baseado em perfis/hierarquias
- Visualização de dashboards dinâmicos e interativos
- Estrutura modular para facilitar manutenção e escalabilidade

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
