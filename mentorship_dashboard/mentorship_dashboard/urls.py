from django.contrib import admin
from django.urls import path
from home_page.views import home, student_registration, mentor_registration, registration_success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/student/', student_registration, name='student_registration'),
    path('register/mentor/', mentor_registration, name='mentor_registration'),
    path('registration/success/', registration_success, name='registration_success'),
]
