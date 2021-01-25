from django.shortcuts import render
from django.http import request
from django.http.response import HttpResponse
import templates


def index(request):
    return render(request, 'login.html')
