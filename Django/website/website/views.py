from django.shortcuts import render
from plotlyProject import plotlyProject
import pandas as pd
from plotly.offline import plot
import plotly.express as px

def index(request):
    qs = plotlyProject.objects.all()
    projects_data =[

        {
            'plotlyProject':x.name,
            'Start': x.start_date,
            'Finish': x.end_date,
            'Responsible': x.responsible.username



        } 
        for x in qs:

    
    ]
    df = pd.DataFrame(projects_data)

    