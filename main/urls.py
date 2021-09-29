from django.urls import path, re_path
from . import views



urlpatterns = [

    path('auth', views.autorization, name='auto'),
    path('', views.index, name='home'),
    path("other",views.other_page, name="other"),
    path("works", views.works, name="works"),
    path("images", views.images, name="images"),
]

