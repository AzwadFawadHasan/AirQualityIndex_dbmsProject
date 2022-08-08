

from wsgiref.handlers import format_date_time
from django.shortcuts import render

from django.shortcuts import render


import plotly.express as px
import pandas as pd
from django.shortcuts import render, redirect



from django.contrib.auth import login

from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objects as go
import plotly.express as px
import geojson
import urllib

import plotly.figure_factory as ff
import numpy as np

import scipy

import plotly.graph_objects as go
import numpy as np

from urllib.request import urlopen
import json
import plotly.express as px
import pandas as pd

from geojsonio import display
from json import load

import plotly.express as px
import plotly.io as pio

import mysql.connector
import csv
import csv, io
from django.contrib import messages
import sqlalchemy
from urllib3 import HTTPResponse

import csv, io;
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required


from .models import FilesUpload
import plotly.graph_objects as go
from pandas import DataFrame
#pio.renderers.default = 'browser'


# Create your views here.

    #x_data = [0,1,2,3]
    #y_data = [x**2 for x in x_data]
    #plot_div = plot([Scatter(x=x_data, y=y_data,
    #                    mode='lines', name='test',
    #                    opacity=0.8, marker_color='green')],
    #           output_type='div')
    #return render(request, "base/index.html", context={'plot_div': plot_div})
    #
    #import plotly.graph_objects as go

    # Add data

#4.
#A comparison between multiple data sources should be shown using line charts,
#scatterplots, and boxplots, e.g.,


def lineCharts(request):

    #connecting database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="air"
    )
    #conn = mydb;
    #SQL_Query_Dhaka =pd.read_sql_query(
    #    """SELECT time, PM25, division from finalTrainData """,conn
#
    #)
    #df = pd.DataFrame(SQL_Query_Dhaka)
    #fig = go.Figure()
    #unique_division = df.division.unique();
#
    #for u in unique_division:
    #    q = "division=='" +  u +"'"
    #    listOfDivision =df.query(q)
    #    utime = listOfDivision['time']
    #    uAvgPM = listOfDivision['PM25']
    #
    #fig.add_trace(go.Scatter(name=u, x=utime, y=uAvgPM))
    #fig.show();
    mycursor = mydb.cursor()
    mycursor1 = mydb.cursor()
    mycursor2 = mydb.cursor()
    #mycursor3= mydb.cursor()
    #mycursor4= mydb.cursor()
    #mycursor5= mydb.cursor()
    #mycursor6= mydb.cursor()
    #mycursor7= mydb.cursor()
    #mycursor8= mydb.cursor()
    ##mycursor2 = mydb.cursor();

    #mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    #csv_data = csv.reader(open('graphs/csvForLineGraph.csv'))
    #csv_data = csv.reader(open('media/final_train_data(Manipulated).csv'))
    #
    #
    #next(csv_data, None) 
    ##sqlFormula = "INSERT INTO lineCharts(date,avgPM) VALUES (%s, %s)"
    #sqlFormula = "INSERT INTO epaDaily(daily,location,latitude,longitude,median,mean,max,sum,count) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)"
    #sqlFormula = "INSERT INTO finalTrainData(time,PM25,averageTemperature,rainPrecipitation,windSpeed,visibility,cloudCover,relativeHumidity,station, division, organization, season) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
    #
#
    #for row in csv_data:
    #    mycursor.execute(sqlFormula,row)
#
    #close the connection to the database.
    #mydb.commit()
    #adding data to database ends here


    #mycursor.close()
    #sqlFormulaFetch ="SELECT date, avgPM from lineCharts"
    sqlFormulaFetch2 ="SELECT time, PM25 from finalTrainData"
    Dhakasql = "SELECT time, PM25 from finalTrainData where division= 'Dhaka' ";
    Rangpursql = "SELECT time, PM25 from finalTrainData where division= 'Rangpur'  ";
    #Khulna sql = "SELECT time, PM25 from finalTrainData where division= 'Khulna' ";
    #Sylhet sql = "SELECT time, PM25 from finalTrainData where division= 'Syhlet' ";
    #Rajshahi sql = "SELECT time, PM25 from finalTrainData where division= 'Rajshahi' ";
    #Chittagong  sql = "SELECT time, PM25 from finalTrainData where division= 'Chittagong' ";
    #Mymensingh sql = "SELECT time, PM25 from finalTrainData where division= 'Mymensingh' ";
    #Barisal sql = "SELECT time, PM25 from finalTrainData where division= 'Barisal' ";
    #
    

    #myAllData = mycursor.fetchall();
    
    mycursor.execute(sqlFormulaFetch2)
    myAllData = mycursor.fetchall();
    #
    mycursor1.execute(Dhakasql)
    myAllDataDhakasql = mycursor1.fetchall();
#
    mycursor2.execute(Rangpursql)
    myAllDataRangpursql = mycursor2.fetchall();
#
    ##mycursor3.execute(Khulnasql)
    ##myAllDataKhulnasql = mycursor3.fetchall();
##
    ##mycursor4.execute(Syhletsql)
    ##myAllDataSyhletsql = mycursor4.fetchall();
##
    ##mycursor5.execute(Rajshahisql)
    ##myAllDataRajshahisql = mycursor5.fetchall();
##
    ##mycursor6.execute(Chittagongsql)
    ##myAllDataChittagongsql = mycursor6.fetchall();
##
    ##mycursor7.execute(Mymensinghsql)
    ##myAllDataMymensinghsql = mycursor7.fetchall();
