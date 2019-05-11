# TNA Web Portal

Turku Nepali Association is a nonprofit organization with the aim of organizing cultural and social events to promote Nepal and Nepalese community in Finland.

## Requirements

1. [Python 2.7.*](https://www.python.org/downloads/)
2. [Django 1.8](https://docs.djangoproject.com/en/1.10/howto/windows/)
3. [Git](https://git-scm.com/downloads)
4. [Pip](https://pip.pypa.io/en/stable/installing/)
6. Pycharm(Optional) but recommended ide.
7. Sourcetree(Optional)  but recommended.

## Installation

In order to install the `Python, Git, Pip` follow the steps described on their web pages. Links are provided above in the requirements section.

In order to install Pycharm. Its recommended that you use the professional version. In order to get the professional version you need to register yourself at [Jetbrains](https://www.jetbrains.com/shop/eform/students) web page.
`NOTE : Use only your school account normal accounts are not accepted.` Once you are registered you can use the professional version of any jetbrains IDE for free till one year.

## Setup Process

Once you are done with the installation. Follow the steps below to run the application.
 1. Create a seperate folder.
     ```
        mkdir github
    ```
 2. Goto folder location.
     ```
        cd github
    ```
 2. Clone the repository to your folder.
     ```
        git clone  http://git.turkunepal.fi:8888/turkunepal/tnawebportal.git
    ```
    `NOTE : You can use ssh link if you like inorder to avoid the username and password typing all the time.`

 3. Now you can see an extra folder name tnawebportal. Goto the folder.
     ```
        cd tnawebportal
     ```
     
 4. Installing virtual environment is optional(If you dont want to messup with your python versions and sites packages in the system.)
     ```
        Follow the link over here [Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/))
     ```    
 
 5. Activate the virtual environment (ONLY IF YOU ARE USING IT).
      ```
        source venv/bin/activate        
     ``` 
 
 6.  ONLY IF YOU ARE NOT USING VIRTUAL ENVIRONMENT Install the requirements
      ```
        pip install -r requirements.txt
        
        OR
        
        sudo pip install -r requirements.txt (`Use SUDO before if you are installing for all users.`)        
     ``` 

## Running The Application

Having all the steps above done successfully. Now we are ready to run the application.

 1. Goto tnawebportal folder.
     ```
        cd ~/github/tnawebportal (CHECK the location in your pc)
     ```
 2. Activate the virtual environment if you are using it else follow to next step.
     ```
        source venv/bin/activate
     ```
3. Run the application.
     ```
        python manage.py runserver
     ```  
    
4. Your application should be running on port 8000 by default. In order to check it open your web browser and use the below url.
     ```
        http://127.0.0.1:8000/
     ```  

5. Close the server.
     ```
        You can close it by Ctrl+C or just close the terminal.
     ```