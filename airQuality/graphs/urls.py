"""airQuality URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from signup.views import signaction
from login.views import loginaction
#from graphs.views import lineCharts
from . import views
from django.conf.urls.static import static
from django.conf import settings
#from graphs.views import csvUpload
#from graphs.models import FilesUpload
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('signup/',signaction),
    #path('login/',loginaction),
    #path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('lineCharts/', views.lineCharts, name='lineCharts'),
    
    path('multipleBoxPlot/', views.multipleBoxPlot, name='multipleBoxPlot'), 
    path('scatterPlotWithLineGraph/', views.scatterPlotWithLineGraph, name='scatterPlotWithLineGraph'),
    
    path('multipleLineCharts/', views.multipleLineCharts, name='multipleLineCharts'),
    
    path('lineChartsWithDots/', views.lineChartsWithDots, name='lineChartsWithDots'),
    
    path('barChartWithLines/', views.barChartWithLines, name='barChartWithLines'),

    #path('country/', views.country, name='country'),
    path('country2/', views.country2, name='country2'),

    #path('csvUpload/', csvUpload, name='csvUpload'),
    #path('csvUpload/', csvUpload, name='csvUpload')
    
]
