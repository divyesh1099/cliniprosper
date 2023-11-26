from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .forms import EditProfileForm

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
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists', extra_tags='bg-red-100 text-red-700 border border-red-400')
                return redirect('home:signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered', extra_tags='bg-red-100 text-red-700 border border-red-400')
                return redirect('home:signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request, user)
                messages.success(request, 'Account created successfully', extra_tags='bg-green-100 text-green-700 border border-green-400')
                return redirect('home:index')
        else:
            messages.error(request, 'Passwords do not match', extra_tags='bg-red-100 text-red-700 border border-red-400')
            return redirect('home:signup')

    else:
        return render(request, 'home/signup.html')

def services(request):
    return render(request, 'home/services.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

@login_required
def view_profile(request):
    user = get_object_or_404(User, username=request.user.username)
    return render(request, 'home/view_profile.html', {'user': user})

@login_required
def request_delete_profile(request):
    if request.method == 'POST':
        # Logic to handle deletion request
        messages.success(request, 'Your profile deletion request has been sent to the admin.', extra_tags='bg-green-100 text-green-700 border border-green-400')
        return redirect('home:view_profile')

    # Redirect to profile or other appropriate page if not POST
    return redirect('home:view_profile')