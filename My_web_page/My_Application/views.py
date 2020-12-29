from django.shortcuts import render
from My_Application.models import About,Contact,Cource,Python,Django,Datascience,Bigdata,Html_css

# Create your views here.
def home(request):
    return render (request,'home.html')

def about(request):
    data = About.objects.all()
    dict1 = {'data':data}
    return render (request,'about.html',dict1)

def cource(request):
    data2=Cource.objects.all()
    dict3={'data2':data2}
    return render (request,'cource.html',dict3)

def contact(request):
    data1=Contact.objects.all()
    dict2={'data1':data1}
    return render (request,'contact.html',dict2)

def python(request):
    data3 = Python.objects.all()
    dict4 = {'data3':data3}
    return render(request,'python.html',dict4)

def django(request):
    data4 = Django.objects.all()
    dict5 = {'data4': data4}
    return render(request, 'django1.html', dict5)

def datascience(request):
    data5 = Datascience.objects.all()
    dict6 = {'data5': data5}
    return render(request, 'datascience.html', dict6)

def bigdata(request):
    data = Bigdata.objects.all()
    dict7 = {'data': data}
    return render(request,'bigdata.html',dict7)

def html_css(request):
    data7 = Html_css.objects.all()
    dict8 = {'data7': data7}
    return render(request,'html_css.html',dict8)

def book(request):
    return render(request,'book.html')

def register(request):
    name1=request.GET['surname']+" "+request.GET['firstname']
    cname1=request.GET['cource']
    dict1={'name':name1,'cname':cname1}
    return render(request,'register.html',dict1)