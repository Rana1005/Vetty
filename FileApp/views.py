from fileinput import filename
import io
from django.shortcuts import render,HttpResponse
from matplotlib.style import context
from django.core.files import File
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
# Create your views here.
def file(request,filename="file1.txt"):

    fileurl='C:\\Users\\codin\\OneDrive\\Desktop\\DjangoPojects\\VentTask\\FileProject\\static\\'+filename
    print(fileurl)
    f = open(fileurl, 'r',encoding="utf-8",errors='ignore')
    mytext=""
    if f.mode == 'r':
       contents=f.readlines()
             
    # print (contents)
    try:
        startno=int(request.GET['startline'])
        endno=int(request.GET['endline'])
        print(startno)
        mytext=mytext.join(contents[startno:endno+1])
    except:
        mytext=mytext.join(contents)

    
    context={
        "variable":mytext
    }
    return render(request,"file.html",context=context)



