from pydoc import doc
from xml.dom.minidom import Document
from django.shortcuts import render
from asyncio import tasks
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from django.views.generic.detail import DetailView
from django. views. generic. edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
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
from urllib3 import HTTPResponse

import csv, io;
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required


from .models import FilesUpload
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
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="air"
    )

    mycursor = mydb.cursor()

    #mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    csv_data = csv.reader(open('graphs/csvForLineGraph.csv'))
    sqlFormula = "INSERT INTO lineCharts(date,avgPM) VALUES (%s, %s)"
    

    for row in csv_data:
        mycursor.execute(sqlFormula, 
            row)

    #close the connection to the database.
    mydb.commit()
    #mycursor.close()
    sqlFormulaFetch ="SELECT date, avgPM from lineCharts"
    mycursor.execute(sqlFormulaFetch)
    myAllData = mycursor.fetchall();
    
    allDateData = [];
    allAvgPmData = [];
    allDateData2 = [];
    allAvgPmData2 = [];
    countFlag = 0
    
    for date, avgPm in myAllData:
        if countFlag==0:
            allDateData2.append(date)
            allAvgPmData2.append(avgPm)
            countFlag+=1;
        elif countFlag>=1:
        
        
            allDateData.append(date)
            allAvgPmData.append(avgPm)
        


    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']
    high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
    low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
    high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
    low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
    high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
    low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]

    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=allDateData, y=allAvgPmData, name='csvForLineGraph',
                             line=dict(color='firebrick', width=4)))
    #fig.add_trace(go.Scatter(x=month, y=low_2014, name = 'Low 2014',
    #                         line=dict(color='royalblue', width=4)))
    #fig.add_trace(go.Scatter(x=month, y=high_2007, name='High 2007',
    #                         line=dict(color='firebrick', width=4,
    #                              dash='dash') # dash options include 'dash', 'dot', and 'dashdot'
    #))
    #fig.add_trace(go.Scatter(x=month, y=low_2007, name='Low 2007',
    #                         line = dict(color='royalblue', width=4, dash='dash')))
    #fig.add_trace(go.Scatter(x=month, y=high_2000, name='High 2000',
    #                         line = dict(color='firebrick', width=4, dash='dot')))
    #fig.add_trace(go.Scatter(x=month, y=low_2000, name='Low 2000',
    #                         line=dict(color='royalblue', width=4, dash='dot')))

    # Edit the layout
    fig.update_layout(title='month vs avg PM 2.5',
                       xaxis_title='Month',
                       yaxis_title='avg Pm 2.5')


    fig.show()
    return render(request, 'graphs/lineCharts.html')


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

def scatterPlotWithLineGraph(request):
    df = px.data.tips()
    fig = px.scatter(df, x="total_bill", y="tip", facet_col="smoker", color="sex", trendline="ols")
    fig.show()

    results = px.get_trendline_results(fig)
    print(results)
    results.query("sex == 'Male' and smoker == 'Yes'").px_fit_results.iloc[0].summary()
    #this uses statmodels 
    # to install
    #python -m pip install statsmodels 
    return render(request, "graphs/multipleBoxPlot.html")

def multipleLineCharts(request):
    df = px.data.gapminder().query("continent == 'Oceania'")
    fig = px.line(df, x='year', y='lifeExp', color='country', markers=True)
    fig.show()
    return render(request, "graphs/multipleLineCharts.html")

def lineChartsWithDots(request):
    df = px.data.gapminder().query("country in ['Canada', 'Botswana']")
    fig = px.line(df, x="lifeExp", y="gdpPercap", color="country", text="year")
    fig.update_traces(textposition="bottom right")
    fig.show()
    return render(request, "graphs/lineChartsWithDots.html")



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
