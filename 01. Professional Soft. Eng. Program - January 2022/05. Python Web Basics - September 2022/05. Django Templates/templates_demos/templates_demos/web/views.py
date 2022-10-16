from django.shortcuts import render


def index(request):
    context = {
        'title': 'SoftUni Homepage',
    }

    return render(request, '', context)