##
    ##mycursor8.execute(Barisalsql)
    ##myAllDataBarisalsql = mycursor8.fetchall();
#
#
    allDateData = [];
    allAvgPmData = [];
    allDateDataDhaka = [];
    allAvgPmDataDhaka= [];
#
    allDateDataRangpur= [];
    allAvgPmDataRangpur = [];
#
    ##allDateDataKhulnasql= [];
    ##allAvgPmDataKhulnasql = [];
##
    ##allDateDataSyhletsql = [];
    ##allAvgPmDataSyhletsql = [];
##
    ##allDateDataRajshahisql = [];
    ##allAvgPmDataRajshahisql = [];
##
##
    ##allDateDataChittagongsql = [];
    ##allAvgPmDataChittagongsql = [];
##
##
    ##allDateDataMymensinghsql = [];
    ##allAvgPmDataMymensinghsql = [];
##
    ##allDateDataBarisalsql = [];
    ##allAvgPmDataBarisalsql = [];
#
#
   #
#
    #allDateData2 = [];
    #allAvgPmData2 = [];
#
    #allDateData3 = [];
    #allAvgPmData3 = [];
    #countFlag = 0
    #
    for time, PM25 in myAllData:
            allDateData.append(time)
            allAvgPmData.append(PM25)
    #for time in myAllData:
    #    allDateData.append(time)
    #  
#
    for time, PM25 in myAllDataDhakasql:
        allDateDataDhaka.append(time)
        allAvgPmDataDhaka.append(PM25)
#
    #count = 0;
    #for x in myAllDataDhakasql:
    #    
    #    print(allAvgPmDataDhaka)
    #    count=count+1;
#
    #print("count is ")
    #print(count)
#
    for time, PM25 in myAllDataRangpursql :
        allDateDataRangpur .append(time)
        allAvgPmDataRangpur .append(PM25)
#
    ##for time, PM25 in myAllDataKhulnasql :
    ##    allDateDataKhulnasql.append(time)
    ##    allAvgPmDataKhulnasql.append(PM25)
    ##
    ##for time, PM25 in myAllDataDhakasql:
    ##    allDateDataDhakasql.append(time)
    ##    allAvgPmDataDhakasql.append(PM25)
    ##
    #for time, PM25 in myAllDataSyhletsql:
    #    allDateDataSyhletsql .append(time)
    #    allAvgPmDataSyhletsql .append(PM25)
#
    #for time, PM25 in myAllDataRajshahisql:
    #    allDateDataRajshahisql.append(time)
    #    allAvgPmDataRajshahisql.append(PM25)
    #
    #for time, PM25 in myAllDataChittagongsql :
    #    allDateDataChittagongsql .append(time)
    #    allAvgPmDataChittagongsql .append(PM25)
#
    #for time, PM25 in myAllDataMymensinghsql:
    #    allDateDataMymensinghsql.append(time)
    #    allAvgPmDataMymensinghsql.append(PM25)
    #
    #for time, PM25 in myAllDataBarisalsql:
    #    allDateDataBarisalsql.append(time)
    #    allAvgPmDataBarisalsql.append(PM25)
    #    


    #month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
    #         'August', 'September', 'October', 'November', 'December']
    #high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
    #low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
    #high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
    #low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
    #high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
    #low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]

    #fig = go.Figure()
    #fig2 = go.Figure()
    # Create and style traces
    #fig.add_trace(go.Scatter(x=allDateDataDhaka, y=allAvgPmDataDhaka, name='Dhaka',mode='lines+markers',
                    
    #                         line=dict(color='firebrick', width=4)))
    
    #fig.add_trace(go.Scatter(x=allDateDataRangpur , y=allAvgPmDataRangpur , name = 'Rangpur',
    #                         line=dict(color='royalblue', width=4)))

    #fig.add_trace(go.Scatter(x=allDateDataKhulnasql , y=allDateDataKhulnasql , name='Khulna',
    #                         line=dict(color='green', width=4,
    #                              ) # dash options include 'dash', 'dot', and 'dashdot'
    #))
    #fig.add_trace(go.Scatter(x=allDateDataSyhletsql  , y=allDateDataSyhletsql  , name='Syhlet',
    #                         line=dict(color='black', width=4,
    #                              ) # dash options include 'dash', 'dot', and 'dashdot'
    #))
    #
    #fig.add_trace(go.Scatter(x=allDateDataRajshahisql  , y=allDateDataRajshahisql  , name='Rajshahi',
    #                         line=dict(color='yellow', width=4,
    #                              ) # dash options include 'dash', 'dot', and 'dashdot'
    #))
    #fig.add_trace(go.Scatter(x=allDateDataChittagongsql  , y=allDateDataChittagongsql  , name='Chittagong',
    #                         line=dict(color='pink', width=4,
    #                              ) # dash options include 'dash', 'dot', and 'dashdot'
    #))
    #fig.add_trace(go.Scatter(x=allDateDataMymensinghsql , y=allDateDataMymensinghsql , name='Mymensingh',
    #                         line=dict(color='purple', width=4,
    #                              ) # dash options include 'dash', 'dot', and 'dashdot'
    #))
    #fig.add_trace(go.Scatter(x=allDateDataBarisalsql  , y=allDateDataBarisalsql , name='Barisal ',
    #                         line=dict(color='orange', width=4,
    #                              ) # dash options include 'dash', 'dot', and 'dashdot'
    #))
    ##fig.add_trace(go.Scatter(x=month, y=low_2007, name='Low 2007',
    ##                         line = dict(color='royalblue', width=4, dash='dash')))
    ##fig.add_trace(go.Scatter(x=month, y=high_2000, name='High 2000',
    ##                         line = dict(color='firebrick', width=4, dash='dot')))
    ##fig.add_trace(go.Scatter(x=month, y=low_2000, name='Low 2000',
    ##                         line=dict(color='royalblue', width=4, dash='dot')))

    ## Edit the layout
    #trace0 = go.Scatter(
    #x=allDateDataDhaka,
    #y=allAvgPmDataDhaka,
    #name='Dhaka'
    #)
    #Rangpur = go.Scatter(
    #    x=allDateDataRangpur,
    #    y=allAvgPmDataRangpur,
    #    name='Rangpur'
    #)
    #trace3 = go.Scatter(
    #    x=[3, 4, 5],
    #    y=[1000, 1100, 1200],
    #    yaxis="y3"
    #)
    #data = [Rangpur,trace0, ]
    #
    #fig = go.Figure(data=data)
    #data = {
    #"Date": allDateDataDhaka,
    #"AvgPm": allAvgPmDataDhaka,
    #}
    #
    ##load data into a DataFrame object:
    #df = pd.DataFrame(data)
    #
    #fig = px.line(df, x="Date", y="AvgPm", color='Date')
    #fig.show()

    

    #x1 = np.array(allDateDataDhaka)
    #y1 = np.array(allAvgPmDataDhaka)
