
# Helpdesk

## Descrição

O projeto **Helpdesk** é uma aplicação para gestão de chamados técnicos, permitindo o registro de abertura e fechamento de tickets. A plataforma foi desenvolvida para facilitar o acompanhamento de chamados, armazenando informações sobre quem abriu e fechou os chamados, além de monitorar os equipamentos instalados em condomínios. O principal objetivo é capturar dados essenciais para alimentar um sistema de Big Data, ajudando na análise de dados e no aprimoramento dos serviços.

## Objetivo

O objetivo do **Helpdesk** é oferecer uma solução prática para o gerenciamento de chamados técnicos, automatizando o registro de aberturas e fechamentos, com rastreamento detalhado das operações realizadas. Além disso, a aplicação visa coletar dados de uso diário para alimentar um sistema de Big Data, auxiliando na geração de insights para a empresa.

## Histórico

Este projeto foi criado para atender a necessidade de uma empresa que buscava uma maneira eficiente de gerenciar seus chamados de suporte técnico de forma centralizada. A ideia surgiu da demanda por uma aplicação que não apenas registrasse os chamados, mas também capturasse dados importantes para futuros aprimoramentos e análises, contribuindo para a construção de um banco de dados robusto para Big Data.

## Tecnologias Usadas

Este projeto foi construído utilizando as seguintes tecnologias:

- **[Python 11](https://www.python.org/)**: Linguagem de programação usada para o backend.
- **[Django 5.0](https://www.djangoproject.com/)**: Framework web em Python que facilita o desenvolvimento rápido e seguro de aplicações web.
- **[HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML/HTML5)**: Estrutura da interface do usuário.
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)**: Estilização da interface do usuário.
- **[Bootstrap 5.0](https://getbootstrap.com/)**: Framework CSS para design responsivo e componentes de UI.
- **[SQL Server](https://www.microsoft.com/sql-server)**: Banco de dados utilizado para armazenamento de dados no projeto.

1. Baixar o python: 

   ```
   
   https://www.python.org/downloads/
   
   ```


2. Clone o repositório ou baixe o arquivo zipado: 

   ```
   
   git clone https://github.com/kemuelkesley/helpdesk-faculdade.git
   
   ```

   - Depois de baixado ou clonado descompactar a pasta em um local de preferencia sua.
    

   
3. Abra o Terminal e entre na pasta do projeto

   ```   
   cd helpdesk-faculdade
   
   ```

4. No terminal dentro da pasta do projeto instale a VIRTUALENV.

   ```   
   pip install virtualenv
   
   ```

 5. Criar um ambiente virtual
    - Ainda com o terminal aberto dentro da pasta do projeto execute o comando:
      
     ```   
     virtualenv env
     ou
     python -m venv venv
     
     ```

 6. Ativar ambiente virtual
   - Depois de ter criado o ambiene virtual *ENV*, ative usando o comando: 

     ```   
     env\Script\Activate
     
     ```

     - Exemplo do ambiente virtual ativado
    
       ![image](https://github.com/kemuelkesley/helpdesk-faculdade/assets/79339726/d48738e4-7744-4c64-9730-a151faa5c66a)


 7. Baixar as dependencias do projeto
     - Dentro da pasta com o terminal aberto execute o comando:
  
     ```   
     pip install -r requirements.txt
     
     ```


 8. Execute as migrações do banco de dados:
      
     ```   
     python manage.py migrate
     
     ```

 9. Criar conta de administrador

     - Ainda no terminal execute o comando para criar a conta para acessar o sistema.
     - Após executar esse comando ele vai pedir para criar:
   
     - Nome de usuário
     - E-mail
     - Senha
      
     ```   
     python manage.py createsuperuser
     
     ```
     

10. Iniciar o servidor de desenvolvimento

     - Depois de tudo configurado e baixado.
     - Execute o comando:    
      
     ```   
     python manage.py runserver
     
     ```

11. Abra seu navegador e acesse *http://localhost:8000/* para ver o projeto em execução
12. Se tudo deu certo vai abrir a pagina de login é só colocar a *conta de administrador* que você criou e *senha*

    ![image](https://github.com/kemuelkesley/helpdesk-faculdade/assets/79339726/a4cffabe-874f-4a2a-8b9e-4dd030f614b4)

   
