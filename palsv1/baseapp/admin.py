from django.contrib import admin
from .models import Course,Subunit,Question

# Register your models here.
admin.site.register(Course)
admin.site.register(Subunit)
admin.site.register(Question)
