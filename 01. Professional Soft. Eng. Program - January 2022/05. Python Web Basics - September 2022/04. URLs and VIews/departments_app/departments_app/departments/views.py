from django.shortcuts import render


def sample_view(request, *args, **kwargs):
    print(f"args= {args}")
    print(f"kwargs= {kwargs}")