from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect


# Create your views here.


class ContentDashboardViews(View):
    template_name= 'content/base_content.html'
    def get(self, request):
        try:
            print("hello")
        #   if request.user.is_authenticated:
            return render(request ,self.template_name)
        except Exception as e:
            print('exception --------->', e)
            return redirect('content-dashboard')
        