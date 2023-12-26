from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class GreetingView(View):
    def get(self, request):
        return HttpResponse("Hello, World")


def index(request):
    return HttpResponse("<h1>Home</h1>")
