from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ("<h1> Welcom to index app2</h1>")

def sample2(request):
    return render(request,"sample2.html")