#
    #x2 = np.array(allDateDataRangpur)
    #y2 = np.array(allAvgPmDataRangpur)
    #
    #df1 = pd.DataFrame({'name': ['Dhaka']*len(x1),
    #                    'x': x1,
    #                    'y': y1})
    #
    #df2 = pd.DataFrame({'name': ['Rangpur']*len(x2),
    #                    'x': x2,
    #                    'y': y2})
    #
    #df = pd.concat([df1, df2])
    #
    #fig = px.line(df, x = 'x', y = 'y', color = 'name', markers = True)
    #fig.show()
    #

    #fig.update_layout(title='Date vs avg PM 2.5',
    #                  xaxis_title='Date',
    #                  yaxis_title='avg Pm 2.5')
    #fig.show()#media\csvForLineGraph.csv
    #fig = go.Figure();
    #df = pd.concat([pd.DataFrame({"day":range(50),"avg_spending":np.random.randint(1,17,50)}).assign(type=type) for type in ["one","two"]])
#
    #fig = px.line(df, x="day", y="avg_spending", color="type")
    #fig.update_layout(yaxis={"dtick":1,"range":[0,17]},margin={"t":0,"b":0},height=500)
    #fig.add_trace(
    #    go.Scatter(x=allDateDataDhaka, y=allAvgPmDataDhaka, name='Dhaka')
    #)
    #fig.add_trace(
    #    go.Scatter(x=allDateDataRangpur, y=allAvgPmDataRangpur, name='Rangpur')
    #)
    #fig.show();

    engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/air')

    #df = pd.read_sql_table("finaltraindata", engine, columns=['time', 'PM25', 'division'])
    query ='''
    SELECT time, PM25 from finalTrainData where division = 'Dhaka'  
    
    '''
    queryRangpur ='''
    SELECT time, PM25 from finalTrainData where division = 'Rangpur'
    
    '''
    queryKhulna  ='''
    SELECT time, PM25 from finalTrainData where division = 'Khulna'
    
    '''
    querySylhet  ='''
    SELECT time, PM25 from finalTrainData where division = 'Sylhet'
    
    '''

    queryRajshahi ='''
    SELECT time, PM25 from finalTrainData where division = 'Rajshahi'
    
    '''
    queryChittagong ='''
    SELECT time, PM25 from finalTrainData where division = 'Chittagong'
    
    '''

    queryMymensingh ='''
    SELECT time, PM25 from finalTrainData where division = 'Mymensingh'
    
    '''

    queryBarisal ='''
    SELECT time, PM25 from finalTrainData where division = 'Barisal'
    
    '''
    
    df = pd.read_sql_query(query, engine)
   
    
    df2 = pd.read_sql_query(queryRangpur, engine)
    df3 = pd.read_sql_query(queryKhulna, engine)
    df4 = pd.read_sql_query(querySylhet, engine)
    df5 = pd.read_sql_query(queryRajshahi, engine)
    df6 = pd.read_sql_query(queryChittagong, engine)
    df7 = pd.read_sql_query(queryMymensingh, engine)
    df8 = pd.read_sql_query(queryBarisal, engine)
    #dhaka_df = pd.pivot_table(df, values=['time','PM25'], columns='division')

    
    #display(df)
    
    #fig = px.line(df, x="time", y="PM25")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["time"], y=df["PM25"], name="Dhaka", mode="lines"))
    fig.add_trace(go.Scatter(x=df["time"], y=df2["PM25"], name="Rangpur", mode="lines",))
    fig.add_trace(go.Scatter(x=df["time"], y=df3["PM25"], name="Khulna", mode="lines",))
    fig.add_trace(go.Scatter(x=df["time"], y=df4["PM25"], name="Sylhet", mode="lines",))
    fig.add_trace(go.Scatter(x=df["time"], y=df5["PM25"], name="Rajshahi", mode="lines",))
    fig.add_trace(go.Scatter(x=df["time"], y=df6["PM25"], name="Chittagong", mode="lines",))
    fig.add_trace(go.Scatter(x=df["time"], y=df7["PM25"], name="Mymensingh", mode="lines",))
    fig.add_trace(go.Scatter(x=df["time"], y=df8["PM25"], name="Barisal", mode="lines",))

    fig.update_layout(
    title="avgpm25 vs time", xaxis_title="Time", yaxis_title="AVG PM 25"
    )
    
    #traces = [go.Scatter(
    #    x= dhaka_df.columns,
    #    y =dhaka_df.loc[rowname],
    #    mode= 'markers+lines',
    #    name = rowname
