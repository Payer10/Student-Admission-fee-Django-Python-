from django.urls import path
from .views import*

urlpatterns = [
    path('',login_page,name='login'),
    path('home/',home_page,name='home'),
    path('register/',register_page,name='register'),
    path('logout/',logout_pages,name='logout'),
    path('student_fee/',student_fee,name='student_fee'),
    path('student_fee/success/',success,name='success'),
    path('student_fee/fail/',fail,name='fail'),
]
