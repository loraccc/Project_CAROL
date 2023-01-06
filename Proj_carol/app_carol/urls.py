from django.urls import include ,path
from . import views

urlpatterns =[
    #person 
    path("variety/",views.variety_index,name="variety.index"),
    path("variety/show/<int:id>/",views.variety_show,name="variety.show"),
    path("variety/edit/<int:id>/",views.variety_edit,name="variety.edit"),
    path("variety/create/",views.variety_create,name="variety.create"),
    path("variety/delete/<int:id>/",views.variety_delete,name="variety.delete"),
    #users
    path("person/login/", views.Person_login, name="person.login"),
    path("person/logout/", views.person_logout, name="person.logout"),
    path("person/register/", views.person_register,name="person.register")
    ]