#
    #)for rowname in dhaka_df.index]
    fig.update_yaxes(autorange=True)
    fig.update_layout(autotypenumbers='convert types')
#
    #figure = go.Figure(data=traces, layout=layout)
    fig.show()
    return render(request, 'graphs/lineCharts.html')








def scatterPlotWithLineGraph(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="air"
    )
#select daily, location from epadaily where daily between '1/1/2017' and '12/31/2017'

#inserting data into purpleair table in the database
    #mycursor = mydb.cursor();
    #csv_data_purpleAir = csv.reader(open('media/purpleair_daily(Manipulated).csv'))
    #next(csv_data_purpleAir,None)
    #sqlInsertFormula = "INSERT INTO purpleair(daily,location,latitude, longitude, median, mean, max, sum, count) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)"
    #for row in csv_data_purpleAir:
    #    mycursor.execute(sqlInsertFormula, row)
    #mydb.commit();


    #engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/air')
    epaMean2017Query ='''
    SELECT daily,mean,  location from epadaily where daily LIKE "%2017";
    '''
    aqaMean2017Query='''
    SELECT daily,mean,location from epadaily where daily LIKE "%2017";
    
    '''

    dfEpaMean2017 = pd.read_sql(epaMean2017Query,con=mydb)
    #fig= px.scatter(dfEpaMean2017, x=dfEpaMean2017["mean"], y=aqaMean2017Query["mean"], name="2017")
    df = px.data.tips()
    fig = px.scatter(df, x="total_bill", y="tip", facet_col="smoker", color="sex", trendline="ols")
    fig.show()

    results = px.get_trendline_results(fig)
    print(results)
    #results.query("sex == 'Male' and smoker == 'Yes'").px_fit_results.iloc[0].summary()
    #this uses statmodels 
    # to install
    #python -m pip install statsmodels 
    return render(request, "graphs/multipleBoxPlot.html")





