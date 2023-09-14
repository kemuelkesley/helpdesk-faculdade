from django.urls import path
from helpdesk.views import login

urlpatterns = [
    path('login', login, name='login')
]