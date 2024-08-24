from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomBaseUser)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Content)
# admin.site.register()