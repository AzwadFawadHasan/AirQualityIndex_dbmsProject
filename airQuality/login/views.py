from django.shortcuts import render
import mysql.connector as sql
from .models import Person

emailVar=''
passwordVar=''

# Create your views here.


def loginaction(request):
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
        getFromDatabase ="select * from users where email='{}' and password ='{}'".format(emailVar,passwordVar)
        cursor.execute(getFromDatabase); #executing query
        storingDataFromDbInATuple = (cursor.fetchall())
        adminQuery = "select * from users where email='root@gmail.com' and password ='root'".format(emailVar,passwordVar);
        cursor.execute(adminQuery);
        storingAdminQuery = (cursor.fetchall())
        
        if storingDataFromDbInATuple==():
            return render(request, 'error.html');
        if storingDataFromDbInATuple==(storingAdminQuery):
            return render(request,'adminHomepage.html')
        else:
            return render(request, 'welcome.html');

        
    return render(request, 'login.html')

    
