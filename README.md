# Equador Eventos - Site de Promotoria de Eventos

Este é um site desenvolvido em Django para uma empresa de promotoria de eventos no Equador. O site permite gerenciar eventos, serviços, portfólio e conteúdo informativo da empresa.

## Características

- Gerenciamento de eventos (criação, edição, agendamento)
- Catálogo de serviços
- Portfólio de projetos realizados
- Seção sobre a empresa e equipe
- Formulário de contato
- Newsletter
- Calendário de eventos
- Depoimentos de clientes
- Galeria de imagens
- Design responsivo

## Tecnologias Utilizadas

- Django 4.2+
- Python 3.9+
- Bootstrap 5
- SQLite (para desenvolvimento)
- HTML, CSS, JavaScript
- jQuery
- FontAwesome
- Swiper.js (para sliders)
- FullCalendar (para o calendário de eventos)
- FancyBox (para galeria de imagens)

## Requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes do Python)
- virtualenv (recomendado)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/equador-eventos.git
cd equador-eventos
```

2. Crie e ative um ambiente virtual:
```bash
# No Linux/Mac
python -m venv venv
source venv/bin/activate

# No Windows
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados:
```bash
python manage.py migrate
```

5. Crie um superusuário para acessar o admin:
```bash
python manage.py createsuperuser
```

6. Execute o servidor de desenvolvimento:
```bash
python manage.py runserver
```

7. Acesse o site em seu navegador:
```
http://127.0.0.1:8000/
```

8. Acesse o painel administrativo:
```
http://127.0.0.1:8000/admin/
```

## Configurações Iniciais

Após a instalação, você deve configurar os dados básicos da empresa:

1. Acesse o admin do Django
2. Cadastre ao menos um registro em `Configuração do Site`
3. Crie tipos de eventos
4. Crie serviços
5. Configure os banners da página inicial

## Estrutura do Projeto

- `core/`: Aplicação principal com configurações do site e páginas estáticas
- `eventos/`: Aplicação para gerenciamento de eventos
- `contato/`: Aplicação para formulário de contato e newsletter
- `admin_site/`: Personalização do admin do Django
- `templates/`: Templates HTML para todas as páginas
- `static/`: Arquivos estáticos (CSS, JS, imagens)
- `media/`: Arquivos enviados pelos usuários

## Desenvolvimento

Para continuar o desenvolvimento:

1. Personalize os templates de acordo com a identidade visual da empresa
2. Adicione funcionalidades adicionais se necessário
3. Configure um banco de dados mais robusto para produção (PostgreSQL recomendado)
4. Configure o envio de emails
5. Desenvolva testes automatizados

## Produção

Para implantar em produção:

1. Configure um servidor web (Nginx, Apache)
2. Use Gunicorn ou uWSGI como servidor de aplicação
3. Configure um banco de dados PostgreSQL
4. Configure variáveis de ambiente para chaves secretas
5. Configure HTTPS usando Let's Encrypt
6. Configure backups regulares do banco de dados e arquivos de mídia

## Licença

Este projeto está licenciado sob a MIT License.