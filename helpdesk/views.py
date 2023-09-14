from django.shortcuts import render

# Create your views here.

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "admin" and password == "admin":
            return render(request, 'helpdesk/home.html')
        else:
            return render(request, 'helpdesk/login.html')

    return render(request, 'helpdesk/login.html')