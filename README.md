Requirements:
    need MYSQL installed on sysytem  and its service needs to ruuning
        start service 
            in linux    
                sudo service  mysqld start
            in windows
                mysql bin directory needs to aaded in path
                then 
                    mysqld -start

    need python 3 installed                
        in linux 
            sudo apt-get install python3
        in windows
            download from python's website and istall it    

    need pip installed

before:

    first time need to populate movie data
        make sure mysql is runnung

        you need to craete a database mannualy to add movie data in it; 

        open mysql console by command
            #mysql -u root -p
             
                here root is username of mysql and passowrd is blank if you have one then place there

                then mysql console will shown as <mysql>$
                give command 
                >create database movie_db; 

        cd to root of project where get_data_.py file placed

        run file by
            #python get_data_.py



how to run:
    open terminal/cmd

    cd to current directory of this project where requiremet.txt placed
           #pip install -r requirements.txt
    
    cd to my_movie_buckt/
       where you find manage.py and some other folders

           give command      

           if its first time to run project then these 2 command required only first time or after you make any changes in model.py file
                #python manage.py makemigrations
                #python manage.py migrate



            this is required to strat serevr
                #python manage.py 
            by default it start on port 8000 
                to visit open 
                    127.0.0.1:8000 in your browser
                to run on other port 
                    #python manage.py runserver port_number    
                        ex
                            #python manage.py runserver 80    
                            



to access admin panel first need to create admin

command on smae directory where manage.py exist

#python manage.py createsuperuser

    enter username,email and password
                    


*to use this system you need to sugnup
                    

the updated version will available on github   https://github.com/nileshnmahajan/My_movie_bucket

mahajan nilesh
9975720525
nileshnmahajan@gmail.com