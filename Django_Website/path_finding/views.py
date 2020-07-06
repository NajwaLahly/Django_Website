from django.shortcuts import render


def path_finding_home(request):
    return render(request, 'path_finding/path_finding_home.html')