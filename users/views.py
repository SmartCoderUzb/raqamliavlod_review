from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from django.views.decorators.csrf import csrf_exempt

from .forms import UserCreationForm, UserModelForm, CustomAuthenticationForm

@csrf_exempt
@login_required(login_url="login")
def signup_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    print(form.errors, 21)
    return render(request, 'signup_errors.html', {'form': form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login_errors.html', {'form': form,"form_errors":form.errors.get("__all__")})

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('home') 
 
@login_required(login_url="login")
def profile(request):
    if request.method == "POST":
        form = UserModelForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserModelForm(instance=request.user)
    return render(request, "profile_errors.html", {"form":form})
