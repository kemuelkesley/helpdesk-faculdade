
#
# Project Title: Helpdesk

## Project Name

**Helpdesk** is a ticket management application designed to streamline technical support operations by allowing users to open and close tickets, track equipment installations in condominiums, and record who performed these operations. The application also captures essential data for feeding into a Big Data system to help analyze and improve services.

## Description

The **Helpdesk** project is an application for managing technical support tickets, allowing users to log the opening and closing of tickets. The platform was developed to simplify the tracking of tickets, storing information on who opened and closed them, and monitoring the equipment installed in condominiums. The primary goal is to capture essential data to feed into a Big Data system, helping with data analysis and service improvement.

## Objective

The **Helpdesk** aims to provide a practical solution for managing technical support tickets, automating the logging of ticket openings and closings, with detailed tracking of all operations. Additionally, the application seeks to collect daily usage data to feed into a Big Data system, helping the company generate insights and improve its services.

## History

This project was created to meet the needs of a company looking for an efficient way to centrally manage its technical support tickets. The idea emerged from the demand for an application that not only logged tickets but also captured important data for future improvements and analysis, contributing to building a robust database for Big Data.


## Technologies Used

This project was built using the following technologies:

- **[Python 11](https://www.python.org/)**: Programming language used for the backend.
- **[Django 5.0](https://www.djangoproject.com/)**: Python web framework that facilitates rapid and secure web application development.
- **[HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML/HTML5)**: Structure of the user interface.
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)**: Styling of the user interface.
- **[Bootstrap 5.0](https://getbootstrap.com/)**: CSS framework for responsive design and UI components.
- **[SQL Server](https://www.microsoft.com/sql-server)**: Database used for data storage in the project.


## Screens

| Project Running                                                                                    | 
|----------------------------------------------------------------------------------------------------
|![helpdesk](https://github.com/user-attachments/assets/2e7a9dd1-6eda-4570-9d5b-d5b2a703bced)        |
 

&nbsp;

# Link project

https://www.youtube.com/watch?v=MQ-h_BrEICQ

### 1. Download Python: 

   ```
   https://www.python.org/downloads/
   ```

### 2. Clone the repository or download the zip file:

   ```
   git clone https://github.com/kemuelkesley/helpdesk-faculdade.git
   ```

   - Once downloaded or cloned, unzip the folder to a location of your choice.
    

### 3. Open the Terminal and navigate to the project folder:

   ```   
   cd helpdesk-faculdade
   ```

### 4. In the terminal, install VIRTUALENV:

   ```   
   pip install virtualenv
   ```

### 5. Create a virtual environment:
- With the terminal open in the project folder, run the command:
         
     ```   
     virtualenv env
     or
     python -m venv venv
     ```

### 6. Activate the virtual environment:
   - After creating the *ENV* virtual environment, activate it using the command: 

     ```   
     env\Scripts\Activate
     ```

     - Example of activated virtual environment:
    
       ![image](https://github.com/kemuelkesley/helpdesk-faculdade/assets/79339726/d48738e4-7744-4c64-9730-a151faa5c66a)

### 7. Install the project dependencies:
   - In the project folder with the terminal open, run the command:
  
     ```   
     pip install -r requirements.txt
     ```

### 8. Run the database migrations:

     ```   
     python manage.py migrate
     ```

### 9. Create an administrator account:
   - In the terminal, run the command to create the account to access the system.
   - After executing this command, it will prompt you to create:
   
     - Username
     - Email
     - Password
      
     ```   
     python manage.py createsuperuser
     ```

### 10. Start the development server:

   - Once everything is configured and installed, run the command:    
      
     ```   
     python manage.py runserver
     ```


11. Open your browser and go to http://localhost:8000/ to see the project running.

12. If everything worked correctly, the login page will open. Just enter the admin account you created and the password.


![image](https://github.com/kemuelkesley/helpdesk-faculdade/assets/79339726/a4cffabe-874f-4a2a-8b9e-4dd030f614b4)

   
