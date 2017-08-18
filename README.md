# instagram contacts
 
 
_**for production on MySQL db:**_
1. open insta/setting.py and find DATABASES
2. comment existing DATABASES lines and uncomment line below the row that sounds like 
        
        # Uncomment files below to use MySQL db

3. to migrate project use commands:

        python manage.py makemigrations
        python manage.py migrate



There are no information about how to deploy this project