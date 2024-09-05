
from django.urls import path
from .views import *

urlpatterns = [
    path('', PythonInterview.as_view(), name='python-interview'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LoginView.as_view(), name='logout'),
    # path('payment/', PaymentView.as_view(), name='payment'),  #delete payment  template , view when it is not used
   
]
