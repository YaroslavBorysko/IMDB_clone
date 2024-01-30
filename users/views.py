from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from users.forms import UserRegisterForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/login.html', {'form': form})


def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account updated for {email}!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('movies_list')

