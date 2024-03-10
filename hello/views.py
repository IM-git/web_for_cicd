from django.http import HttpResponse


def index(request):
    return HttpResponse("Test Web-Project for the CI/CD.")
