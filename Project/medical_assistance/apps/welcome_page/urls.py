from django.urls import path, re_path
from apps.welcome_page import views

urlpatterns = [

    # The home page
    path('', views.homepage, name='welcome'),

]
