from django.http import HttpResponse
from django.shortcuts import render


# def sample_view(request, *args, **kwargs):
#     print(f"args= {args}")
#     print(f"kwargs= {kwargs}")


def show_departments(request, *args, **kwargs):
    body = f"args= {args}, kwargs= {kwargs}"
    return HttpResponse(body)