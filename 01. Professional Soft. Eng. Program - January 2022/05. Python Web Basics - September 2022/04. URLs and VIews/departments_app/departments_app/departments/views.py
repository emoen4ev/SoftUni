from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect


# def sample_view(request, *args, **kwargs):
#     print(f"args= {args}")
#     print(f"kwargs= {kwargs}")


# Without render
# def show_departments(request: HttpRequest, *args, **kwargs):
#     print(request.method)
#     print(request.GET)  # query params (?param1=value1&param2=value2)
#     print(request.POST)  # body of HTTP request
#     print(request.get_port())
#     print(request.get_host())
#     print(request.headers)
#     # body = f"args= {args}, kwargs= {kwargs}"

#     order_by = request.GET.get("order_by", "name")
#     body = f"path: {request.path}, args= {args}, kwargs= {kwargs}, order_by: {order_by}"
#     return HttpResponse(body)
#     # return HttpResponse()


def show_departments(request: HttpRequest, *args, **kwargs):
    context = {
        "method": request.method,
        "order_by": request.GET.get("order_by", "name"),
    }

    return render(request, "departments/all.html", context)


def show_department_details(request: HttpRequest, department_id):
    body = f"path: {request.path}, id: {department_id}"
    return HttpResponse(body)