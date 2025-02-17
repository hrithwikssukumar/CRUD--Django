
from django.urls import path
from .import views

urlpatterns = [
    path('employee/',views.employee_list,name='employeelist'),
    path('employeeform/',views.employee_form,name='employeeform')
]
