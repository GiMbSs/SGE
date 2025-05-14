# 📊 SGE - Sistema de Gestão de Estoque


Um sistema completo para gerenciamento de estoque desenvolvido em Django, com interface moderna e recursos avançados para controle de produtos, fornecedores, entradas e saídas.

## ✨ Funcionalidades Principais

### 🏢 Gestão Empresarial Completa
- **🏷️ Marcas:** Cadastro e gerenciamento de marcas de produtos
- **📁 Categorias:** Organização de produtos em categorias personalizadas
- **📦 Produtos:** Controle de produtos com preços, estoque e detalhes completos
- **🚚 Fornecedores:** Gerenciamento de fornecedores com contatos e informações fiscais

### 📈 Controle de Estoque
- **📥 Entradas:** Registro de entrada de produtos no estoque
- **📤 Saídas:** Controle de saídas com impacto automático no estoque
- **🔄 Atualização automática:** Saldo de estoque atualizado em tempo real

### 📊 Dashboard e Relatórios
- **📊 Métricas de produtos:** Visualização de quantidade, custo e valor do estoque
- **📈 Métricas de vendas:** Acompanhamento de vendas e lucratividade
- **📉 Gráficos interativos:** Análise visual de desempenho em períodos específicos

### 🔒 Segurança e Acessos
- **👤 Controle de permissões:** Diferentes níveis de acesso por usuário
- **🔐 Autenticação segura:** Sistema de login com proteção de rotas
- **🔄 JWT Authentication:** API com autenticação via tokens JWT

## 🛠️ Tecnologias Utilizadas

- ![Django](https://img.shields.io/badge/Django-5.2.1-092E20?style=flat-square&logo=django) - Framework web
- ![DRF](https://img.shields.io/badge/Django%20Rest%20Framework-3.16.0-ff1709?style=flat-square&logo=django) - API REST
- ![JWT](https://img.shields.io/badge/JWT-2.9.0-000000?style=flat-square&logo=json-web-tokens) - Autenticação
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat-square&logo=bootstrap) - Frontend
- ![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat-square&logo=sqlite) - Banco de dados

## Screenshots

![Dashboard do SGE](./_screenshots/1.jpeg)

![Gestão de Produtos](./_screenshots/2.jpeg)

![Controle de Estoque](./_screenshots/3.jpeg)


## 📦 Módulos do Sistema

| Módulo | Descrição | Ícone |
|--------|-----------|-------|
| **Dashboard** | Página inicial com métricas e gráficos | 📊 |
| **Marcas** | Gerenciamento de marcas de produtos | 🏷️ |
| **Categorias** | Organização de produtos em categorias | 📁 |
| **Produtos** | Cadastro e gestão de produtos | 📦 |
| **Fornecedores** | Gerenciamento de fornecedores | 🚚 |
| **Entradas** | Registro de entrada de produtos | 📥 |
| **Saídas** | Controle de saída de produtos | 📤 |

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/ERP_DjangoMaster.git
cd ERP_DjangoMaster

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
# source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Crie um usuário administrador
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

## 📱 Interface do Sistema

O SGE possui uma interface moderna e responsiva, utilizando Bootstrap e ícones Bootstrap Icons. O sistema é projetado com tema escuro para maior conforto visual durante o uso prolongado.

### 🎨 Paleta de Cores
- ![#7d3cd8](https://placehold.co/15x15/7d3cd8/7d3cd8.png) `Azul Primário`
- ![#dc5022](https://placehold.co/15x15/dc5022/dc5022.png) `Vermelho Alerta`
- ![#0799a1](https://placehold.co/15x15/0799a1/0799a1.png) `Verde Sucesso`
- ![#c4c11d](https://placehold.co/15x15/c4c11d/c4c11d.png) `Amarelo Atenção`
- ![#23272b](https://placehold.co/15x15/23272b/23272b.png) `Fundo Escuro`

## 🔌 API REST

O sistema disponibiliza uma API REST completa para integração com outros sistemas.

``` Rotas da API
- Obtenção de token JWT
/api/token/
/api/token/refresh/
/api/token/verify/
-
/api/v1/brands/
/api/v1/categories/
/api/v1/inflows/
/api/v1/outflows/
/api/v1/products/
/api/v1/suppliers/
/api/token/ - Obtenção de token JWT
```

## 📝 Licença

Um projeto @pycodebr.