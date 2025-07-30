from django.shortcuts import render
from django.http import HttpResponse

def home(reuests):
    return HttpResponse('Hello World!')