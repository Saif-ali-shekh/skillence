from django.urls import path
from .views import *

urlpatterns = [
    path('', ContentDashboardViews.as_view(), name='content-dashboard'),
   
]
