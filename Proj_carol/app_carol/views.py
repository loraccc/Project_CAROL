from django.shortcuts import render,redirect
from .forms import variety_info,Personloginform,Personregisterform
from .models import under_person,Person
from datetime import datetime


def variety_index(request):
    if not request.session.has.key("session_email"):
        return redirect("person.login")
    form=under_person()
    context={"form":form}
    return render(request,"variety/index.html",context)

def variety_show(request):
    if not request.session.has.key("session_email"):
        return redirect("person.login")
    data=under_person.objects.all() # UnderMODEL MA VAKO NAM
    context={"data":data}

    return render(request,"variety/show.html",context)

def variety_edit(request):
    if not request.session.has.key("session_email"):
        return redirect("person.login")
    data = under_person.objects.get(id=id)  #under class name
    context = {"data": data}
    return render(request,"variety/edit.html",context)
    
def variety_create(request):
    form=variety_info()              # forms ma vako CLASS name !
    context={"form":form}
    if request.method == "POST":
        item = under_person.objects.get(id=request.POST.get("id"))         # UNDERclass ko nam tanni
        user  =Person.objects.get(id=1) # PARENT CLASS
        item.title = request.POST.get("title")
        item.particular = request.POST.get("particular")
        item.lf = request.POST.get("lf")
        item.price = request.POST.get("price")
        item.quantity = request.POST.get("quantity")
        item.total = request.POST.get("total")
        item.added_at = datetime.now()
        item.user = user
        item.save()
        context.setdefault("msg","Variety Created Successfully!")
    return render(request, "variety/create.html",context)
def variety_update(request):
    if not request.session.has_key("session_email"):
        return redirect("person.login")
    if request.method == "POST":
        item_obj = variety_info.objects.get(id=request.POST.get("id"))
        user = Person.objects.get(id=1)
        item_obj.title = request.POST.get("title")
        item_obj.particular = request.POST.get("particular")
        item_obj.lf = request.POST.get("lf")
        item_obj.price = request.POST.get("price")
        item_obj.quantity = request.POST.get("quantity")
        item_obj.total = request.POST.get("total")
        item_obj.added_at = datetime.now()
        item_obj.user = user
        item_obj.save()
    return redirect("items.index")

def variety_delete(request, id):
    if not request.session.has.key("session_email"):
        return redirect("person.login")
    data = under_person.objects.get(id=id)
    data.delete()
    return redirect("items.index")
    
        #PERSON
def Person_login(request):          # url.PY ma vako NAME . views//
    form=Personloginform()          # forms class ko nam
    context={"form":form}
    if request.method=="POST":
        req_email=request.POST.get("email")
        req_password=request.POST.get("password")
        user=Person.objects.get(email="req_email")
        if Person.email==req_email and Person.password==req_password:
            request.session["session_email"]=Person.email
            return redirect ("variety.index")
        else:
            return redirect ("person.login")
    
    return render(request, "person/login.html",context)
    #try:
    #   return render(request, "person/login.html")
    #except:
    #    print("error")
    #finally:
    #    return render(request, "person/login.html"
def person_logout(request):
    if not request.session.has_key("session_email"):
        return redirect("person.login")
    del request.session["session_email"]
    return redirect("person.login")
def person_register(request):
    form = Personregisterform()
    context = {"form": form}
    if request.method =="POST":
        user= Person() # class ko nam
        user.first_name =request.POST["first_name"]
        user.last_name =request.POST["last_name"]
        user.age= request.POST["age"]
        user.email= request.POST["email"]
        user.password =request.POST["password"]
        user.added_at =request.POST["added_at"]
        user.save()
    return render(request, "person/register.html", context) # name of PATH "person/register.html"
    