from django.shortcuts import redirect, render
from .models import * 
from .forms import *
# Create your views here.

def company(request):
    company = Company.objects.all()
    ctx = {'company': company}
    return render(request, 'home.html', ctx)


def employee(request, company_name):
    employee = Employee.objects.filter(company__name=company_name)
    ctx = {'employee': employee}
    return render(request, 'employee.html', ctx)

def add_company(request):
    if request.method == "POST":
        form = addCompanyForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('myapp:home')
        else :
            pass
    else:
        form = addCompanyForm()
        ctx = {'form': form}
        return render(request, 'add_company.html', ctx)




def add_employee(request , company_name):
    if request.method == "POST":
        form = addEmployeeForm(request.POST)
        if form.is_valid():
          employee = form.save(commit=False)
          employee.company = Company.objects.get(name = company_name)
          print('--------______----------->>>>>>>>',request.META['HTTP_REFERER'])
          employee.save()
          return redirect(f'/{company_name}')
    else:
        form = addEmployeeForm()
        ctx = {'form': form}
        return render(request, 'add_employee.html', ctx)

def update_company(request, company_name):
    if request.method == 'POST':
        inst = Company.objects.get(name = company_name)
        form = addCompanyForm(request.POST or None, instance = inst)
        if form.is_valid():
            form.save()
            return redirect(f'myapp:home')
        else: 
            pass

    else:
        inst = Company.objects.get(name = company_name)
        form = addCompanyForm(request.POST or None, instance = inst)
        ctx = {'form': form}
        return render(request, 'update_company.html', ctx)

def delete_company(request, company_name):
    company = Company.objects.get(name=company_name)
    company.delete()
    return redirect(f'myapp:home')