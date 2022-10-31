from django.shortcuts import render, redirect

from CarCollection.CarCollectionWeb.models import Profile

'''
•	http://localhost:8000/ - index page
•	http://localhost:8000/profile/create - profile create page
•	http://localhost:8000/catalogue/ - catalogue page
•	http://localhost:8000/car/create/ - car create page
•	http://localhost:8000/car/<car-id>/details/ - car details page
•	http://localhost:8000/car/<car-id>/edit/ - car edit page
•	http://localhost:8000/car/<car-id>/delete/ - car delete page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - profile delete page

'''


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('index without profile')

    return render(request, 'home/index.html')


def index_without_profile(request):
    return render(request, 'home/index_without_profile.html')


def create_profile(request):
    return render(request, 'profile/profile-create.html')


def catalogue(request):
    return render(request, 'car/catalogue.html')


def create_car(request):
    return render(request, 'car/car-create.html')


def details_car(request, pk):
    return render(request, 'car/car-details.html')


def edit_car(request, pk):
    return render(request, 'car/car-edit.html')


def delete_car(request, pk):
    return render(request, 'car/car-delete.html')


def details_profile(request):
    return render(request, 'profile/profile-details.html')


def edit_profile(request):
    return render(request, 'profile/profile-edit.html')


def delete_profile(request):
    return render(request, 'profile/profile-delete.html')