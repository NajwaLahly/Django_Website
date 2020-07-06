from django.shortcuts import render


def sorting_home(request):
    return render(request, 'sorting/sorting_home.html')
