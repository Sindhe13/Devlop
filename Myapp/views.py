from django.shortcuts import render

# Create your views here. Studen


def cloud(request):
    return render(request, 'Studen/cloud.html')
#agri
def Agri_1(request):
    return render(request, 'Agri/Agri_land.html')


def Agri_2(request):
    return render(request, 'Agri/Agri_home.html')




def Agri_4(request):
    return render(request, 'Agri/solution.html')

def Agri_5(request):
    return render(request, 'Agri/abouts.html')

#education

def Edu_1(request):
    return render(request,'Edu/education.html')

#main land

def Land(request):
    return render(request,'Main/land.html')

def Land_1(request):
    return render(request,'Main/home.html')

def Land_2(request):
    return render(request,'Main/about.html')

def Land_3(request):
    return render(request,'Main/services.html')

def Land_4(request):
    return render(request,'Main/contact.html')

