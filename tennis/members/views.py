from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Doctors
from .forms import Booking_form 
from django.core.paginator import Paginator # - new
import requests  # --new
from datetime import datetime # --new
# Create your views here.
# def login(request): #new
#     if request.method=="POST":
#         form=Login(request.POST)
#         if form.is_valid():
#             return render(request, "index.html")
    
#     form=Login()   
#     f={
#         'form':form
#     }   
#     return render(request,"login.html",f)

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def booking(request):
    if request.method=="POST":
        form=Booking_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "confirmation.html")
    
    form=Booking_form()   
    f={
        'form':form
    }   
    return render(request,"booking.html",f)

def contact(request):
    return render(request,"contact.html")

def department(request):
    dept={
        'd':Department.objects.all()
    }
    return render(request,"department.html",dept)

def doctors(request):
    doct={
        'doc':Doctors.objects.all()
    }
    return render(request,"doctors.html",doct)

# - new
def doctors_list(request):
    doctor = Doctors.objects.all()

    paginator = Paginator(doctor, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(request, "doctors_list.html", {
        "page_obj": page_obj
    })

# --new
def weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        API_KEY = 'your_api_key_here'  # your_api_key_here
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        try:
            data = requests.get(url).json()
            context = {
            'city': city,
            'country_code': data['sys']['country'],
            'coordinate': f"{data['coord']['lon']} {data['coord']['lat']}",
            'temp': f"{data['main']['temp']} °C",
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'time': datetime.now().strftime("%A, %B %d %Y, %H:%M:%S %p")
            }
        except:
            context = {'error': 'City not found or API error'}
        return render(request, 'weather.html', context)
    return render(request, 'weather.html')








# def register(request):
#     if request.method=="POST":
#         form=Registration_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, "login.html")
    
#     form=Registration_form()   
#     f={
#         'form':form
#     }   
#     return render(request,"register.html",f)