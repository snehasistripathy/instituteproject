from django.contrib import admin

from .models import courses



class AdminCourse(admin.ModelAdmin):
    list_display = ['courses_name', 'duresion','start_date','fee','timeing','trainer_name','trainer_exp']

admin.site.register(courses,AdminCourse)