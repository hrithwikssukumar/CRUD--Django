from django.shortcuts import render
from .forms import*
from .models import Employee

# Create your views here.
def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request,'employeelist.html',context)

def employee_form(request):
    if request.method == 'GET':
        form = EmployeeForm()
        return render(request,'employeeform.html',{'form':form})  
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeelist')
   


   

