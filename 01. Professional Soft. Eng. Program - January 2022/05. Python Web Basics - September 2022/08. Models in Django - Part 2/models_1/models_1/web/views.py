from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from models_1.web.models import Employee, Department, Project


def index(request):
    # employees = Employee.objects.all()
    employees = [e for e in Employee.objects.all() if e.department_id == 2]  # Slower
    # employees_2 = Employee.objects.all()
    # employees_2 = Employee.objects.filter(department_id=2) # Right way - Fastest
    employees_2 = Employee.objects\
        .filter(department_id=2) \
        .filter(age__gt=30) \
        .order_by('last_name', 'first_name')
    # employees_2 = Employee.objects \
    #     .filter(department__name='Engineering') \
    #     .filter(age__gt=30) \
    #     .order_by('last_name', 'first_name')

    # # 'employees' is empty QuerySet
    # # employees_list = list(employees)
    # print(list(Employee.objects.all()))
    # print(list(Department.objects.all()))
    # # print(employees_list)
    # print(employees)

    # 'get' returns an object, not QuerySet!
    # 'get' returns a single object and throws when none or multiple results
    # 'get' is 'eager' and does not return a QuerySet
    # 'get' is not 'lazy' as 'QuerySet', it executes immediately!
    # 'get' is primarily used for fetching by primary key
    department = Department.objects.get(pk=2)
    # print(department)

    get_object_or_404(Employee, level=Employee.LEVEL_REGULAR)

    Employee.objects.filter(level=Employee.LEVEL_SENIOR).first()

    context = {
        'employees': employees,
        'employees_2': employees_2,
        # 'department': Department.objects.get(pk=2)
        'department': department,

    }

    return render(request, 'index.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()

    # department_pk = 3
    # # When 'on_delete=models.RESTRICT' this must be done explicitly
    # # When 'on_delete=models.CASCADE' this is done explicitly
    # get_list_or_404(Employee, department_id=department_pk)\
    #     .delete()
    # get_object_or_404(Department, pk=department_pk).delete()

    # employee = get_object_or_404(Employee, pk=pk)
    # employee.delete()

    # # Deletes all projects with this criteria
    # Project.objects.filter()\
    #     .delete()

    # # Delete all projects
    # Project.objects.all()\
    #     .delete()

    return redirect('index')