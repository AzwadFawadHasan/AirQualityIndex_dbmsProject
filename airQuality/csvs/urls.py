from django.urls import path  
#from .views import upload_file_view
#from .views import upload
from . import views
#app_name = 'csvs'

urlpatterns = [
    #path('', upload_file_view, name='upload-view'),
    path('upload/',views.upload, name='upload'),
]
