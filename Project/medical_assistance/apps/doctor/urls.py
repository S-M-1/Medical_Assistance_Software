from django.urls import path, re_path
from apps.doctor import views

urlpatterns = [

    # The home page
    path('', views.index, name='doctor'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
