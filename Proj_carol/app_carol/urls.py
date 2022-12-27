from django.urls import path
from . import views

urlpatterns =[
    #person 
    path("variety/",views.variety_index,name="variety.index"),
    path("variety/show/",views.variety_show,name="variety.show"),
    path("variety/edit/",views.variety_edit,name="variety.edit"),
    path("variety/create/",views.variety_create,name="variety.create"),
    #users
    path("person/login/", views.person_login, name="person.login"),
    path("person/register/", views.person_register,name="person.register")
    ]
