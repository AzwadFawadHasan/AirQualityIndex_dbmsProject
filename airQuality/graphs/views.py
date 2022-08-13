
from wsgiref.handlers import format_date_time
from django.shortcuts import render
import pymysql
import pandas as pd

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
import csv
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

import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly. graph_objs as go


import pymysql
import pandas as pd
import plotly.graph_objects as go # or 
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go # or plotly.express as px

import pymysql
import dash
import dash_core_components as dcc
import dash_html_components as html











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

    db_name = "air"
    db_host = "localhost"
    db_username = "root"
    db_password = "root"

    try:
        conn=pymysql.connect(host =db_host,
                            port = int(3306),
                            user = db_username,
                            passwd = db_password,
                            db=db_name)
    except e:
            print(e)
    
   
    
    df = pd.read_sql_query("SELECT * FROM epadaily", conn)
    df2 = pd.read_sql_query("SELECT * FROM purpleair", conn)
    df['daily'] = pd.to_datetime(df['daily'])
    df2['daily'] = pd.to_datetime(df2['daily'])


    filtered_df_epa_2017 = df.query("daily > '2016-12-31' and daily  < '2018-1-1'")
    #adding year 2017 as a column to the dataframe
    YEARS =2017
    filtered_df_epa_2017['YEARS']=YEARS
    #print(filtered_df_epa_2017)

    filtered_df_aqa_2017 = df2.query("daily > '2016-12-31' and daily  < '2018-1-1'")

    filtered_df_aqa_2017.rename(columns = {'mean':'aqamean'},inplace = True)
    extracted_col = filtered_df_aqa_2017["aqamean"]
    #rint("column to added from first dataframe to second:")
    #isplay(extracted_col)
    
    filtered_df_epa_2017 = filtered_df_epa_2017.join(extracted_col)



    #for 2018
    
    filtered_df_epa_2018 = df.query("daily > '2017-12-31' and daily  < '2019-1-1'")
    #adding year 2017 as a column to the dataframe
    YEARS =2018
    filtered_df_epa_2018['YEARS']=YEARS
    #print(filtered_df_epa_2018)

    filtered_df_aqa_2018 = df2.query("daily > '2017-12-31' and daily  < '2019-1-1'")

    filtered_df_aqa_2018.rename(columns = {'mean':'aqamean'},inplace = True)
    extracted_col = filtered_df_aqa_2018["aqamean"]
    #rint("column to added from first dataframe to second:")
    #isplay(extracted_col)
    
    filtered_df_epa_2018 = filtered_df_epa_2018.join(extracted_col)
    #2018 ends
    
    #for 2019
    
    
    filtered_df_epa_2019 = df.query("daily > '2018-12-31' and daily  < '2020-1-1'")
    #adding year 2017 as a column to the dataframe
    YEARS =2019
    filtered_df_epa_2019['YEARS']=YEARS
    #print(filtered_df_epa_2018)

    filtered_df_aqa_2019 = df2.query("daily > '2018-12-31' and daily  < '2020-1-1'")

    filtered_df_aqa_2019.rename(columns = {'mean':'aqamean'},inplace = True)
    extracted_col = filtered_df_aqa_2019["aqamean"]
    #rint("column to added from first dataframe to second:")
    #isplay(extracted_col)
    
    filtered_df_epa_2019 = filtered_df_epa_2019.join(extracted_col)
    #2019 ends
    
    #for 2020
    
    
    filtered_df_epa_2020 = df.query("daily > '2019-12-31' and daily  < '2021-1-1'")
    #adding year 2017 as a column to the dataframe
    YEARS =2020
    filtered_df_epa_2020['YEARS']=YEARS
    #print(filtered_df_epa_2018)

    filtered_df_aqa_2020 = df2.query("daily > '2019-12-31' and daily  < '2021-1-1'")

    filtered_df_aqa_2020.rename(columns = {'mean':'aqamean'},inplace = True)
    extracted_col = filtered_df_aqa_2020["aqamean"]
    #rint("column to added from first dataframe to second:")
    #isplay(extracted_col)
    
    filtered_df_epa_2020 = filtered_df_epa_2020.join(extracted_col)
    #2020 ends
    
    #for 2021
    
    
    filtered_df_epa_2021 = df.query("daily > '2020-12-31' and daily  < '2022-1-1'")
    #adding year 2017 as a column to the dataframe
    YEARS =2021
    filtered_df_epa_2021['YEARS']=YEARS
    #print(filtered_df_epa_2018)

    filtered_df_aqa_2021 = df2.query("daily > '2020-12-31' and daily  < '2022-1-1'")

    filtered_df_aqa_2021.rename(columns = {'mean':'aqamean'},inplace = True)
    extracted_col = filtered_df_aqa_2021["aqamean"]
    #rint("column to added from first dataframe to second:")
    #isplay(extracted_col)
    
    filtered_df_epa_2021 = filtered_df_epa_2021.join(extracted_col)
    #2021 ends
    
    
    
    
    color_discrete_map = {'YEARS': 'rgb(255,0,0)', 'YEARS': 'rgb(0,255,0)', 'YEARS': 'rgb(0,0,255)'}
    #color_discrete_map = {'virginica': 'blue', 'setosa': 'red', 'versicolor': 'green'}
    
    fig1 =px.scatter(filtered_df_epa_2017, x=filtered_df_epa_2017['aqamean'], y=filtered_df_epa_2017['mean'],symbol="YEARS", labels= {"x":"EPA_MEAN","y":"AQA_MEAN"})#.update_traces(marker=dict(color='blue'))

    fig2 = px.scatter(filtered_df_epa_2018, x=filtered_df_epa_2018['aqamean'], y=filtered_df_epa_2018['mean'], symbol="YEARS"
                      
                   ).update_traces(marker=dict(color='orange'))
    
    fig3 = px.scatter(filtered_df_epa_2019, x=filtered_df_epa_2019['aqamean'], y=filtered_df_epa_2019['mean'], symbol="YEARS"
                          
                   ).update_traces(marker=dict(color='red'))
    
    fig4 = px.scatter(filtered_df_epa_2020, x=filtered_df_epa_2020['aqamean'], y=filtered_df_epa_2020['mean'], symbol="YEARS"
                          
                   ).update_traces(marker=dict(color='green'))
    
    #fig5 = px.scatter(filtered_df_epa_2021, x=filtered_df_epa_2021['aqamean'], y=filtered_df_epa_2021['mean'], color='YEARS', title='scatterplot',
    #               labels= {"mean":"EPA_MEAN",
    #                        "aqamean":"AQA_MEAN"},
                          
     #              ).update_traces(marker=dict(color='purple'))

    fig = go.Figure(data = fig1.data + fig2.data + fig3.data +fig4.data)
    fig.update_yaxes(autorange=True)
    fig.update_xaxes(autorange=True)
    fig.update_layout(autotypenumbers='convert types')
    #@fig.update_layout(title_x=0)
    #fig.update_layout(margin_autoexpand=False)
    fig.update_traces(marker=dict(
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                 selector=dict(mode='markers'))
   # fig.update_title='scatterplot',
     #              labels= {"mean":"EPA_MEAN",
    #                        "aqamean":"AQA_MEAN"},#color_discrete_map=color_discrete_map
    
    
    
    
    #fig.update_layout(colorscale=dict(...))
    #fig.update_layout(title="scatterplot",  labels={'x':'t', 'y':'cos(t)'})
    
                  #xaxis_range=[-1,4], yaxis_range=[len(set(namestems)),-1],
                 # margin=dict(b=0,r=0), xaxis_side="top", height=1400, width=400)
    fig.update_layout(title_text="epa vs aqa mean")
    fig.update_layout(title_xanchor="auto")
    fig.update_xaxes(title_text='AQA_MEAN')
    fig.update_yaxes(title_text='EPA_MEAN')
    
    #fig.update_layout()
    
    #fig.update_layout(showlegend=True)
    
    
    fig.show()

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
   

















# box plot for no 4
def multipleBoxPlot(request):
    db_name = "air"
    db_host = "localhost"
    db_username = "root"
    db_password = "root"

    try:
        conn=pymysql.connect(host =db_host,
                            port = int(3306),
                            user = db_username,
                            passwd = db_password,
                            db=db_name)
    except e:
            print(e)
    
   
    
    df = pd.read_sql_query("SELECT * FROM finaltraindata", conn)
    df1 = pd.read_sql_query("SELECT * FROM epadaily", conn)
    df2 = pd.read_sql_query("SELECT * FROM purpleair", conn)

    df['time'] = pd.to_datetime(df['time'])
    df1['daily'] = pd.to_datetime(df1['daily'])
    df2['daily'] = pd.to_datetime(df2['daily'])

    trace0 = go.Box(
    y=df['PM25'],
    name = 'finaltraindata'

    )
    trace1 = go.Box(
        y=df1['mean'],
        name = 'epadaily'

    )
    trace2 = go.Box(
        y=df2['mean'],
        name = 'purpletrain'

    )
    data = [trace0, trace1,trace2]
    layout =go.Layout(title="Boxplot")
    fig = go.Figure(data=data, layout=layout)


    fig.update_layout(autotypenumbers='convert types')
    #fig.update_layout(yaxis_range=[-4,400])
    #fig.update_yaxes(range = [0,400])
    fig.show()
    pyo.plot(fig)



    
    return render(request, "graphs/multipleBoxPlot.html")













def multipleLineCharts(request):
    db_name = "air"
    db_host = "localhost"
    db_username = "root"
    db_password = "root"

    try:
        conn=pymysql.connect(host =db_host,
                            port = int(3306),
                            user = db_username,
                            passwd = db_password,
                            db=db_name)
    except e:
            print(e)
    #Division-Wise daily AQI data visualization using line charts, e.g.
    df = pd.read_sql_query("SELECT * FROM finaltraindata", conn)
    df1 = pd.read_sql_query("SELECT * FROM purpleair", conn)
    df2 = pd.read_sql_query("SELECT * FROM epadaily", conn)

    df['time'] = pd.to_datetime(df['time'])
    df.PM25 = df.PM25.astype(float)

    df1['daily'] = pd.to_datetime(df1['daily'])
    df2['daily'] = pd.to_datetime(df2['daily'])
    newdfDhaka = df.loc[df['division'] =="Dhaka"]
    newdfDhaka.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    newdfDhakaMean =  newdfDhaka['PM25'].mean()
    newdfDhaka = df.loc[df['division'] =="Dhaka"]
    newdfDhaka.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    newdfDhakaMean =  newdfDhaka['PM25'].mean()

    newdf_Rangpur = df.loc[df['division'] =="Rangpur"]
    newdf_Rangpur.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    newdf_RangpurMean =  newdf_Rangpur['PM25'].mean()

    newdf_Khulna = df.loc[df['division'] =="Khulna"]
    newdf_Khulna.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    newdf_KhulnaMean =  newdf_Khulna['PM25'].mean()

    newdf_Sylhet = df.loc[df['division'] =="Sylhet"]
    newdf_Sylhet.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    newdf_SylhetMean =  newdf_Sylhet['PM25'].mean()

    newdf_Rajshahi = df.loc[df['division'] =="Rajshahi"]
    newdf_Rajshahi.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    newdf_RajshahiMean =  newdf_Rajshahi['PM25'].mean()

    newdf_Barishal = df.loc[df['division'] =="Barishal"]
    newdf_Barishal.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    newdf_BarishalMean =  newdf_Barishal['PM25'].mean()

    newdf_Chittagong = df.loc[df['division'] =="Chittagong"]
    newdf_Chittagong.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    newdf_ChittagongMean =  newdf_Chittagong['PM25'].mean()

    newdf_Mymensingh = df.loc[df['division'] =="Mymensingh"]
    newdf_Mymensingh.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    newdf_MymensinghMean =  newdf_Mymensingh['PM25'].mean()

    allDivisionWisePM25Mean = [newdf_MymensinghMean,newdf_ChittagongMean,newdf_BarishalMean,newdf_RajshahiMean,newdf_SylhetMean,newdf_KhulnaMean,newdf_RangpurMean,newdfDhakaMean]

    allDivision =['Mymensingh','Chittagong','Barishal','Rajshahi','Sylhet','Khulna','Rangpur','Dhaka']



    fig = px.line( x=allDivision, y=allDivisionWisePM25Mean, markers=True)
    fig.update_layout(
        xaxis_title="Division", yaxis_title="AVG PM25"
    )
    fig.show()
    pyo.plot(fig)


    

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


def boxPlotOne(request):
    db_name = "air"
    db_host = "localhost"
    db_username = "root"
    db_password = "root"

    try:

        conn=pymysql.connect(host =db_host,
                                port = int(3306),
                                user = db_username,
                                passwd = db_password,
                                db=db_name)
    except e:


        print(e)

    

    df = pd.read_sql_query("SELECT * FROM finaltraindata", conn)
    df1 = pd.read_sql_query("SELECT * FROM epadaily", conn)
    df2 = pd.read_sql_query("SELECT * FROM purpleair", conn)

    df['time'] = pd.to_datetime(df['time'])
    df1['daily'] = pd.to_datetime(df1['daily'])
    df2['daily'] = pd.to_datetime(df2['daily'])

    #pm25 vs station
    #pm25 vs month (each box plot of different station)
    #print (df)






    fig = px.box(df, x="station", y="PM25", color="station")

    fig.update_traces(quartilemethod="exclusive") 
    #fig.update_traces(quartilemethod="linear")# or "inclusive", or "linear" by default
    layout = go.Layout(legend={'traceorder':'normal'})
    fig.update_layout(autotypenumbers='convert types')

    fig.update_yaxes(autorange=True)
    fig.update_xaxes(autorange=True)
    fig.update_layout(title_text="PM25 vs station")
    fig.update_layout(title_xanchor="auto")
    fig.update_xaxes(title_text='station')
    fig.update_yaxes(title_text='PM25')
    fig.update_layout(title_text="Box plot of stationwise recorded PM2.5 concentration")
    #fig.update_layout(legend_traceorder="reversed")
    #legendgroup=df.sort_values("station", axis = 0, ascending = True,
    #                 inplace = True, na_position ='last')
    #fig.update_layout(legend_traceorder="reversed+grouped")
    fig.show()
    






    return render(request, "graphs/boxPlotOne.html")


def boxPlotTwo(request):
    #Station-Wise AQI data visualization using a box plot, e.g.
    




    db_name = "air"
    db_host = "localhost"
    db_username = "root"
    db_password = "root"

    try:

        conn=pymysql.connect(host =db_host,
                            port = int(3306),
                            user = db_username,
                            passwd = db_password,
                            db=db_name)
    except e:


        print(e)



    df = pd.read_sql_query("SELECT * FROM finaltraindata", conn)
    df1 = pd.read_sql_query("SELECT * FROM epadaily", conn)
    df2 = pd.read_sql_query("SELECT * FROM purpleair", conn)
    df['time'] = pd.to_datetime(df['time'])
    df1['daily'] = pd.to_datetime(df1['daily'])
    df2['daily'] = pd.to_datetime(df2['daily'])
    #pm25 vs station
    #pm25 vs month (each box plot of different station)
    df['month'] = df['time'].dt.month
    newdfmonth1 = df.loc[df['month'] =="1"]
    newdfmonth1.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth1 =  newdfmonth1['PM25'].mean()
    df['month'] = df['time'].dt.month
    newdfmonth2 = df.loc[df['month'] =="2"]
    newdfmonth2.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth2 =  newdfmonth2['PM25'].mean()
    df['month'] = df['time'].dt.month
    newdfmonth3 = df.loc[df['month'] =="3"]
    newdfmonth3.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth3 =  newdfmonth3['PM25'].mean()
    df['month'] = df['time'].dt.month
    newdfmonth4 = df.loc[df['month'] =="4"]
    newdfmonth4.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth4 =  newdfmonth4['PM25'].mean()
    df['month'] = df['time'].dt.month
    newdfmonth5 = df.loc[df['month'] =="5"]
    newdfmonth5.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth5 =  newdfmonth5['PM25'].mean()
    df['month'] = df['time'].dt.month
    newdfmonth6 = df.loc[df['month'] =="6"]
    newdfmonth6.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth6 =  newdfmonth6['PM25'].mean()
    df['month'] = df['time'].dt.month
    newdfmonth6 = df.loc[df['month'] =="6"]
    newdfmonth6.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth6 =  newdfmonth6['PM25'].mean()
    df['month'] = df['time'].dt.month
    newdfmonth7 = df.loc[df['month'] =="7"]
    newdfmonth7.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth7 =  newdfmonth7['PM25'].mean()
    df['month'] = df['time'].dt.month
    newdfmonth8 = df.loc[df['month'] =="8"]
    newdfmonth8.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth8 =  newdfmonth8['PM25'].mean()
    df['month'] = df['time'].dt.month
    newdfmonth9 = df.loc[df['month'] =="9"]
    newdfmonth9.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth9 =  newdfmonth9['PM25'].mean()
    df['month'] = df['time'].dt.month
    newdfmonth10 = df.loc[df['month'] =="10"]
    newdfmonth10.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth10 =  newdfmonth10['PM25'].mean()
    df['month'] = df['time'].dt.month
    newdfmonth11 = df.loc[df['month'] =="11"]
    newdfmonth11.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth11 =  newdfmonth11['PM25'].mean()
    df['month'] = df['time'].dt.month
    newdfmonth12 = df.loc[df['month'] =="12"]
    newdfmonth12.PM25 = df.PM25.astype(float)
    #newdfDhaka=newdfDhaka['PM25'].astype(float)
    avgPMmonth12 =  newdfmonth12['PM25'].mean()
    avgPMmonth12 =  newdfmonth12['PM25'].mean()
    month=[1,2,3,4,5,6,7,8,9,10,11,12]
    avgOfallPM25MonthWise = [avgPMmonth1,avgPMmonth2,avgPMmonth3,avgPMmonth4,avgPMmonth5,avgPMmonth6,avgPMmonth7,avgPMmonth8,avgPMmonth9,avgPMmonth10,avgPMmonth11,avgPMmonth12]
    pd_new = pd.DataFrame(avgOfallPM25MonthWise) 
    df.loc[df.month == 1, "MonthAverage"] = avgPMmonth1
    df.loc[df.month == 2, "MonthAverage"] = avgPMmonth2
    df.loc[df.month == 3, "MonthAverage"] = avgPMmonth3
    df.loc[df.month == 4, "MonthAverage"] = avgPMmonth4
    df.loc[df.month == 5, "MonthAverage"] = avgPMmonth5
    df.loc[df.month == 6, "MonthAverage"] = avgPMmonth6
    df.loc[df.month == 7, "MonthAverage"] = avgPMmonth7
    df.loc[df.month == 8, "MonthAverage"] = avgPMmonth8
    df.loc[df.month == 9, "MonthAverage"] = avgPMmonth9
    df.loc[df.month == 10, "MonthAverage"] = avgPMmonth10
    df.loc[df.month == 11, "MonthAverage"] = avgPMmonth11
    df.loc[df.month == 12, "MonthAverage"] = avgPMmonth12
    dfmonth1 = df.loc[df['month'] == 1]
    dfmonth2 = df.loc[df['month'] == 2]
    dfmonth3 = df.loc[df['month'] == 3]
    dfmonth4 = df.loc[df['month'] == 4]
    dfmonth5 = df.loc[df['month'] == 5]
    dfmonth6 = df.loc[df['month'] == 6]
    dfmonth7 = df.loc[df['month'] == 7]
    dfmonth8 = df.loc[df['month'] == 8]
    dfmonth9 = df.loc[df['month'] == 9]
    dfmonth10 = df.loc[df['month'] == 10]
    dfmonth11 = df.loc[df['month'] == 11]
    dfmonth12 = df.loc[df['month'] == 12]

    dfstation1month1 = dfmonth1.loc[dfmonth1['station']== '1']
    dfstation1month2 = dfmonth2.loc[dfmonth2['station']== '1']
    dfstation1month3 = dfmonth3.loc[dfmonth3['station']== '1']
    dfstation1month4 = dfmonth4.loc[dfmonth4['station']== '1']
    dfstation1month5 = dfmonth5.loc[dfmonth5['station']== '1']
    dfstation1month6 = dfmonth6.loc[dfmonth6['station']== '1']
    dfstation1month7 = dfmonth7.loc[dfmonth7['station']== '1']
    dfstation1month8 = dfmonth8.loc[dfmonth8['station']== '1']
    dfstation1month9 = dfmonth9.loc[dfmonth9['station']== '1']
    dfstation1month10 = dfmonth10.loc[dfmonth10['station']== '1']
    dfstation1month11 = dfmonth11.loc[dfmonth11['station']== '1']
    dfstation1month12 = dfmonth12.loc[dfmonth12['station']== '1']




    dfstation2month1 = dfmonth1.loc[dfmonth1['station']== '2']
    dfstation2month2 = dfmonth2.loc[dfmonth2['station']== '2']
    dfstation2month3 = dfmonth3.loc[dfmonth3['station']== '2']
    dfstation2month4 = dfmonth4.loc[dfmonth4['station']== '2']
    dfstation2month5 = dfmonth5.loc[dfmonth5['station']== '2']
    dfstation2month6 = dfmonth6.loc[dfmonth6['station']== '2']
    dfstation2month7 = dfmonth7.loc[dfmonth7['station']== '2']
    dfstation2month8 = dfmonth8.loc[dfmonth8['station']== '2']
    dfstation2month9 = dfmonth9.loc[dfmonth9['station']== '2']
    dfstation2month10 = dfmonth10.loc[dfmonth10['station']== '2']
    dfstation2month11 = dfmonth11.loc[dfmonth11['station']== '2']
    dfstation2month12 = dfmonth12.loc[dfmonth12['station']== '2']




    dfstation3month1 = dfmonth1.loc[dfmonth1['station']== '3']
    dfstation3month2 = dfmonth2.loc[dfmonth2['station']== '3']
    dfstation3month3 = dfmonth3.loc[dfmonth3['station']== '3']
    dfstation3month4 = dfmonth4.loc[dfmonth4['station']== '3']
    dfstation3month5 = dfmonth5.loc[dfmonth5['station']== '3']
    dfstation3month6 = dfmonth6.loc[dfmonth6['station']== '3']
    dfstation3month7 = dfmonth7.loc[dfmonth7['station']== '3']
    dfstation3month8 = dfmonth8.loc[dfmonth8['station']== '3']
    dfstation3month9 = dfmonth9.loc[dfmonth9['station']== '3']
    dfstation3month10 = dfmonth10.loc[dfmonth10['station']== '3']
    dfstation3month11 = dfmonth11.loc[dfmonth11['station']== '3']
    dfstation3month12 = dfmonth12.loc[dfmonth12['station']== '3']



    dfstation4month1 = dfmonth1.loc[dfmonth1['station']== '4']
    dfstation4month2 = dfmonth2.loc[dfmonth2['station']== '4']
    dfstation4month3 = dfmonth3.loc[dfmonth3['station']== '4']
    dfstation4month4 = dfmonth4.loc[dfmonth4['station']== '4']
    dfstation4month5 = dfmonth5.loc[dfmonth5['station']== '4']
    dfstation4month6 = dfmonth6.loc[dfmonth6['station']== '4']
    dfstation4month7 = dfmonth7.loc[dfmonth7['station']== '4']
    dfstation4month8 = dfmonth8.loc[dfmonth8['station']== '4']
    dfstation4month9 = dfmonth9.loc[dfmonth9['station']== '4']
    dfstation4month10 = dfmonth10.loc[dfmonth10['station']== '4']
    dfstation4month11 = dfmonth11.loc[dfmonth11['station']== '4']
    dfstation4month12 = dfmonth12.loc[dfmonth12['station']== '4']

    dfstation5month1 = dfmonth1.loc[dfmonth1['station']==    '5']
    dfstation5month2 = dfmonth2.loc[dfmonth2['station']==    '5']
    dfstation5month3 = dfmonth3.loc[dfmonth3['station']==    '5']
    dfstation5month4 = dfmonth4.loc[dfmonth4['station']==    '5']
    dfstation5month5 = dfmonth5.loc[dfmonth5['station']==    '5']
    dfstation5month6 = dfmonth6.loc[dfmonth6['station']==    '5']
    dfstation5month7 = dfmonth7.loc[dfmonth7['station']==    '5']
    dfstation5month8 = dfmonth8.loc[dfmonth8['station']==    '5']
    dfstation5month9 = dfmonth9.loc[dfmonth9['station']==    '5']
    dfstation5month10 = dfmonth10.loc[dfmonth10['station']== '5']
    dfstation5month11 = dfmonth11.loc[dfmonth11['station']== '5']
    dfstation5month12 = dfmonth12.loc[dfmonth12['station']== '5']

    dfstation6month1 = dfmonth1.loc[dfmonth1['station']==    '6']
    dfstation6month2 = dfmonth2.loc[dfmonth2['station']==    '6']
    dfstation6month3 = dfmonth3.loc[dfmonth3['station']==    '6']
    dfstation6month4 = dfmonth4.loc[dfmonth4['station']==    '6']
    dfstation6month5 = dfmonth5.loc[dfmonth5['station']==    '6']
    dfstation6month6 = dfmonth6.loc[dfmonth6['station']==    '6']
    dfstation6month7 = dfmonth7.loc[dfmonth7['station']==    '6']
    dfstation6month8 = dfmonth8.loc[dfmonth8['station']==    '6']
    dfstation6month9 = dfmonth9.loc[dfmonth9['station']==    '6']
    dfstation6month10 = dfmonth10.loc[dfmonth10['station']== '6']
    dfstation6month11 = dfmonth11.loc[dfmonth11['station']== '6']
    dfstation6month12 = dfmonth12.loc[dfmonth12['station']== '6']

    dfstation7month1 = dfmonth1.loc[dfmonth1['station']==    '7']
    dfstation7month2 = dfmonth2.loc[dfmonth2['station']==    '7']
    dfstation7month3 = dfmonth3.loc[dfmonth3['station']==    '7']
    dfstation7month4 = dfmonth4.loc[dfmonth4['station']==    '7']
    dfstation7month5 = dfmonth5.loc[dfmonth5['station']==    '7']
    dfstation7month6 = dfmonth6.loc[dfmonth6['station']==    '7']
    dfstation7month7 = dfmonth7.loc[dfmonth7['station']==    '7']
    dfstation7month8 = dfmonth8.loc[dfmonth8['station']==    '7']
    dfstation7month9 = dfmonth9.loc[dfmonth9['station']==    '7']
    dfstation7month10 = dfmonth10.loc[dfmonth10['station']== '7']
    dfstation7month11 = dfmonth11.loc[dfmonth11['station']== '7']
    dfstation7month12 = dfmonth12.loc[dfmonth12['station']== '7']

    dfstation8month1 = dfmonth1.loc[dfmonth1['station']==    '8']
    dfstation8month2 = dfmonth2.loc[dfmonth2['station']==    '8']
    dfstation8month3 = dfmonth3.loc[dfmonth3['station']==    '8']
    dfstation8month4 = dfmonth4.loc[dfmonth4['station']==    '8']
    dfstation8month5 = dfmonth5.loc[dfmonth5['station']==    '8']
    dfstation8month6 = dfmonth6.loc[dfmonth6['station']==    '8']
    dfstation8month7 = dfmonth7.loc[dfmonth7['station']==    '8']
    dfstation8month8 = dfmonth8.loc[dfmonth8['station']==    '8']
    dfstation8month9 = dfmonth9.loc[dfmonth9['station']==    '8']
    dfstation8month10 = dfmonth10.loc[dfmonth10['station']== '8']
    dfstation8month11 = dfmonth11.loc[dfmonth11['station']== '8']
    dfstation8month12 = dfmonth12.loc[dfmonth12['station']== '8']


    dfstation9month1 = dfmonth1.loc[dfmonth1['station']==    '9']
    dfstation9month2 = dfmonth2.loc[dfmonth2['station']==    '9']
    dfstation9month3 = dfmonth3.loc[dfmonth3['station']==    '9']
    dfstation9month4 = dfmonth4.loc[dfmonth4['station']==    '9']
    dfstation9month5 = dfmonth5.loc[dfmonth5['station']==    '9']
    dfstation9month6 = dfmonth6.loc[dfmonth6['station']==    '9']
    dfstation9month7 = dfmonth7.loc[dfmonth7['station']==    '9']
    dfstation9month8 = dfmonth8.loc[dfmonth8['station']==    '9']
    dfstation9month9 = dfmonth9.loc[dfmonth9['station']==    '9']
    dfstation9month10 = dfmonth10.loc[dfmonth10['station']== '9']
    dfstation9month11 = dfmonth11.loc[dfmonth11['station']== '9']
    dfstation9month12 = dfmonth12.loc[dfmonth12['station']== '9']

    dfstation10month1 = dfmonth1.loc[dfmonth1['station']==    '10']
    dfstation10month2 = dfmonth2.loc[dfmonth2['station']==    '10']
    dfstation10month3 = dfmonth3.loc[dfmonth3['station']==    '10']
    dfstation10month4 = dfmonth4.loc[dfmonth4['station']==    '10']
    dfstation10month5 = dfmonth5.loc[dfmonth5['station']==    '10']
    dfstation10month6 = dfmonth6.loc[dfmonth6['station']==    '10']
    dfstation10month7 = dfmonth7.loc[dfmonth7['station']==    '10']
    dfstation10month8 = dfmonth8.loc[dfmonth8['station']==    '10']
    dfstation10month9 = dfmonth9.loc[dfmonth9['station']==    '10']
    dfstation10month10 = dfmonth10.loc[dfmonth10['station']== '10']
    dfstation10month11 = dfmonth11.loc[dfmonth11['station']== '10']
    dfstation10month12 = dfmonth12.loc[dfmonth12['station']== '10']

    dfstation11month1 = dfmonth1.loc[dfmonth1['station']==    '11']
    dfstation11month2 = dfmonth2.loc[dfmonth2['station']==    '11']
    dfstation11month3 = dfmonth3.loc[dfmonth3['station']==    '11']
    dfstation11month4 = dfmonth4.loc[dfmonth4['station']==    '11']
    dfstation11month5 = dfmonth5.loc[dfmonth5['station']==    '11']
    dfstation11month6 = dfmonth6.loc[dfmonth6['station']==    '11']
    dfstation11month7 = dfmonth7.loc[dfmonth7['station']==    '11']
    dfstation11month8 = dfmonth8.loc[dfmonth8['station']==    '11']
    dfstation11month9 = dfmonth9.loc[dfmonth9['station']==    '11']
    dfstation11month10 = dfmonth10.loc[dfmonth10['station']== '11']
    dfstation11month11 = dfmonth11.loc[dfmonth11['station']== '11']
    dfstation11month12 = dfmonth12.loc[dfmonth12['station']== '11']


    dfstation12month1 = dfmonth1.loc[dfmonth1['station']==    '12']
    dfstation12month2 = dfmonth2.loc[dfmonth2['station']==    '12']
    dfstation12month3 = dfmonth3.loc[dfmonth3['station']==    '12']
    dfstation12month4 = dfmonth4.loc[dfmonth4['station']==    '12']
    dfstation12month5 = dfmonth5.loc[dfmonth5['station']==    '12']
    dfstation12month6 = dfmonth6.loc[dfmonth6['station']==    '12']
    dfstation12month7 = dfmonth7.loc[dfmonth7['station']==    '12']
    dfstation12month8 = dfmonth8.loc[dfmonth8['station']==    '12']
    dfstation12month9 = dfmonth9.loc[dfmonth9['station']==    '12']
    dfstation12month10 = dfmonth10.loc[dfmonth10['station']== '12']
    dfstation12month11 = dfmonth11.loc[dfmonth11['station']== '12']
    dfstation12month12 = dfmonth12.loc[dfmonth12['station']== '12']



    dfstation13month1 = dfmonth1.loc[dfmonth1['station']==    '13']
    dfstation13month2 = dfmonth2.loc[dfmonth2['station']==    '13']
    dfstation13month3 = dfmonth3.loc[dfmonth3['station']==    '13']
    dfstation13month4 = dfmonth4.loc[dfmonth4['station']==    '13']
    dfstation13month5 = dfmonth5.loc[dfmonth5['station']==    '13']
    dfstation13month6 = dfmonth6.loc[dfmonth6['station']==    '13']
    dfstation13month7 = dfmonth7.loc[dfmonth7['station']==    '13']
    dfstation13month8 = dfmonth8.loc[dfmonth8['station']==    '13']
    dfstation13month9 = dfmonth9.loc[dfmonth9['station']==    '13']
    dfstation13month10 = dfmonth10.loc[dfmonth10['station']== '13']
    dfstation13month11 = dfmonth11.loc[dfmonth11['station']== '13']
    dfstation13month12 = dfmonth12.loc[dfmonth12['station']== '13']



    dfstation14month1 = dfmonth1.loc[dfmonth1['station']==    '14']
    dfstation14month2 = dfmonth2.loc[dfmonth2['station']==    '14']
    dfstation14month3 = dfmonth3.loc[dfmonth3['station']==    '14']
    dfstation14month4 = dfmonth4.loc[dfmonth4['station']==    '14']
    dfstation14month5 = dfmonth5.loc[dfmonth5['station']==    '14']
    dfstation14month6 = dfmonth6.loc[dfmonth6['station']==    '14']
    dfstation14month7 = dfmonth7.loc[dfmonth7['station']==    '14']
    dfstation14month8 = dfmonth8.loc[dfmonth8['station']==    '14']
    dfstation14month9 = dfmonth9.loc[dfmonth9['station']==    '14']
    dfstation14month10 = dfmonth10.loc[dfmonth10['station']== '14']
    dfstation14month11 = dfmonth11.loc[dfmonth11['station']== '14']
    dfstation14month12 = dfmonth12.loc[dfmonth12['station']== '14']


    dfstation15month1 = dfmonth1.loc[dfmonth1['station']==    '15']
    dfstation15month2 = dfmonth2.loc[dfmonth2['station']==    '15']
    dfstation15month3 = dfmonth3.loc[dfmonth3['station']==    '15']
    dfstation15month4 = dfmonth4.loc[dfmonth4['station']==    '15']
    dfstation15month5 = dfmonth5.loc[dfmonth5['station']==    '15']
    dfstation15month6 = dfmonth6.loc[dfmonth6['station']==    '15']
    dfstation15month7 = dfmonth7.loc[dfmonth7['station']==    '15']
    dfstation15month8 = dfmonth8.loc[dfmonth8['station']==    '15']
    dfstation15month9 = dfmonth9.loc[dfmonth9['station']==    '15']
    dfstation15month10 = dfmonth10.loc[dfmonth10['station']== '15']
    dfstation15month11 = dfmonth11.loc[dfmonth11['station']== '15']
    dfstation15month12 = dfmonth12.loc[dfmonth12['station']== '15']


    dfstation16month1 = dfmonth1.loc[dfmonth1['station']==    '16']
    dfstation16month2 = dfmonth2.loc[dfmonth2['station']==    '16']
    dfstation16month3 = dfmonth3.loc[dfmonth3['station']==    '16']
    dfstation16month4 = dfmonth4.loc[dfmonth4['station']==    '16']
    dfstation16month5 = dfmonth5.loc[dfmonth5['station']==    '16']
    dfstation16month6 = dfmonth6.loc[dfmonth6['station']==    '16']
    dfstation16month7 = dfmonth7.loc[dfmonth7['station']==    '16']
    dfstation16month8 = dfmonth8.loc[dfmonth8['station']==    '16']
    dfstation16month9 = dfmonth9.loc[dfmonth9['station']==    '16']
    dfstation16month10 = dfmonth10.loc[dfmonth10['station']== '16']
    dfstation16month11 = dfmonth11.loc[dfmonth11['station']== '16']
    dfstation16month12 = dfmonth12.loc[dfmonth12['station']== '16']

    dfstation17month1 = dfmonth1.loc[dfmonth1['station']==    '17']
    dfstation17month2 = dfmonth2.loc[dfmonth2['station']==    '17']
    dfstation17month3 = dfmonth3.loc[dfmonth3['station']==    '17']
    dfstation17month4 = dfmonth4.loc[dfmonth4['station']==    '17']
    dfstation17month5 = dfmonth5.loc[dfmonth5['station']==    '17']
    dfstation17month6 = dfmonth6.loc[dfmonth6['station']==    '17']
    dfstation17month7 = dfmonth7.loc[dfmonth7['station']==    '17']
    dfstation17month8 = dfmonth8.loc[dfmonth8['station']==    '17']
    dfstation17month9 = dfmonth9.loc[dfmonth9['station']==    '17']
    dfstation17month10 = dfmonth10.loc[dfmonth10['station']== '17']
    dfstation17month11 = dfmonth11.loc[dfmonth11['station']== '17']
    dfstation17month12 = dfmonth12.loc[dfmonth12['station']== '17']

    dfstation18month1 = dfmonth1.loc[dfmonth1['station']==    '18']
    dfstation18month2 = dfmonth2.loc[dfmonth2['station']==    '18']
    dfstation18month3 = dfmonth3.loc[dfmonth3['station']==    '18']
    dfstation18month4 = dfmonth4.loc[dfmonth4['station']==    '18']
    dfstation18month5 = dfmonth5.loc[dfmonth5['station']==    '18']
    dfstation18month6 = dfmonth6.loc[dfmonth6['station']==    '18']
    dfstation18month7 = dfmonth7.loc[dfmonth7['station']==    '18']
    dfstation18month8 = dfmonth8.loc[dfmonth8['station']==    '18']
    dfstation18month9 = dfmonth9.loc[dfmonth9['station']==    '18']
    dfstation18month10 = dfmonth10.loc[dfmonth10['station']== '18']
    dfstation18month11 = dfmonth11.loc[dfmonth11['station']== '18']
    dfstation18month12 = dfmonth12.loc[dfmonth12['station']== '18']

    dfstation19month1 = dfmonth1.loc[dfmonth1['station']==    '19']
    dfstation19month2 = dfmonth2.loc[dfmonth2['station']==    '19']
    dfstation19month3 = dfmonth3.loc[dfmonth3['station']==    '19']
    dfstation19month4 = dfmonth4.loc[dfmonth4['station']==    '19']
    dfstation19month5 = dfmonth5.loc[dfmonth5['station']==    '19']
    dfstation19month6 = dfmonth6.loc[dfmonth6['station']==    '19']
    dfstation19month7 = dfmonth7.loc[dfmonth7['station']==    '19']
    dfstation19month8 = dfmonth8.loc[dfmonth8['station']==    '19']
    dfstation19month9 = dfmonth9.loc[dfmonth9['station']==    '19']
    dfstation19month10 = dfmonth10.loc[dfmonth10['station']== '19']
    dfstation19month11 = dfmonth11.loc[dfmonth11['station']== '19']
    dfstation19month12 = dfmonth12.loc[dfmonth12['station']== '19']

    dfstation20month1 = dfmonth1.loc[dfmonth1['station']==    '20']
    dfstation20month2 = dfmonth2.loc[dfmonth2['station']==    '20']
    dfstation20month3 = dfmonth3.loc[dfmonth3['station']==    '20']
    dfstation20month4 = dfmonth4.loc[dfmonth4['station']==    '20']
    dfstation20month5 = dfmonth5.loc[dfmonth5['station']==    '20']
    dfstation20month6 = dfmonth6.loc[dfmonth6['station']==    '20']
    dfstation20month7 = dfmonth7.loc[dfmonth7['station']==    '20']
    dfstation20month8 = dfmonth8.loc[dfmonth8['station']==    '20']
    dfstation20month9 = dfmonth9.loc[dfmonth9['station']==    '20']
    dfstation20month10 = dfmonth10.loc[dfmonth10['station']== '20']
    dfstation20month11 = dfmonth11.loc[dfmonth11['station']== '20']
    dfstation20month12 = dfmonth12.loc[dfmonth12['station']== '20']


    dfstation21month1 = dfmonth1.loc[dfmonth1['station']==    '21']
    dfstation21month2 = dfmonth2.loc[dfmonth2['station']==    '21']
    dfstation21month3 = dfmonth3.loc[dfmonth3['station']==    '21']
    dfstation21month4 = dfmonth4.loc[dfmonth4['station']==    '21']
    dfstation21month5 = dfmonth5.loc[dfmonth5['station']==    '21']
    dfstation21month6 = dfmonth6.loc[dfmonth6['station']==    '21']
    dfstation21month7 = dfmonth7.loc[dfmonth7['station']==    '21']
    dfstation21month8 = dfmonth8.loc[dfmonth8['station']==    '21']
    dfstation21month9 = dfmonth9.loc[dfmonth9['station']==    '21']
    dfstation21month10 = dfmonth10.loc[dfmonth10['station']== '21']
    dfstation21month11 = dfmonth11.loc[dfmonth11['station']== '21']
    dfstation21month12 = dfmonth12.loc[dfmonth12['station']== '21']


    dfstation22month1 = dfmonth1.loc[dfmonth1['station']==    '22']
    dfstation22month2 = dfmonth2.loc[dfmonth2['station']==    '22']
    dfstation22month3 = dfmonth3.loc[dfmonth3['station']==    '22']
    dfstation22month4 = dfmonth4.loc[dfmonth4['station']==    '22']
    dfstation22month5 = dfmonth5.loc[dfmonth5['station']==    '22']
    dfstation22month6 = dfmonth6.loc[dfmonth6['station']==    '22']
    dfstation22month7 = dfmonth7.loc[dfmonth7['station']==    '22']
    dfstation22month8 = dfmonth8.loc[dfmonth8['station']==    '22']
    dfstation22month9 = dfmonth9.loc[dfmonth9['station']==    '22']
    dfstation22month10 = dfmonth10.loc[dfmonth10['station']== '22']
    dfstation22month11 = dfmonth11.loc[dfmonth11['station']== '22']
    dfstation22month12 = dfmonth12.loc[dfmonth12['station']== '22']

    dfstation23month1 = dfmonth1.loc[dfmonth1['station']==    '23']
    dfstation23month2 = dfmonth2.loc[dfmonth2['station']==    '23']
    dfstation23month3 = dfmonth3.loc[dfmonth3['station']==    '23']
    dfstation23month4 = dfmonth4.loc[dfmonth4['station']==    '23']
    dfstation23month5 = dfmonth5.loc[dfmonth5['station']==    '23']
    dfstation23month6 = dfmonth6.loc[dfmonth6['station']==    '23']
    dfstation23month7 = dfmonth7.loc[dfmonth7['station']==    '23']
    dfstation23month8 = dfmonth8.loc[dfmonth8['station']==    '23']
    dfstation23month9 = dfmonth9.loc[dfmonth9['station']==    '23']
    dfstation23month10 = dfmonth10.loc[dfmonth10['station']== '23']
    dfstation23month11 = dfmonth11.loc[dfmonth11['station']== '23']
    dfstation23month12 = dfmonth12.loc[dfmonth12['station']== '23']



    # Create figure

    fig1 = go.Figure()
    fig1.add_trace(go.Box(y=dfstation1month1["PM25"], name=month[0],
                       ))

    fig1.add_trace(go.Box(y=dfstation1month2["PM25"], name=month[1],
                        ))
    fig1.add_trace(go.Box(y=dfstation1month3["PM25"], name=month[2],
                        ))
    fig1.add_trace(go.Box(y=dfstation1month4["PM25"], name=month[3],
                        ))
    fig1.add_trace(go.Box(y=dfstation1month5["PM25"], name=month[4],
                        ))
    fig1.add_trace(go.Box(y=dfstation1month6["PM25"], name=month[5],
                        ))
    fig1.add_trace(go.Box(y=dfstation1month7["PM25"], name=month[6],
                        ))
    fig1.add_trace(go.Box(y=dfstation1month8["PM25"], name=month[7],
                        ))
    fig1.add_trace(go.Box(y=dfstation1month9["PM25"], name=month[8],
                        ))
    fig1.add_trace(go.Box(y=dfstation1month10["PM25"], name=month[9],
                        ))
    fig1.add_trace(go.Box(y=dfstation1month11["PM25"], name=month[10],
                        ))
    fig1.add_trace(go.Box(y=dfstation1month12["PM25"], name=month[11],
                        ))


    fig1.update_layout(
        title_text="for station 1",
        xaxis_title="month", yaxis_title="PM2.5",
        showlegend=True,autotypenumbers='convert types'
    )





    fig2 = go.Figure()
    fig2.add_trace(go.Box(y=dfstation2month1["PM25"], name=month[0],
                      ))

    fig2.add_trace(go.Box(y=dfstation2month2["PM25"], name=month[1],
                        ))
    fig2.add_trace(go.Box(y=dfstation2month3["PM25"], name=month[2],
                        ))
    fig2.add_trace(go.Box(y=dfstation2month4["PM25"], name=month[3],
                        ))
    fig2.add_trace(go.Box(y=dfstation2month5["PM25"], name=month[4],
                        ))
    fig2.add_trace(go.Box(y=dfstation2month6["PM25"], name=month[5],
                        ))
    fig2.add_trace(go.Box(y=dfstation2month7["PM25"], name=month[6],
                        ))
    fig2.add_trace(go.Box(y=dfstation2month8["PM25"], name=month[7],
                        ))
    fig2.add_trace(go.Box(y=dfstation2month9["PM25"], name=month[8],
                        ))
    fig2.add_trace(go.Box(y=dfstation2month10["PM25"], name=month[9],
                        ))
    fig2.add_trace(go.Box(y=dfstation2month11["PM25"], name=month[10],
                        ))
    fig2.add_trace(go.Box(y=dfstation2month12["PM25"], name=month[11],
                        ))


    fig2.update_layout(
        title_text="for station 2",
        showlegend=True,
        xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types'
    )



    fig3 = go.Figure()
    fig3.add_trace(go.Box(y=dfstation3month1["PM25"], name=month[0],
                      ))

    fig3.add_trace(go.Box(y=dfstation3month2["PM25"], name=month[1],
                        ))
    fig3.add_trace(go.Box(y=dfstation3month3["PM25"], name=month[2],
                        ))
    fig3.add_trace(go.Box(y=dfstation3month4["PM25"], name=month[3],
                        ))
    fig3.add_trace(go.Box(y=dfstation3month5["PM25"], name=month[4],
                        ))
    fig3.add_trace(go.Box(y=dfstation3month6["PM25"], name=month[5],
                        ))
    fig3.add_trace(go.Box(y=dfstation3month7["PM25"], name=month[6],
                        ))
    fig3.add_trace(go.Box(y=dfstation3month8["PM25"], name=month[7],
                        ))
    fig3.add_trace(go.Box(y=dfstation3month9["PM25"], name=month[8],
                        ))
    fig3.add_trace(go.Box(y=dfstation3month10["PM25"], name=month[9],
                        ))
    fig3.add_trace(go.Box(y=dfstation3month11["PM25"], name=month[10],
                        ))
    fig3.add_trace(go.Box(y=dfstation3month12["PM25"], name=month[11],
                        ))


    fig3.update_layout(
        title_text="for station 3",
        showlegend=True,
        xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types'
    )





    fig4 = go.Figure()
    fig4.add_trace(go.Box(y=dfstation4month1["PM25"], name=month[0],
                      ))

    fig4.add_trace(go.Box(y=dfstation4month2["PM25"], name=month[1],
                        ))
    fig4.add_trace(go.Box(y=dfstation4month3["PM25"], name=month[2],
                        ))
    fig4.add_trace(go.Box(y=dfstation4month4["PM25"], name=month[3],
                        ))
    fig4.add_trace(go.Box(y=dfstation4month5["PM25"], name=month[4],
                        ))
    fig4.add_trace(go.Box(y=dfstation4month6["PM25"], name=month[5],
                        ))
    fig4.add_trace(go.Box(y=dfstation4month7["PM25"], name=month[6],
                        ))
    fig4.add_trace(go.Box(y=dfstation4month8["PM25"], name=month[7],
                        ))
    fig4.add_trace(go.Box(y=dfstation4month9["PM25"], name=month[8],
                        ))
    fig4.add_trace(go.Box(y=dfstation4month10["PM25"], name=month[9],
                        ))
    fig4.add_trace(go.Box(y=dfstation4month11["PM25"], name=month[10],
                        ))
    fig4.add_trace(go.Box(y=dfstation4month12["PM25"], name=month[11],
                        ))

    fig4.update_layout(
        title_text="for station 4",
        showlegend=True,
        xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types'
    )





    fig5 = go.Figure()
    fig5.add_trace(go.Box(y=dfstation5month1["PM25"], name=month[0],))
    fig5.add_trace(go.Box(y=dfstation5month2["PM25"], name=month[1],))
    fig5.add_trace(go.Box(y=dfstation5month3["PM25"], name=month[2],))
    fig5.add_trace(go.Box(y=dfstation5month4["PM25"], name=month[3],))
    fig5.add_trace(go.Box(y=dfstation5month5["PM25"], name=month[4],))
    fig5.add_trace(go.Box(y=dfstation5month6["PM25"], name=month[5],))
    fig5.add_trace(go.Box(y=dfstation5month7["PM25"], name=month[6],))
    fig5.add_trace(go.Box(y=dfstation5month8["PM25"], name=month[7],))
    fig5.add_trace(go.Box(y=dfstation5month9["PM25"], name=month[8],))
    fig5.add_trace(go.Box(y=dfstation5month10["PM25"], name=month[9],))
    fig5.add_trace(go.Box(y=dfstation5month11["PM25"], name=month[10],))
    fig5.add_trace(go.Box(y=dfstation5month12["PM25"], name=month[11],))
    fig5.update_layout(title_text="for station 5",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')


    fig6 = go.Figure()
    fig6.add_trace(go.Box(y=dfstation6month1["PM25"], name=month[0],))
    fig6.add_trace(go.Box(y=dfstation6month2["PM25"], name=month[1],))
    fig6.add_trace(go.Box(y=dfstation6month3["PM25"], name=month[2],))
    fig6.add_trace(go.Box(y=dfstation6month4["PM25"], name=month[3],))
    fig6.add_trace(go.Box(y=dfstation6month5["PM25"], name=month[4],))
    fig6.add_trace(go.Box(y=dfstation6month6["PM25"], name=month[5],))
    fig6.add_trace(go.Box(y=dfstation6month7["PM25"], name=month[6],))
    fig6.add_trace(go.Box(y=dfstation6month8["PM25"], name=month[7],))
    fig6.add_trace(go.Box(y=dfstation6month9["PM25"], name=month[8],))
    fig6.add_trace(go.Box(y=dfstation6month10["PM25"], name=month[9],))
    fig6.add_trace(go.Box(y=dfstation6month11["PM25"], name=month[10],))
    fig6.add_trace(go.Box(y=dfstation6month12["PM25"], name=month[11],))
    fig6.update_layout(title_text="for station 6",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig7 = go.Figure()
    fig7.add_trace(go.Box(y=dfstation7month1["PM25"], name=month[0],))
    fig7.add_trace(go.Box(y=dfstation7month2["PM25"], name=month[1],))
    fig7.add_trace(go.Box(y=dfstation7month3["PM25"], name=month[2],))
    fig7.add_trace(go.Box(y=dfstation7month4["PM25"], name=month[3],))
    fig7.add_trace(go.Box(y=dfstation7month5["PM25"], name=month[4],))
    fig7.add_trace(go.Box(y=dfstation7month6["PM25"], name=month[5],))
    fig7.add_trace(go.Box(y=dfstation7month7["PM25"], name=month[6],))
    fig7.add_trace(go.Box(y=dfstation7month8["PM25"], name=month[7],))
    fig7.add_trace(go.Box(y=dfstation7month9["PM25"], name=month[8],))
    fig7.add_trace(go.Box(y=dfstation7month10["PM25"], name=month[9],))
    fig7.add_trace(go.Box(y=dfstation7month11["PM25"], name=month[10],))
    fig7.add_trace(go.Box(y=dfstation7month12["PM25"], name=month[11],))
    fig7.update_layout(title_text="for station 7",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig8 = go.Figure()
    fig8.add_trace(go.Box(y=dfstation8month1["PM25"], name=month[0],))
    fig8.add_trace(go.Box(y=dfstation8month2["PM25"], name=month[1],))
    fig8.add_trace(go.Box(y=dfstation8month3["PM25"], name=month[2],))
    fig8.add_trace(go.Box(y=dfstation8month4["PM25"], name=month[3],))
    fig8.add_trace(go.Box(y=dfstation8month5["PM25"], name=month[4],))
    fig8.add_trace(go.Box(y=dfstation8month6["PM25"], name=month[5],))
    fig8.add_trace(go.Box(y=dfstation8month7["PM25"], name=month[6],))
    fig8.add_trace(go.Box(y=dfstation8month8["PM25"], name=month[7],))
    fig8.add_trace(go.Box(y=dfstation8month9["PM25"], name=month[8],))
    fig8.add_trace(go.Box(y=dfstation8month10["PM25"], name=month[9],))
    fig8.add_trace(go.Box(y=dfstation8month11["PM25"], name=month[10],))
    fig8.add_trace(go.Box(y=dfstation8month12["PM25"], name=month[11],))
    fig8.update_layout(title_text="for station 8",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')


    fig9 = go.Figure()
    fig9.add_trace(go.Box(y=dfstation9month1["PM25"], name=month[0],))
    fig9.add_trace(go.Box(y=dfstation9month2["PM25"], name=month[1],))
    fig9.add_trace(go.Box(y=dfstation9month3["PM25"], name=month[2],))
    fig9.add_trace(go.Box(y=dfstation9month4["PM25"], name=month[3],))
    fig9.add_trace(go.Box(y=dfstation9month5["PM25"], name=month[4],))
    fig9.add_trace(go.Box(y=dfstation9month6["PM25"], name=month[5],))
    fig9.add_trace(go.Box(y=dfstation9month7["PM25"], name=month[6],))
    fig9.add_trace(go.Box(y=dfstation9month8["PM25"], name=month[7],))
    fig9.add_trace(go.Box(y=dfstation9month9["PM25"], name=month[8],))
    fig9.add_trace(go.Box(y=dfstation9month10["PM25"], name=month[9],))
    fig9.add_trace(go.Box(y=dfstation9month11["PM25"], name=month[10],))
    fig9.add_trace(go.Box(y=dfstation9month12["PM25"], name=month[11],))
    fig9.update_layout(title_text="for station 9",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig10 = go.Figure()
    fig10.add_trace(go.Box(y=dfstation10month1["PM25"], name=month[0],))
    fig10.add_trace(go.Box(y=dfstation10month2["PM25"], name=month[1],))
    fig10.add_trace(go.Box(y=dfstation10month3["PM25"], name=month[2],))
    fig10.add_trace(go.Box(y=dfstation10month4["PM25"], name=month[3],))
    fig10.add_trace(go.Box(y=dfstation10month5["PM25"], name=month[4],))
    fig10.add_trace(go.Box(y=dfstation10month6["PM25"], name=month[5],))
    fig10.add_trace(go.Box(y=dfstation10month7["PM25"], name=month[6],))
    fig10.add_trace(go.Box(y=dfstation10month8["PM25"], name=month[7],))
    fig10.add_trace(go.Box(y=dfstation10month9["PM25"], name=month[8],))
    fig10.add_trace(go.Box(y=dfstation10month10["PM25"], name=month[9],))
    fig10.add_trace(go.Box(y=dfstation10month11["PM25"], name=month[10],))
    fig10.add_trace(go.Box(y=dfstation10month12["PM25"], name=month[11],))
    fig10.update_layout(title_text="for station 10",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig11 = go.Figure()
    fig11.add_trace(go.Box(y=dfstation11month1["PM25"], name=month[0],))
    fig11.add_trace(go.Box(y=dfstation11month2["PM25"], name=month[1],))
    fig11.add_trace(go.Box(y=dfstation11month3["PM25"], name=month[2],))
    fig11.add_trace(go.Box(y=dfstation11month4["PM25"], name=month[3],))
    fig11.add_trace(go.Box(y=dfstation11month5["PM25"], name=month[4],))
    fig11.add_trace(go.Box(y=dfstation11month6["PM25"], name=month[5],))
    fig11.add_trace(go.Box(y=dfstation11month7["PM25"], name=month[6],))
    fig11.add_trace(go.Box(y=dfstation11month8["PM25"], name=month[7],))
    fig11.add_trace(go.Box(y=dfstation11month9["PM25"], name=month[8],))
    fig11.add_trace(go.Box(y=dfstation11month10["PM25"], name=month[9],))
    fig11.add_trace(go.Box(y=dfstation11month11["PM25"], name=month[10],))
    fig11.add_trace(go.Box(y=dfstation11month12["PM25"], name=month[11],))
    fig11.update_layout(title_text="for station 11",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig12 = go.Figure()
    fig12.add_trace(go.Box(y=dfstation12month1["PM25"], name=month[0],))
    fig12.add_trace(go.Box(y=dfstation12month2["PM25"], name=month[1],))
    fig12.add_trace(go.Box(y=dfstation12month3["PM25"], name=month[2],))
    fig12.add_trace(go.Box(y=dfstation12month4["PM25"], name=month[3],))
    fig12.add_trace(go.Box(y=dfstation12month5["PM25"], name=month[4],))
    fig12.add_trace(go.Box(y=dfstation12month6["PM25"], name=month[5],))
    fig12.add_trace(go.Box(y=dfstation12month7["PM25"], name=month[6],))
    fig12.add_trace(go.Box(y=dfstation12month8["PM25"], name=month[7],))
    fig12.add_trace(go.Box(y=dfstation12month9["PM25"], name=month[8],))
    fig12.add_trace(go.Box(y=dfstation12month10["PM25"], name=month[9],))
    fig12.add_trace(go.Box(y=dfstation12month11["PM25"], name=month[10],))
    fig12.add_trace(go.Box(y=dfstation12month12["PM25"], name=month[11],))
    fig12.update_layout(title_text="for station 12",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig13 = go.Figure()
    fig13.add_trace(go.Box(y=dfstation13month1["PM25"], name=month[0],))
    fig13.add_trace(go.Box(y=dfstation13month2["PM25"], name=month[1],))
    fig13.add_trace(go.Box(y=dfstation13month3["PM25"], name=month[2],))
    fig13.add_trace(go.Box(y=dfstation13month4["PM25"], name=month[3],))
    fig13.add_trace(go.Box(y=dfstation13month5["PM25"], name=month[4],))
    fig13.add_trace(go.Box(y=dfstation13month6["PM25"], name=month[5],))
    fig13.add_trace(go.Box(y=dfstation13month7["PM25"], name=month[6],))
    fig13.add_trace(go.Box(y=dfstation13month8["PM25"], name=month[7],))
    fig13.add_trace(go.Box(y=dfstation13month9["PM25"], name=month[8],))
    fig13.add_trace(go.Box(y=dfstation13month10["PM25"], name=month[9],))
    fig13.add_trace(go.Box(y=dfstation13month11["PM25"], name=month[10],))
    fig13.add_trace(go.Box(y=dfstation13month12["PM25"], name=month[11],))
    fig13.update_layout(title_text="for station 13",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig14 = go.Figure()
    fig14.add_trace(go.Box(y=dfstation14month1["PM25"], name=month[0],))
    fig14.add_trace(go.Box(y=dfstation14month2["PM25"], name=month[1],))
    fig14.add_trace(go.Box(y=dfstation14month3["PM25"], name=month[2],))
    fig14.add_trace(go.Box(y=dfstation14month4["PM25"], name=month[3],))
    fig14.add_trace(go.Box(y=dfstation14month5["PM25"], name=month[4],))
    fig14.add_trace(go.Box(y=dfstation14month6["PM25"], name=month[5],))
    fig14.add_trace(go.Box(y=dfstation14month7["PM25"], name=month[6],))
    fig14.add_trace(go.Box(y=dfstation14month8["PM25"], name=month[7],))
    fig14.add_trace(go.Box(y=dfstation14month9["PM25"], name=month[8],))
    fig14.add_trace(go.Box(y=dfstation14month10["PM25"], name=month[9],))
    fig14.add_trace(go.Box(y=dfstation14month11["PM25"], name=month[10],))
    fig14.add_trace(go.Box(y=dfstation14month12["PM25"], name=month[11],))
    fig14.update_layout(title_text="for station 14",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig15 = go.Figure()
    fig15.add_trace(go.Box(y=dfstation15month1["PM25"], name=month[0],))
    fig15.add_trace(go.Box(y=dfstation15month2["PM25"], name=month[1],))
    fig15.add_trace(go.Box(y=dfstation15month3["PM25"], name=month[2],))
    fig15.add_trace(go.Box(y=dfstation15month4["PM25"], name=month[3],))
    fig15.add_trace(go.Box(y=dfstation15month5["PM25"], name=month[4],))
    fig15.add_trace(go.Box(y=dfstation15month6["PM25"], name=month[5],))
    fig15.add_trace(go.Box(y=dfstation15month7["PM25"], name=month[6],))
    fig15.add_trace(go.Box(y=dfstation15month8["PM25"], name=month[7],))
    fig15.add_trace(go.Box(y=dfstation15month9["PM25"], name=month[8],))
    fig15.add_trace(go.Box(y=dfstation15month10["PM25"], name=month[9],))
    fig15.add_trace(go.Box(y=dfstation15month11["PM25"], name=month[10],))
    fig15.add_trace(go.Box(y=dfstation15month12["PM25"], name=month[11],))
    fig15.update_layout(title_text="for station 15",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig16 = go.Figure()
    fig16.add_trace(go.Box(y=dfstation16month1["PM25"], name=month[0],))
    fig16.add_trace(go.Box(y=dfstation16month2["PM25"], name=month[1],))
    fig16.add_trace(go.Box(y=dfstation16month3["PM25"], name=month[2],))
    fig16.add_trace(go.Box(y=dfstation16month4["PM25"], name=month[3],))
    fig16.add_trace(go.Box(y=dfstation16month5["PM25"], name=month[4],))
    fig16.add_trace(go.Box(y=dfstation16month6["PM25"], name=month[5],))
    fig16.add_trace(go.Box(y=dfstation16month7["PM25"], name=month[6],))
    fig16.add_trace(go.Box(y=dfstation16month8["PM25"], name=month[7],))
    fig16.add_trace(go.Box(y=dfstation16month9["PM25"], name=month[8],))
    fig16.add_trace(go.Box(y=dfstation16month10["PM25"], name=month[9],))
    fig16.add_trace(go.Box(y=dfstation16month11["PM25"], name=month[10],))
    fig16.add_trace(go.Box(y=dfstation16month12["PM25"], name=month[11],))
    fig16.update_layout(title_text="for station 16",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')


    fig17 = go.Figure()
    fig17.add_trace(go.Box(y=dfstation17month1["PM25"], name=month[0],))
    fig17.add_trace(go.Box(y=dfstation17month2["PM25"], name=month[1],))
    fig17.add_trace(go.Box(y=dfstation17month3["PM25"], name=month[2],))
    fig17.add_trace(go.Box(y=dfstation17month4["PM25"], name=month[3],))
    fig17.add_trace(go.Box(y=dfstation17month5["PM25"], name=month[4],))
    fig17.add_trace(go.Box(y=dfstation17month6["PM25"], name=month[5],))
    fig17.add_trace(go.Box(y=dfstation17month7["PM25"], name=month[6],))
    fig17.add_trace(go.Box(y=dfstation17month8["PM25"], name=month[7],))
    fig17.add_trace(go.Box(y=dfstation17month9["PM25"], name=month[8],))
    fig17.add_trace(go.Box(y=dfstation17month10["PM25"], name=month[9],))
    fig17.add_trace(go.Box(y=dfstation17month11["PM25"], name=month[10],))
    fig17.add_trace(go.Box(y=dfstation17month12["PM25"], name=month[11],))
    fig17.update_layout(title_text="for station 17",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')


    fig18 = go.Figure()
    fig18.add_trace(go.Box(y=dfstation18month1["PM25"], name=month[0],))
    fig18.add_trace(go.Box(y=dfstation18month2["PM25"], name=month[1],))
    fig18.add_trace(go.Box(y=dfstation18month3["PM25"], name=month[2],))
    fig18.add_trace(go.Box(y=dfstation18month4["PM25"], name=month[3],))
    fig18.add_trace(go.Box(y=dfstation18month5["PM25"], name=month[4],))
    fig18.add_trace(go.Box(y=dfstation18month6["PM25"], name=month[5],))
    fig18.add_trace(go.Box(y=dfstation18month7["PM25"], name=month[6],))
    fig18.add_trace(go.Box(y=dfstation18month8["PM25"], name=month[7],))
    fig18.add_trace(go.Box(y=dfstation18month9["PM25"], name=month[8],))
    fig18.add_trace(go.Box(y=dfstation18month10["PM25"], name=month[9],))
    fig18.add_trace(go.Box(y=dfstation18month11["PM25"], name=month[10],))
    fig18.add_trace(go.Box(y=dfstation18month12["PM25"], name=month[11],))
    fig18.update_layout(title_text="for station 18",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig19 = go.Figure()
    fig19.add_trace(go.Box(y=dfstation19month1["PM25"], name=month[0],))
    fig19.add_trace(go.Box(y=dfstation19month2["PM25"], name=month[1],))
    fig19.add_trace(go.Box(y=dfstation19month3["PM25"], name=month[2],))
    fig19.add_trace(go.Box(y=dfstation19month4["PM25"], name=month[3],))
    fig19.add_trace(go.Box(y=dfstation19month5["PM25"], name=month[4],))
    fig19.add_trace(go.Box(y=dfstation19month6["PM25"], name=month[5],))
    fig19.add_trace(go.Box(y=dfstation19month7["PM25"], name=month[6],))
    fig19.add_trace(go.Box(y=dfstation19month8["PM25"], name=month[7],))
    fig19.add_trace(go.Box(y=dfstation19month9["PM25"], name=month[8],))
    fig19.add_trace(go.Box(y=dfstation19month10["PM25"], name=month[9],))
    fig19.add_trace(go.Box(y=dfstation19month11["PM25"], name=month[10],))
    fig19.add_trace(go.Box(y=dfstation19month12["PM25"], name=month[11],))
    fig19.update_layout(title_text="for station 19",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig20 = go.Figure()
    fig20.add_trace(go.Box(y=dfstation20month1["PM25"], name=month[0],))
    fig20.add_trace(go.Box(y=dfstation20month2["PM25"], name=month[1],))
    fig20.add_trace(go.Box(y=dfstation20month3["PM25"], name=month[2],))
    fig20.add_trace(go.Box(y=dfstation20month4["PM25"], name=month[3],))
    fig20.add_trace(go.Box(y=dfstation20month5["PM25"], name=month[4],))
    fig20.add_trace(go.Box(y=dfstation20month6["PM25"], name=month[5],))
    fig20.add_trace(go.Box(y=dfstation20month7["PM25"], name=month[6],))
    fig20.add_trace(go.Box(y=dfstation20month8["PM25"], name=month[7],))
    fig20.add_trace(go.Box(y=dfstation20month9["PM25"], name=month[8],))
    fig20.add_trace(go.Box(y=dfstation20month10["PM25"], name=month[9],))
    fig20.add_trace(go.Box(y=dfstation20month11["PM25"], name=month[10],))
    fig20.add_trace(go.Box(y=dfstation20month12["PM25"], name=month[11],))
    fig20.update_layout(title_text="for station 20",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig21 = go.Figure()
    fig21.add_trace(go.Box(y=dfstation21month1["PM25"], name=month[0],))
    fig21.add_trace(go.Box(y=dfstation21month2["PM25"], name=month[1],))
    fig21.add_trace(go.Box(y=dfstation21month3["PM25"], name=month[2],))
    fig21.add_trace(go.Box(y=dfstation21month4["PM25"], name=month[3],))
    fig21.add_trace(go.Box(y=dfstation21month5["PM25"], name=month[4],))
    fig21.add_trace(go.Box(y=dfstation21month6["PM25"], name=month[5],))
    fig21.add_trace(go.Box(y=dfstation21month7["PM25"], name=month[6],))
    fig21.add_trace(go.Box(y=dfstation21month8["PM25"], name=month[7],))
    fig21.add_trace(go.Box(y=dfstation21month9["PM25"], name=month[8],))
    fig21.add_trace(go.Box(y=dfstation21month10["PM25"], name=month[9],))
    fig21.add_trace(go.Box(y=dfstation21month11["PM25"], name=month[10],))
    fig21.add_trace(go.Box(y=dfstation21month12["PM25"], name=month[11],))
    fig21.update_layout(title_text="for station 21",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')

    fig22 = go.Figure()
    fig22.add_trace(go.Box(y=dfstation22month1["PM25"], name=month[0],))
    fig22.add_trace(go.Box(y=dfstation22month2["PM25"], name=month[1],))
    fig22.add_trace(go.Box(y=dfstation22month3["PM25"], name=month[2],))
    fig22.add_trace(go.Box(y=dfstation22month4["PM25"], name=month[3],))
    fig22.add_trace(go.Box(y=dfstation22month5["PM25"], name=month[4],))
    fig22.add_trace(go.Box(y=dfstation22month6["PM25"], name=month[5],))
    fig22.add_trace(go.Box(y=dfstation22month7["PM25"], name=month[6],))
    fig22.add_trace(go.Box(y=dfstation22month8["PM25"], name=month[7],))
    fig22.add_trace(go.Box(y=dfstation22month9["PM25"], name=month[8],))
    fig22.add_trace(go.Box(y=dfstation22month10["PM25"], name=month[9],))
    fig22.add_trace(go.Box(y=dfstation22month11["PM25"], name=month[10],))
    fig22.add_trace(go.Box(y=dfstation22month12["PM25"], name=month[11],))
    fig22.update_layout(title_text="for station 22",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')


    fig23 = go.Figure()
    fig23.add_trace(go.Box(y=dfstation23month1["PM25"], name=month[0],))
    fig23.add_trace(go.Box(y=dfstation23month2["PM25"], name=month[1],))
    fig23.add_trace(go.Box(y=dfstation23month3["PM25"], name=month[2],))
    fig23.add_trace(go.Box(y=dfstation23month4["PM25"], name=month[3],))
    fig23.add_trace(go.Box(y=dfstation23month5["PM25"], name=month[4],))
    fig23.add_trace(go.Box(y=dfstation23month6["PM25"], name=month[5],))
    fig23.add_trace(go.Box(y=dfstation23month7["PM25"], name=month[6],))
    fig23.add_trace(go.Box(y=dfstation23month8["PM25"], name=month[7],))
    fig23.add_trace(go.Box(y=dfstation23month9["PM25"], name=month[8],))
    fig23.add_trace(go.Box(y=dfstation23month10["PM25"], name=month[9],))
    fig23.add_trace(go.Box(y=dfstation23month11["PM25"], name=month[10],))
    fig23.add_trace(go.Box(y=dfstation23month12["PM25"], name=month[11],))
    fig23.update_layout(title_text="for station 23",showlegend=True,xaxis_title="month", yaxis_title="PM2.5", autotypenumbers='convert types')



    app = dash.Dash()

    fig_names = ['fig1', 'fig2', 'fig3', 'fig4', 'fig5', 'fig6', 'fig7', 'fig8', 'fig9', 'fig10', 'fig11', 'fig12', 'fig13', 'fig14', 'fig15'
                , 'fig16', 'fig17', 'fig18', 'fig19', 'fig20', 'fig21', 'fig22', 'fig23']
    fig_dropdown = html.Div([
        dcc.Dropdown(
            id='fig_dropdown',
            options=[{'label': x, 'value': x} for x in fig_names],
            value=None
        )])
    fig_plot = html.Div(id='fig_plot')
    app.layout = html.Div([fig_dropdown, fig_plot])

    @app.callback(
    dash.dependencies.Output('fig_plot', 'children'),
    [dash.dependencies.Input('fig_dropdown', 'value')])
    def update_output(fig_name):
        return name_to_figure(fig_name)

    def name_to_figure(fig_name):
        figure = go.Figure()
        if fig_name == 'fig1':
            figure=fig1
        elif fig_name == 'fig2': 
            figure=fig2
        elif fig_name == 'fig3': 
            figure=fig3
        elif fig_name == 'fig4': 
            figure=fig4
        elif fig_name == 'fig5': 
            figure=fig5
        elif fig_name == 'fig6': 
            figure=fig6
        elif fig_name == 'fig7': 
            figure=fig7
        elif fig_name == 'fig8': 
            figure=fig8
        elif fig_name == 'fig9': 
            figure=fig9
        elif fig_name == 'fig10': 
            figure=fig10
        elif fig_name == 'fig11': 
            figure=fig11
        elif fig_name == 'fig12': 
            figure=fig12
        elif fig_name == 'fig13': 
            figure=fig13
        elif fig_name == 'fig14': 
            figure=fig14
        elif fig_name == 'fig15': 
            figure=fig15
        elif fig_name == 'fig16': 
            figure=fig16
        elif fig_name == 'fig17': 
            figure=fig17
        elif fig_name == 'fig18': 
            figure=fig18
        elif fig_name == 'fig19': 
            figure=fig19
        elif fig_name == 'fig20': 
            figure=fig20
        elif fig_name == 'fig21': 
            figure=fig21
        elif fig_name == 'fig22': 
            figure=fig22
        elif fig_name == 'fig23': 
            figure=fig23
        return dcc.Graph(figure=figure)

    app.run_server(debug=True, use_reloader=False)

    return render(request, "graphs/boxPlotTwo.html")#http://127.0.0.1:8050


def boxPlotThree(request):
    import pandas as pd
    import plotly.express as px
    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Input, Output

    app = dash.Dash(__name__)

    data = [['Blue',20],['Red ',12],['Green',33]]
    df = pd.DataFrame(data,columns=['Color','Number'])

    data1 = [['A',10,88],['B ',50,45],['C',25,120]]
    df1 = pd.DataFrame(data1,columns=['Letter','Column1','Column2'])

    app.layout = html.Div(children=[
        html.H1(children='Colors and Letters', style={'text-align': 'center'}),
        html.Div(children='Color', style={'text-align': 'center'}),

        html.Div([
            html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'graph1', 'value': 'graph1'},
                    {'label': 'graph2', 'value': 'graph2'},
                        ],
                value='graph1',
                style={"width": "60%"}),

        html.Div(dcc.Graph(id='graph')),        
            ]),

    ])

    @app.callback(
        Output('graph', 'figure'),
        [Input(component_id='dropdown', component_property='value')]
    )
    def select_graph(value):
        if value == 'graph1':
            fig = px.bar(df, x=df['Color'], y=df['Number'])
            return fig
        else:
            fig1 = px.line(x=df1['Letter'], y=df1['Column1'], color=px.Constant('Column1'),
                         labels=dict(x='Letter', y='Column1', color='Letter'))
            fig1.add_bar(x=df1['Letter'], y=df1['Column2'], name='Letter')
            return fig1

    if __name__ == '__main__':
        app.run_server(debug=True)
        #Season-Wise time based AQI data visualization using box plot
    return render(request, "graphs/boxPlotThree.html")


def routeWise(request):
    #Season-Wise time based AQI data visualization using box plot
    return render(request, "graphs/routeWise.html")