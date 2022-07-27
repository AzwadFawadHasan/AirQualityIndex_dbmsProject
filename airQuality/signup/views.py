from django.shortcuts import render
import mysql.connector as sql

emailVar=''
passwordVar=''

# Create your views here.


def signaction(request):
    global em, pwd
    if request.method == "POST":
        mysqlObject = sql.connect(
            host="localhost",
            user="root",
            password ="root",
            database='air'
            )
        cursor = mysqlObject.cursor();

        dataFromForm=request.POST
        for key, value in dataFromForm.items():
            if key =="email":
                emailVar=value;
            if key =="password":
                passwordVar=value;
        saveInDatabase ="insert into users Values('{}','{}')".format(emailVar,passwordVar)
        cursor.execute(saveInDatabase); #executing query
        mysqlObject.commit();#saves info in mysql server
    return render(request, 'signup.html')

    
