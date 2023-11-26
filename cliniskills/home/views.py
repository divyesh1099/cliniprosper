from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# Create your views here.
def index(request):
    context={}
    return render(request, 'home/index.html', context)

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')  # Redirect to the home page or any other page
        else:
            # Return an 'invalid login' error message
            return render(request, 'home/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'home/login.html')

def logout_request(request):
    logout(request)
    return redirect('home:index')  # Redirect to the home page or any other page after logout

def password_reset(request):
    return render(request, 'home/password_reset.html')

def new_password(request):
    return render(request, 'home/new_password.html')

def signup(request):
    return render(request, 'home/signup.html')

def services(request):
    return render(request, 'home/services.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')