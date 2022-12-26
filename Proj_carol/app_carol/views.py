from django.shortcuts import render

def variety_index(request):
    return render(request,"variety/index.html")