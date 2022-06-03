from django.shortcuts import render
import mysql.connector as sql

fn=''
ln=''
s=''
em=''
pwd=''
#creating variables here as globbal variables
# Create your views here.
def signupaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
    #carried out when user clicks on submit buttion
    #creating an object called m and connecting it to my sql
        m = sql.connect(host="localhost", user="root", passwd="root", database='website')
    #creating a cursor below
        cursor=m.cursor()
    #we will take the user inputs in a variable called d
        d = request.POST

        for key,value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "sex":
                s = value
            if key == "email":
                em= value
            if key == "password":
                pwd = value           
        c = "insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()
    return render(request, 'signupv2.html')   
