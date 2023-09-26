from django.urls import path
from .views import login


#Rota para a página de login
urlpatterns = [
    path('login', login, name='login'),  
]

