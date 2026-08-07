from django import forms
from .models import Booking
from datetime import date
class Booking_form(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        
        widgets = {
            'booking_date' : forms.DateInput(attrs = {'type' : 'date',"min": date.today().isoformat()})
        }
        
        labels = {
            'name' : 'Patient Name',
            'phone' : 'Phone Number',
            'email' : 'Email',
            'd_name' : 'Doctor Name',
            'booking_date' : 'Booking Date'
        }
        
# class Registration_form(forms.ModelForm):
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={"class": "form-control"})
#     )
#     class Meta:
#         model=Register
#         fields='__all__'
        
#         widgets = {
#             "fname": forms.TextInput(attrs={"class": "form-control"}),
#             "lname": forms.TextInput(attrs={"class": "form-control"}),
#             "email": forms.EmailInput(attrs={"class": "form-control"}),
#             "username": forms.TextInput(attrs={"class": "form-control"}),
#         }
        
#         labels = {
#             'fname' : 'First Name',
#             'lname' : 'Last Name',
#             'email' : 'Email',
#             'username' : 'User Name',
#             'password' : 'Password'
#         }
        
        
        # password = forms.CharField()
        
#new      
# class Login(forms.ModelForm):
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={"class": "form-control"})
#     )
#     class Meta:
#         model=Register
#         fields= ['username', 'password']
#         widgets = {
#             "username": forms.TextInput(attrs={"class": "form-control"}),
#         }
        
#         labels = {
#             'username' : 'User Name',
#             'password' : 'Password'
#         }
