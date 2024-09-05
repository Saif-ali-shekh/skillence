from django.shortcuts import render
from django.views import View

# Create your views here.


from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from App_Models.models import *
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from asgiref.sync import sync_to_async,async_to_sync
from instamojo_wrapper import Instamojo

@sync_to_async
def send_otp_email(email, otp):
    print("i mam in mail ")
    subject = 'Your OTP Code'
    message = f'Your OTP code is {otp}. It is valid for 10 minutes.'
    email = EmailMessage(subject, message, to=[email])
    email.send()


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
            if  not CustomBaseUser.objects.filter(email=email).exists():
                
                if email and password:
                    user =CustomBaseUser.objects.create_user(email=email,name=name,password=password)
                    user.generate_otp()
                    user.save()
                    async_to_sync(send_otp_email)(user.email, user.otp)
                    print('Otp send to your mail')
                    messages.success(request, 'Otp send to your mail')
                    request.session['email']=email
                    one=request.session.get(email)
                    print(one)
                    return redirect('verify-otp')
                else:
                    messages.error(request, 'Please correct the errors below.')
            else:
                    messages.error(request, 'Email alrady exiists')
                
        except Exception as e:
            print("error -----------", e)
            messages.error(request, f'An error occurred: {str(e)}')
        return render(request,'interview/python.html' )
    
class VerifyOTPView(View):
    template_name = 'base/verify_otp.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        otp = request.POST.get('otp')
        email = request.session.get('email')
        print(email)
        try:
            user = CustomBaseUser.objects.get(email=email)
            if user.verify_otp(otp):
                user.is_otp_verify=True
                user.save()
                messages.success(request,"Account created successfully.")
                return redirect('python-interview')
            else:
                messages.error(request, 'Invalid OTP or OTP expired.')
        except CustomBaseUser.DoesNotExist:
            messages.error(request, 'User does not exist.')
        return render(request, self.template_name)
    
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
            print(email)
            if CustomBaseUser.objects.filter(email=email).exists():
                user=CustomBaseUser.objects.filter(email=email).first()
                if  not user.is_otp_verify:
                    messages.error(request, "Otp not verified!")
                    return redirect('verify-otp')
                user =authenticate(request,email=email, password=password)
                if user:
                    messages.success(request, "Login Successfull")
                    return render(request, 'interview/python.html')
                messages.error(request, "Invalid username/password")
                return render(request , self.template_name)
        except Exception as e:
            print(e)
            messages.error(request, "Something went wrong")
            return render(request, self.template_name)
        
        
class Logout(View):
    template_name ='base/login.html'
    def post(self ,request):
        user =request.user
        print(user)
        if user:
            try:
                user.is_active=False
                user.save() 
                print("i am in logout")
                messages.success(request, "Logout Successfull")
                return render(request, self.template_name)
                
            except Exception as e:
                print("logout")
                messages.error(request, "Something went wrong")
                return render(request, self.template_name)
            
    
 
class PythonInterview(View):
    
    template_name ='interview/python.html' 
    def get(self, request):
        try:
            return render(request, self.template_name)
        except:
            
            return render(request ,self.template_name)


###############################################################
###############################################################
# # pAYMENT METHODS

# from django.conf import settings
# from instamojo_wrapper import Instamojo

# class PaymentView(View):
#     template_name ="payment/buyme.html"
#     def get(self, request):
#         return render(request, self.template_name)
    
#     def post(self, request):
#         print("i am also iin  payment")
#         api = Instamojo(api_key=settings.API_KEY, auth_token=settings.AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/' )
#         print(api)
#         response = api.payment_request_create(
#             amount='100',
#             purpose='skillence testing',
#             send_email=True,
#             email="saifalishekh980@gmail.com",
#             redirect_url="http://127.0.0.1:8000/signup/"
#             )
#         print("response is ",response)
#         return render(request, "payment/success.html")