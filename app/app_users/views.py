from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from app_users.forms import RegistrationForm, LoginForm


def register_view(request):
    """ Registration view """

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            group = Group.objects.get(name='registered')
            group.user_set.add(user)
            user.is_staff = True
            user.save()
            user = authenticate(username=username, password=raw_password, is_staff=True)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'app_users/registration.html', {'form': form})


def login_view(request):
    """ Login view """

    if request.method == 'POST':
        auth_form = LoginForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            if not user:
                auth_form.add_error('__all__', 'Not registered')
            return redirect('main')
    else:
        auth_form = LoginForm
    context = {
        'form': auth_form
    }
    return render(request, 'app_users/login.html', context=context)


def logout_view(request):
    """ Logout view """

    logout(request)
    return redirect('main')