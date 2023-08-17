from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    if request.method == "POST":
        print(request.GET.values())
    return render(request,'home.html')
    #return HttpResponse("Home PAge")