from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .forms import ProfileForm, UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('base'))
    else:
        form = UserLoginForm()
        error = True
    return render(request, 'users/login.html',
                  {'form': form})

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(
                request, f'{user.username}, Вы зарегистрированы'
            )
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration.html',
                  {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user,
                           files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль был изменен')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'users/profile.html',
                  {'form': form})

def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('user:login'))