#pm25 vs year (catagorized by districts)
def lineChartsWithDots(request):



    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="air"
    )
    conn = mydb;
    avgpm25for2017Dhaka =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2017" AND division= "Dhaka"; 
        """,conn
    )
    avgpm25for2018Dhaka =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2018" AND division= "Dhaka"; 
        """,conn
    )
    avgpm25for2019Dhaka =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2019" AND division= "Dhaka"; 
        """,conn
    )
    avgpm25for2020Dhaka =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2020" AND division= "Dhaka"; 
        """,conn
    )
    avgpm25for2021Dhaka =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2021" AND division= "Dhaka"; 
        """,conn
    )


    DhakaAvgPM25For2017Value=avgpm25for2017Dhaka['AVG(PM25)'][0]
    DhakaAvgPM25For2018Value=avgpm25for2018Dhaka['AVG(PM25)'][0]
    DhakaAvgPM25For2019Value=avgpm25for2019Dhaka['AVG(PM25)'][0]
    DhakaAvgPM25For2020Value=avgpm25for2020Dhaka['AVG(PM25)'][0]
    DhakaAvgPM25For2021Value=avgpm25for2021Dhaka['AVG(PM25)'][0]

    
    
    print("dhaka 2017 ",DhakaAvgPM25For2017Value)
    print("\ndhaka 2018 ",DhakaAvgPM25For2018Value)
    print("\ndhaka 2019 ",DhakaAvgPM25For2019Value)
    print("\ndhaka 2020 ",DhakaAvgPM25For2020Value)
    print("\ndhaka 2021 ",DhakaAvgPM25For2021Value)
   
    #for Rangpur
    avgpm25for2017Rangpur =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2017" AND division= "Rangpur"; 
        """,conn
    )
    avgpm25for2018Rangpur =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2018" AND division= "Rangpur"; 
        """,conn
    )
    avgpm25for2019Rangpur =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2019" AND division= "Rangpur"; 
        """,conn
    )
    avgpm25for2020Rangpur =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2020" AND division= "Rangpur"; 
        """,conn
    )
    avgpm25for2021Rangpur =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2021" AND division= "Rangpur"; 
        """,conn
    )

    RangpurAvgPM25For2017Value=avgpm25for2017Rangpur['AVG(PM25)'][0]
    RangpurAvgPM25For2018Value=avgpm25for2018Rangpur['AVG(PM25)'][0]
    RangpurAvgPM25For2019Value=avgpm25for2019Rangpur['AVG(PM25)'][0]
    RangpurAvgPM25For2020Value=avgpm25for2020Rangpur['AVG(PM25)'][0]
    RangpurAvgPM25For2021Value=avgpm25for2021Rangpur['AVG(PM25)'][0]


    #for Khulna
    avgpm25for2017Khulna =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2017" AND division= "Khulna"; 
        """,conn
    )
    avgpm25for2018Khulna =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2018" AND division= "Khulna"; 
        """,conn
    )
    avgpm25for2019Khulna =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2019" AND division= "Khulna"; 
        """,conn
    )
    avgpm25for2020Khulna =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2020" AND division= "Khulna"; 
        """,conn
    )
    avgpm25for2021Khulna =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2021" AND division= "Khulna"; 
        """,conn
    )

    KhulnaAvgPM25For2017Value=avgpm25for2017Khulna['AVG(PM25)'][0]
    KhulnaAvgPM25For2018Value=avgpm25for2018Khulna['AVG(PM25)'][0]
    KhulnaAvgPM25For2019Value=avgpm25for2019Khulna['AVG(PM25)'][0]
    KhulnaAvgPM25For2020Value=avgpm25for2020Khulna['AVG(PM25)'][0]
    KhulnaAvgPM25For2021Value=avgpm25for2021Khulna['AVG(PM25)'][0]
    
     #for Syhlet
    avgpm25for2017Syhlet =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2017" AND division= "Sylhet"; 
        """,conn
    )
    avgpm25for2018Syhlet =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2018" AND division= "Sylhet"; 
        """,conn
    )
    avgpm25for2019Syhlet =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2019" AND division= "Sylhet"; 
        """,conn
    )
    avgpm25for2020Syhlet =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2020" AND division= "Sylhet"; 
        """,conn
    )
    avgpm25for2021Syhlet =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2021" AND division= "Sylhet"; 
        """,conn
    )
    SyhletAvgPM25For2017Value=avgpm25for2017Syhlet['AVG(PM25)'][0]
    SyhletAvgPM25For2018Value=avgpm25for2018Syhlet['AVG(PM25)'][0]
    SyhletAvgPM25For2019Value=avgpm25for2019Syhlet['AVG(PM25)'][0]
    SyhletAvgPM25For2020Value=avgpm25for2020Syhlet['AVG(PM25)'][0]
    SyhletAvgPM25For2021Value=avgpm25for2021Syhlet['AVG(PM25)'][0]

    print("  Shylet 2017 ",SyhletAvgPM25For2017Value)
    print("\nShylet 2018 ",SyhletAvgPM25For2018Value)
    print("\nShylet 2019 ",SyhletAvgPM25For2019Value)
    print("\nShylet 2020 ",SyhletAvgPM25For2020Value)
    print("\nShylet 2021 ",SyhletAvgPM25For2021Value)
    
     #for Rajshahi
    avgpm25for2017Rajshahi =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2017" AND division= "Rajshahi"; 
        """,conn
    )
    avgpm25for2018Rajshahi =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2018" AND division= "Rajshahi"; 
        """,conn
    )
    avgpm25for2019Rajshahi =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2019" AND division= "Rajshahi"; 
        """,conn
    )
    avgpm25for2020Rajshahi =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2020" AND division= "Rajshahi"; 
        """,conn
    )
    avgpm25for2021Rajshahi =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2021" AND division= "Rajshahi"; 
        """,conn
    )

    RajshahiAvgPM25For2018Value=avgpm25for2018Rajshahi['AVG(PM25)'][0]
    RajshahiAvgPM25For2019Value=avgpm25for2019Rajshahi['AVG(PM25)'][0]
    RajshahiAvgPM25For2020Value=avgpm25for2020Rajshahi['AVG(PM25)'][0]
    RajshahiAvgPM25For2017Value=avgpm25for2017Rajshahi['AVG(PM25)'][0]
    RajshahiAvgPM25For2021Value=avgpm25for2021Rajshahi['AVG(PM25)'][0]
    
     #for Chittagong
  
    avgpm25for2017Chittagong =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2017" AND division= "Chittagong"; 
        """,conn
    )

    avgpm25for2018Chittagong =pd.read_sql_query(
            """
            select AVG(PM25) from finaltraindata where time Like "%2018" AND division= "Chittagong"; 
            """,conn
        )

    avgpm25for2019Chittagong =pd.read_sql_query(
            """
            select AVG(PM25) from finaltraindata where time Like "%2019" AND division= "Chittagong"; 
            """,conn
        )

    avgpm25for2020Chittagong =pd.read_sql_query(
            """
            select AVG(PM25) from finaltraindata where time Like "%2020" AND division= "Chittagong"; 
            """,conn
        )
    avgpm25for2021Chittagong =pd.read_sql_query(
            """
            select AVG(PM25) from finaltraindata where time Like "%2021" AND division= "Chittagong"; 
            """,conn
        )
    ChittagongAvgPM25For2018Value=avgpm25for2018Chittagong['AVG(PM25)'][0]
    ChittagongAvgPM25For2019Value=avgpm25for2019Chittagong['AVG(PM25)'][0]
    ChittagongAvgPM25For2020Value=avgpm25for2020Chittagong['AVG(PM25)'][0]
    ChittagongAvgPM25For2017Value=avgpm25for2017Chittagong['AVG(PM25)'][0]
    ChittagongAvgPM25For2021Value=avgpm25for2021Chittagong['AVG(PM25)'][0]

     #for Mymensingh
  
    avgpm25for2017Mymensingh =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2017" AND division= "Mymensingh"; 
        """,conn
    )
    avgpm25for2018Mymensingh =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2018" AND division= "Mymensingh"; 
        """,conn
    )
    avgpm25for2019Mymensingh =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2019" AND division= "Mymensingh"; 
        """,conn
    )
    avgpm25for2020Mymensingh =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2020" AND division= "Mymensingh"; 
        """,conn
    )
    avgpm25for2021Mymensingh =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2021" AND division= "Mymensingh"; 
        """,conn
    )

    MymensinghAvgPM25For2018Value=avgpm25for2018Mymensingh['AVG(PM25)'][0]
    MymensinghAvgPM25For2019Value=avgpm25for2019Mymensingh['AVG(PM25)'][0]
    MymensinghAvgPM25For2020Value=avgpm25for2020Mymensingh['AVG(PM25)'][0]
    MymensinghAvgPM25For2017Value=avgpm25for2017Mymensingh['AVG(PM25)'][0]
    MymensinghAvgPM25For2021Value=avgpm25for2021Mymensingh['AVG(PM25)'][0]

     #for Barisal
  
    avgpm25for2017Barisal =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2017" AND division= "Barishal"; 
        """,conn
    )
    avgpm25for2018Barisal =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2018" AND division= "Barishal"; 
        """,conn
    )
    avgpm25for2019Barisal =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2019" AND division= "Barishal"; 
        """,conn
    )
    avgpm25for2020Barisal =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2020" AND division= "Barishal"; 
        """,conn
    )
    avgpm25for2021Barisal =pd.read_sql_query(
        """
        select AVG(PM25) from finaltraindata where time Like "%2021" AND division= "Barishal"; 
        """,conn
    )
    BarisalAvgPM25For2018Value=avgpm25for2018Barisal['AVG(PM25)'][0]
    BarisalAvgPM25For2019Value=avgpm25for2019Barisal['AVG(PM25)'][0]
    BarisalAvgPM25For2020Value=avgpm25for2020Barisal['AVG(PM25)'][0]
    BarisalAvgPM25For2017Value=avgpm25for2017Barisal['AVG(PM25)'][0]
    BarisalAvgPM25For2021Value=avgpm25for2021Barisal['AVG(PM25)'][0]








    engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/air')

    #df = pd.read_sql_table("finaltraindata", engine, columns=['time', 'PM25', 'division'])
    query ='''
    select AVG(PM25) from finaltraindata where time Like "%2017" AND division= "Dhaka"; 
    
    '''
    queryRangpur ='''
    SELECT time, PM25 from finalTrainData where division = 'Rangpur'
    
    '''
    queryKhulna  ='''
    SELECT time, PM25 from finalTrainData where division = 'Khulna'
    
    '''
    querySylhet  ='''
    SELECT time, PM25 from finalTrainData where division = 'Sylhet'
    
    '''

    queryRajshahi ='''
    SELECT time, PM25 from finalTrainData where division = 'Rajshahi'
    
    '''
    queryChittagong ='''
    SELECT time, PM25 from finalTrainData where division = 'Chittagong'
    
    '''

    queryMymensingh ='''
    SELECT time, PM25 from finalTrainData where division = 'Mymensingh'
    
    '''

    queryBarisal ='''
    SELECT time, PM25 from finalTrainData where division = 'Barisal'
    
    '''
    
    
    
    df2 = pd.read_sql_query(queryRangpur, engine)
    df3 = pd.read_sql_query(queryKhulna, engine)
    df4 = pd.read_sql_query(querySylhet, engine)
    df5 = pd.read_sql_query(queryRajshahi, engine)
    df6 = pd.read_sql_query(queryChittagong, engine)
    df7 = pd.read_sql_query(queryMymensingh, engine)
    df8 = pd.read_sql_query(queryBarisal, engine)

    DhakaAvgPM25For2017Value=avgpm25for2017Dhaka['AVG(PM25)'][0]
    DhakaAvgPM25For2018Value=avgpm25for2018Dhaka['AVG(PM25)'][0]
    DhakaAvgPM25For2019Value=avgpm25for2019Dhaka['AVG(PM25)'][0]
    DhakaAvgPM25For2020Value=avgpm25for2020Dhaka['AVG(PM25)'][0]
    DhakaAvgPM25For2021Value=avgpm25for2021Dhaka['AVG(PM25)'][0]
    
    dict1={
        "YEAR":['2017','2018','2019','2020','2021'],
        "AvgPM25":[DhakaAvgPM25For2017Value, DhakaAvgPM25For2018Value, DhakaAvgPM25For2019Value, DhakaAvgPM25For2020Value, DhakaAvgPM25For2021Value]
    }

    dhakaDf=pd.DataFrame(dict1);

    dict1={
        "YEAR":['2017','2018','2019','2020','2021'],
        "AvgPM25":[RangpurAvgPM25For2017Value,RangpurAvgPM25For2018Value, RangpurAvgPM25For2019Value, RangpurAvgPM25For2020Value, RangpurAvgPM25For2021Value]
    }

    RangpurDf=pd.DataFrame(dict1);
    
    #dict2={
    #    "YEAR":['2017','2018','2019','2020','2021'],
    #    "division":["Dhaka","Rangpur","Khulna","Syhlet","Rajshahi","Chittagong","Mymensingh","Barisal"],
    #    "AvgPM25":[DhakaAvgPM25For2017Value, DhakaAvgPM25For2018Value, DhakaAvgPM25For2019Value, DhakaAvgPM25For2020Value, DhakaAvgPM25For2021Value]
    #}

    dict1={
        "YEAR":['2017','2018','2019','2020','2021'],
        "AvgPM25":[KhulnaAvgPM25For2017Value,KhulnaAvgPM25For2018Value, KhulnaAvgPM25For2019Value, KhulnaAvgPM25For2020Value, KhulnaAvgPM25For2021Value]
    }

    KhulnaDf=pd.DataFrame(dict1);

    dict1={
        "YEAR":['2017','2018','2019','2020','2021'],
        "AvgPM25":[SyhletAvgPM25For2017Value,SyhletAvgPM25For2018Value, SyhletAvgPM25For2019Value, SyhletAvgPM25For2020Value, SyhletAvgPM25For2021Value]
    }

    SyhletDf=pd.DataFrame(dict1);

    dict1={
        "YEAR":['2017','2018','2019','2020','2021'],
        "AvgPM25":[RajshahiAvgPM25For2017Value,RajshahiAvgPM25For2018Value, RajshahiAvgPM25For2019Value, RajshahiAvgPM25For2020Value, RajshahiAvgPM25For2021Value]
    }

    RajshahiDf=pd.DataFrame(dict1);

    dict1={
        "YEAR":['2017','2018','2019','2020','2021'],
        "AvgPM25":[RajshahiAvgPM25For2017Value,RajshahiAvgPM25For2018Value, RajshahiAvgPM25For2019Value, RajshahiAvgPM25For2020Value, RajshahiAvgPM25For2021Value]
    }

    RajshahiDf=pd.DataFrame(dict1);

    dict1={
        "YEAR":['2017','2018','2019','2020','2021'],
        "AvgPM25":[ChittagongAvgPM25For2017Value,ChittagongAvgPM25For2018Value, ChittagongAvgPM25For2019Value, ChittagongAvgPM25For2020Value, ChittagongAvgPM25For2021Value]
    }

    ChittagongDf=pd.DataFrame(dict1);

    dict1={
        "YEAR":['2017','2018','2019','2020','2021'],
        "AvgPM25":[MymensinghAvgPM25For2017Value,MymensinghAvgPM25For2018Value, MymensinghAvgPM25For2019Value, MymensinghAvgPM25For2020Value, MymensinghAvgPM25For2021Value]
    }

    MymensinghDf=pd.DataFrame(dict1);

    
    dict1={
        "YEAR":['2017','2018','2019','2020','2021'],
        "AvgPM25":[BarisalAvgPM25For2017Value,BarisalAvgPM25For2018Value, BarisalAvgPM25For2019Value, BarisalAvgPM25For2020Value, BarisalAvgPM25For2021Value]
    }

    BarisalDf=pd.DataFrame(dict1);

    
    #display(df)
    fig = go.Figure()
    #fig2 = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=dhakaDf["YEAR"], y=dhakaDf["AvgPM25"], name='Dhaka',mode='lines'))
    fig.add_trace(go.Scatter(x=RangpurDf["YEAR"], y=RangpurDf["AvgPM25"], name='Rangpur',mode='lines'))
    fig.add_trace(go.Scatter(x=KhulnaDf["YEAR"], y=KhulnaDf["AvgPM25"], name='Khulna',mode='lines'))
    fig.add_trace(go.Scatter(x=SyhletDf["YEAR"], y=SyhletDf["AvgPM25"], name='Syhlet',mode='lines'))
    fig.add_trace(go.Scatter(x=RajshahiDf["YEAR"], y=RajshahiDf["AvgPM25"], name='Rajshahi',mode='lines'))
    fig.add_trace(go.Scatter(x=ChittagongDf["YEAR"], y=ChittagongDf["AvgPM25"], name='Chittagong',mode='lines'))
    fig.add_trace(go.Scatter(x=MymensinghDf["YEAR"], y=MymensinghDf["AvgPM25"], name='Mymensingh',mode='lines'))
    fig.add_trace(go.Scatter(x=BarisalDf["YEAR"], y=BarisalDf["AvgPM25"], name='Barisal',mode='lines'))
    

    fig.update_layout(
    title="avgpm25 vs time", xaxis_title="Time", yaxis_title="AVG PM 25"
    )
   
    
    fig.show()
    
    return render(request, "graphs/lineChartsWithDots.html")
    #media\csvForLineGraph.csv
    #Chittagong
    #Mymensingh
    #Barisal

















# box plot for no 4
def multipleBoxPlot(request):
    N = 30     # Number of boxes

    # generate an array of rainbow colors by fixing the saturation and lightness of the HSL
    # representation of colour and marching around the hue.
    # Plotly accepts any CSS color format, see e.g. http://www.w3schools.com/cssref/css_colors_legal.asp.
    c = ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]

    # Each box is represented by a dict that contains the data, the type, and the colour.
    # Use list comprehension to describe N boxes, each with a different colour and with different randomly generated data:
    fig = go.Figure(data=[go.Box(
     y=3.5 * np.sin(np.pi * i/N) + i/N + (1.5 + 0.5 * np.cos(np.pi*i/N)) * np.random.rand(10),
        marker_color=c[i]
        ) for i in range(int(N))])

    # format the layout
    fig.update_layout(
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(zeroline=False, gridcolor='white'),
        paper_bgcolor='rgb(233,233,233)',
        plot_bgcolor='rgb(233,233,233)',
    )

    fig.show()
    return render(request, "graphs/multipleBoxPlot.html")



def multipleLineCharts(request):
    df = px.data.gapminder().query("continent == 'Oceania'")
    fig = px.line(df, x='year', y='lifeExp', color='country', markers=True)
    fig.show()
    return render(request, "graphs/multipleLineCharts.html")





def index2(request):

    x = ['Product A', 'Product B', 'Product C']
    y = [20, 14, 23]
    

    # Use textposition='auto' for direct text
    fig = go.Figure()
    fig.add_trace(
    go.Scatter(
         x=x, y=y
    ))
    fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            text=y,
            textposition='auto',
        )])

    fig.show()
    return render(request, "base/index2.html")


def barChartWithLines(request):
    #bar chart graph with lines
    fig = go.Figure()

    fig.add_trace(
    go.Scatter(
         x=[0, 1, 2, 3, 4, 5],
        y=[1, 0.5, 0.7, -1.2, 0.3, 0.4]
    ))

    fig.add_trace(
    go.Bar(
        x=[0, 1, 2, 3, 4, 5],
        y=[1, 0.5, 0.7, -1.2, 0.3, 0.4]
    ))

    fig.show()
    return render(request, "graphs/barChartWithLines.html")



def index4(request):
    #negative bar chart graph with lines
    fig = go.Figure()

    fig.add_trace(
    go.Scatter(
         x=[0, 1, 2, 3, 4, 5],
          y=[-1, -0.5, -0.7, -1.2, -0.3, -0.4]
    ))

    fig.add_trace(
    go.Bar(
        x=[0, 1, 2, 3, 4, 5],
        y=[-1, -0.5, -0.7, -1.2, -0.3, -0.4]
    ))

    fig.show()
    return render(request, "base/index4.html")


def boxplot(request):
    #negative bar chart graph with lines
    

    df = px.data.tips()

    fig = px.box(df, x="day", y="total_bill", color="smoker")
    fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
    fig.show()
    return render(request, "base/boxplot.html")


def dataDistribution(request):
    #negative bar chart graph with lines
    

    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    x4 = np.random.randn(200) + 4

    # Group data together
    hist_data = [x1, x2, x3, x4]

    group_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=.2)
    fig.show()
    return render(request, "base/dataDistribution.html")




def country(request):
    #with urlopen('https://drive.google.com/file/d/18AwrNB1iest498bqN8Kf3PCKaC25JKl6/view?usp=sharing') as response:
    #    counties = json.load(response)
    #import pandas as pd
    #data = pd.read_json('graphs/bangladesh.geojson')
    #print(data)
    #https://drive.google.com/file/d/18AwrNB1iest498bqN8Kf3PCKaC25JKl6/view?usp=sharing
    #
    #df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
    #                   dtype={"fips": str})
    #
    #
    #
    #fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
    #                           color_continuous_scale="Viridis",
    #                           range_color=(0, 12),
    #                           mapbox_style="carto-positron",
    #                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
    #                           opacity=0.5,
    #                           labels={'unemp':'unemployment rate'}
    #                          )
    #fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    #fig.show()

    bangladeshDistricts = json.load.open('graphs/bangladesh.geojson', 'r')
    bangladeshDistricts['features'][0]

    #with urlopen('https://github.com/realfahimreza/bangladesh-geojson/blob/master/bangladesh.geojson') as response:
    #    counties = json.load(response)
#
    #import pandas as pd
    #df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
    #               dtype={"fips": str})
#
   #
#
    #fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
    #                           range_color=(0, 12),
    #                           color_continuous_scale="Viridis",
    #                           mapbox_style="carto-positron",
    #                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
    #                           opacity=0.5,
    #                           labels={'unemp':'unemployment rate'}
    #                      )
    #fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    #fig.show()
    #return render(request, "graphs/country.html")



def country2(request):
    
    bd_districts=load(open('graphs/bangladesh_geojson_adm2_64_districts_zillas.json','r'))
    df=pd.read_csv("graphs/Districts_of_Bangladesh.csv")
    df.District = df.District.apply(lambda x: x.replace(" District",""))
    district_id_map = {}
    for feature in bd_districts["features"]:
        feature["id"] = feature["id"]
        district_id_map[feature["properties"]["ADM2_EN"]] = feature["id"]
    df['id'] = df.District.apply(lambda x: district_id_map[x])
    df = df.rename(columns={
    'Population (thousands)[28]' : 'Population (thousands)',
    'Area (km2)[28]' : 'Area (km2)' })    

    fig = px.choropleth(
    df,
    locations='id',
    geojson=bd_districts,
    color='Population (thousands)',
    title='Bangladesh Population',
    )
    fig.update_geos(fitbounds="locations", visible=True)
    fig.show()

    

    return render(request, "graphs/country2.html")
    
import csv


###
#def csvUpload(request):
#    if request.method =="POST":
#    
#    #if request.method =="GET":
#    #    return render(request, "graphs/csvUpload.html")
#    ##if request.method == "POST":
#    #    fileUploaded = request.FILES["file"]
#    #    document= FilesUpload.objects.create(file = fileUploaded)
#    #    document.save()
#    #    return HTTPResponse("your file was uploaded")
#    #return render(request, "graphs/csvUpload.html")
# 
#        csv_file = request.FILES['file'];
#   
# 
#        data_set = csv_file.read().decode('UTF-8')    
#        io_string = io.StringIO(data_set)
#        next(io_string)
#        for column in csv.reader(io_string, delimiter=',', quotechar='|'):
#            _, created = FilesUpload.objects.update_or_create(date  = column[0],
#            avgPM = column[1])
#    context = {}
#    return render (request,"graphs/csvUpload.html", context )    
#        
#        
#
#
