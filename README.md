# LectoClub Backend 📚

Backend da aplicação LectoClub - Um "Letterboxd para livros" desenvolvido como projeto final da disciplina **Desenvolvimento para Dispositivos Móveis** do IFRN, curso de Análise e Desenvolvimento de Sistemas.

## 📖 Sobre o Projeto

O LectoClub é uma plataforma que permite aos usuários catalogar, avaliar e acompanhar suas leituras, inspirado no conceito do Letterboxd para filmes. Este repositório contém a API REST desenvolvida em Django que serve como backend para a aplicação móvel.

## 🚀 Tecnologias Utilizadas

- **Django 5.2.4** - Framework web principal
- **Django REST Framework 3.15.2** - Para criação da API REST
- **Django REST Framework SimpleJWT 5.3.0** - Autenticação via JWT
- **Pillow 10.4.0** - Processamento de imagens

## 🔧 Configuração e Instalação

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/murlokfs/lectoclub-backend.git
cd lectoclub-backend
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

5. **Execute as migrações:**
```bash
python manage.py migrate
```

6. **Crie um superusuário (opcional):**
```bash
python manage.py createsuperuser
```

7. **Execute o servidor de desenvolvimento:**
```bash
python manage.py runserver
```

A API estará disponível em `http://localhost:8000/`

## 📡 Endpoints da API

### Autenticação (`/api/auth/`)

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| POST | `/login/` | Login de usuário | Não |
| POST | `/register/` | Registro de novo usuário | Não |
| POST | `/logout/` | Logout de usuário | Sim |
| POST | `/refresh/` | Renovar token de acesso | Não |
| GET | `/me/` | Dados do usuário atual | Sim |
| GET/PUT/PATCH | `/profile/` | Perfil do usuário | Sim |

### Exemplos de Requisição

**Registro:**
```json
POST /api/auth/register/
{
    "username": "usuario123",
    "full_name": "Nome Completo",
    "email": "usuario@email.com",
    "password": "senha123"
}
```

**Login:**
```json
POST /api/auth/login/
{
    "username": "usuario123",
    "password": "senha123"
}
```

## 🎯 Próximos Recursos (Em Desenvolvimento)

- 📚 **Gestão de livros** - CRUD completo de livros
- ⭐ **Sistema de avaliações** - Avaliações e comentários
- 📋 **Listas de leitura** - Listas personalizadas (lidos, lendo, quero ler)
- 👥 **Sistema social** - Seguir usuários e ver atividades
- 🔍 **Busca avançada** - Filtros por gênero, autor, ano, etc.
- 📈 **Estatísticas** - Metas de leitura e estatísticas pessoais
- 🏷️ **Tags e categorias** - Organização personalizada

## 🧪 Desenvolvimento

### Comandos Úteis

```bash
# Executar testes
python manage.py test

# Criar nova migração
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Acessar shell do Django
python manage.py shell

# Coletar arquivos estáticos
python manage.py collectstatic
```

## 📄 Licença

Este projeto é desenvolvido para fins educacionais como parte do curso de Análise e Desenvolvimento de Sistemas do IFRN.

---

**Status do Projeto:** 🚧 Em desenvolvimento ativo

> Este é um projeto acadêmico em desenvolvimento. Novos recursos e melhorias são adicionados constantemente.