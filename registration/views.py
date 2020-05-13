from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from registration.forms import CustomUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def create_user(request):
    global context
    form = CustomUserForm()

    if request.method == 'POST':
        form = CustomUserForm(data=request.POST)
    # Check double e-mail in DB
    email = request.POST.get('email')
    if not User.objects.filter(email=email).first():
        if form.is_valid():
            form.save()
            return redirect(reverse('main:main'))
        return render(request, 'registration.html', {'form': form})
    else:
        error_messages = "Email используется"
        context = {'error_messages': error_messages}
        return render(request, 'registration.html', {'form': form,'error_messages':error_messages})


def login_view(request):
    """Логин"""

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        success_url = reverse('main:main')

        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return redirect(success_url)

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('registration:login'))
