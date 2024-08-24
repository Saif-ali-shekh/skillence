from django.shortcuts import render
from django.views import View

# Create your views here.


from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from App_Models.models import *
from django.contrib.auth import authenticate


class SignUpView(View):
    template_name ='base/signup.html'
    def get(self, request):
        try:
            return render(request, self.template_name)   
        except:
            return render(request, self.template_name)

    def post(self, request):
        try:
            print("I am in 1")
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if email and password:
                obj =CustomBaseUser.objects.create_user(email=email,name=name,password=password)
                obj.save()
                print('login seccessfull')
                messages.success(request, 'Account created successfully!')
                return render(request, self.template_name)   
            else:
                messages.error(request, 'Please correct the errors below.')
        except Exception as e:
            print("error -----------", e)
            messages.error(request, f'An error occurred: {str(e)}')
        return render(request,'interview/python.html' )
    
class LoginView(View):
    template_name ='base/login.html'
    
    def get(self, request):
        try:
            return render(request, self.template_name)
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return render(request,'interview/python.html' )
    def post(self,request):
        try:
            email =request.POST['email']
            password =request.POST['password']            
            user =authenticate(request,email=email, password=password)
            if user:
                messages.success(request, "Login Successfull")
                return render(request, 'interview/python.html')
            messages.error(request, "Invalid username/password")
            return render(request , self.template_name)
        except Exception as e:
            messages.error(request, "Something went wrong")
            return render(request, self.template_name)
            
    

class PythonInterview(View):
    
    template_name ='interview/python.html'
    def get(self, request):
        try:
            return render(request, self.template_name)
        except:
            
            return render(request ,self.template_name)
        