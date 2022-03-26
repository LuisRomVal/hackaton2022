from django.http import HttpResponse


def index(request):
    return HttpResponse("bye, world :(")

