from django.contrib import admin
from emp_app.models import *
# Register your models here.
admin.site.register(Department)
admin.site.register(Role)
class EmployeeDetails (admin.ModelAdmin):
    list_display=['first_name','last_name','department','salery','bonus','phone','hire_date','role','phone','hire_date']
admin.site.register(Employee,EmployeeDetails)