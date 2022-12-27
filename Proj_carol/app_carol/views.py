from django.shortcuts import render

def variety_index(request):
    return render(request,"variety/index.html")

def variety_show(request):
    return render(request,"variety/show.html")

def variety_edit(request):
    return render(request,"variety/edit.html")
    
def variety_create(request):
    return render(request,"variety/create.html")
    
    #PERSON
def person_login(request):
    return render(request,"person/login.html")
def person_register(request):
    return render(request,"person/register.html")