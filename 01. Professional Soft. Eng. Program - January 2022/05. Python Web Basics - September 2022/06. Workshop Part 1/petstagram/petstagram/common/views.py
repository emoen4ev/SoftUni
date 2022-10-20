from django.shortcuts import render


def index(reques):
    return render(reques, 'common/home-page.html')