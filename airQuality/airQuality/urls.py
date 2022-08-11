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
import csvs 
from signup.views import signaction
from login.views import loginaction
from graphs.views import lineCharts
from django.conf.urls.static import static
from django.conf import settings
from csvs.views import upload
from csvs.views import upload


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signaction),
    path('',loginaction),
    path('login',loginaction),
    path('upload/', include('csvs.urls')),
    
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    #path('lineCharts/', lineCharts.as_view(), name="lineCharts"),
    #path('graphs/', include('lineCharts')),
    path('lineCharts/', include('graphs.urls')),
    
    path('multipleBoxPlot/', include('graphs.urls')),
    path('scatterPlotWithLineGraph/', include('graphs.urls')),
    
    path('multipleLineCharts/', include('graphs.urls')),
    
    path('lineChartsWithDots/', include('graphs.urls')),
    
    path('barChartWithLines/', include('graphs.urls')),

    #path('country/', include('graphs.urls')),
    path('country2/', include('graphs.urls')),
    #path('csvs/', include('csvs.urls', namespace='csvs')),
    #path('csvUpload/', include('graphs.urls')),
    path('boxPlotOne/', include('graphs.urls')),
    path('boxPlotTwo/', include('graphs.urls')),
    path('boxPlotThree/', include('graphs.urls')),
    path('routeWise/', include('graphs.urls')),
    
   # path('upload/', include('csvs.upload')),
    


    
]

urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
