from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ("<h1> Welcom to index app1</h1>")

def sample1(request):
    return render(request,"sample1.html")