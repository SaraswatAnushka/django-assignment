
from django.urls import path,include
from . import views
from files import views as file_views


urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/', views.user_logout, name='logout'),  
    path('fi/',file_views.index,name='fi'),
   
]