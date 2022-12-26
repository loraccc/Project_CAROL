from django.urls import path
from . import views

urlpatterns = [
    path("variety/",views.variety_index,name="variety.index")
]
