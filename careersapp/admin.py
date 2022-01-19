from django.contrib import admin

from .models import Careers #, Jobs

@admin.register(Careers)
class CareersAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['id','full_name','email','phone_number']

# @admin.register(Jobs)
# class JobsAdmin(admin.ModelAdmin):
#     class Meta:
#         list_display = ['id','job','job_description']