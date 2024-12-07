from django.shortcuts import render

# Create your views here.
def dresses(request):
    return render(request,'dresses.html')