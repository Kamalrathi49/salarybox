from django.shortcuts import redirect, render
from .models import * 
from .forms import *
from django.contrib import messages #import messages

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
          messages.success(request, f"Your Company is added sucessfully!")
          return redirect('myapp:home')
        else :
             messages.error(request, f'Company name already exist!, Please try something else')
             return redirect('myapp:add-company')
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
          employee.save()
          messages.success(request, f" Your Employee '{employee.first_name} {employee.last_name}' is added sucessfully!")
          return redirect(f'/{company_name}')
        else:
            messages.error(request, f"Something went wrong!, Please try again")
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
            messages.success(request, f"Your Company '{company_name}' is updated sucessfully!")
            return redirect(f'myapp:home')
        else: 
            messages.error(request, f"Something went wrong!, Please try again")
            return redirect(f'myapp:home')

    else:
        inst = Company.objects.get(name = company_name)
        form = addCompanyForm(request.POST or None, instance = inst)
        ctx = {'form': form}
        return render(request, 'update_company.html', ctx)

def delete_company(request, company_name):
    company = Company.objects.get(name=company_name)
    company.delete()
    messages.success(request, f"Your Company '{company_name}' is removed sucessfully!")
    return redirect(f'myapp:home')


def update_employee(request, company_name, id):
    if request.method == 'POST':
        employee = Employee.objects.get(id = id)
        form = addEmployeeForm(request.POST or None, instance = employee)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your Employee '{employee.first_name} {employee.last_name}' is updated sucessfully!")
            return redirect(f'/{company_name}')
        else: 
            messages.error(request, f'Something went wrong!, Please try again')
            return redirect(f'/{company_name}')

    else:
        employee = Employee.objects.get(id = id)
        form = addEmployeeForm(request.POST or None, instance = employee)
        ctx = {'form': form}
        return render(request, 'update_employee.html', ctx)

def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.success(request, f"Your Employee'{employee.first_name} {employee.last_name}' is removed sucessfully!")
    return redirect(f'/{employee.company.name}')