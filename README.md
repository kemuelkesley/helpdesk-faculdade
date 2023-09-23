# Meu Projeto Django

Este é um projeto Django simples para [descreva brevemente o propósito do projeto].

## Tecnologias Utilizadas

- Python [versão]: [[link para a página oficial do Python]](https://www.python.org/downloads/)
- Django [versão]: [link para a página oficial do Django]
- [Outras tecnologias usadas, se aplicável]

## Instalação

Siga estas etapas para configurar e executar o projeto localmente:

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

   
