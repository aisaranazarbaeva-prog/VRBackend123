from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет! Это страница About Us.")
