from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),

    #Welcome_Page
    path("", include("apps.welcome_page.urls")),

    #Doctor
    path("auth_doctor/", include("apps.auth_doctor.urls")), # Auth routes - login / register
    path("doctor/", include("apps.doctor.urls"))             # UI Kits Html files

    # #Patient
    # path("", include("apps.auth_patient.urls")), # Auth routes - login / register
    # path("", include("apps.patient.urls"))             # UI Kits Html files
]
