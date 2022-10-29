from django.contrib.auth.models import User
from django.shortcuts import render

from models_1.web.models import Employee, Department


def index(request):
    employees = Employee.objects.all()
    employees_2 = Employee.objects.all()
    # # 'employees' is empty QuerySet
    # # employees_list = list(employees)
    # print(list(Employee.objects.all()))
    # print(list(Department.objects.all()))
    # # print(employees_list)
    # print(employees)

    context = {
        'employees': employees,
        'employees_2': employees_2,

    }

    return render(request, 'index.html', context)