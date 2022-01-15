from django.http import HttpResponse    
from django.shortcuts import render


def homepage(request):
    data={
        'title': 'HOME PAGE'
    }
    return render(request, "w_page/w_index.html",data)   #render(parameter,page_name, DICT_name)

def doctor_login(request):
    return render(request,"medical_login.html")