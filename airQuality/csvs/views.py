from fileinput import filename
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import os
import glob
from django.core.files.storage import FileSystemStorage
import os
import pandas as pd
from glob import iglob
import fnmatch
import os.path
import glob

#from .forms import CsvModelForm
#from .models import Csv

# Create your views here.

#def upload_file_view(request):
#    form = CsvModelForm(request.POST or None, request.FILES or None)
#    if form.is_valid():
#        form.save()
#        form= CsvModelForm()
#        obj = Csv.objects.get(activated = False)
#    return(request, 'csvs/base.html', {'form': form})

def upload(request):
    if request.method=="POST":
        file = request.FILES["myFile"]
        #print(file)
        if file.name.endswith('.csv'):
            savefile= FileSystemStorage()
            name = savefile.save(file.name, file)

            d= os.getcwd() #getCurrent Directory
            file_directory = d + '\media\\' +name

            readfile(file_directory)
        #csv = pd.read_csv(file)
        #print(csv.head())
        #arr = csv 
        
    return render(request, "csvs/fileupload.html")

FOLDER_PATH = r'C:\\Users\\dellG15\\Documents\\CSE303_Database_Project\\airQuality\\media'
def readfile(filename):
    my_file = pd.read_csv(filename, sep=',', engine='python')
    #my_file = pd.read_csv(filename, sep='[:;,_|#]', engine='python')
    
    data = pd.DataFrame(data=my_file, index=None)
    #pth = "myfile"
    #print(list(map(path.basename,iglob(pth+"*.mkv"))))
    #
    #
    #print([path.basename(f) for f in  iglob(pth+"*.mkv")])

    print(filename)
    listdir(FOLDER_PATH)
    print(data);


def listdir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        print('File Name: '+ fileName)
        if(fileName=="myfile.csv"):

            print("I found your file")


if __name__ == '__main__':
    listdir(FOLDER_PATH)