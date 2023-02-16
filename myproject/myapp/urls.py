from . import views
from django.urls import path
app_name = 'myapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
    path('form/', views.form, name='form'),
    path('application/', views.application, name='application'),
    path('logout/', views.logout, name='logout')

]