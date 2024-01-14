from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, LoginForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        print(form.is_valid())
        print(request.POST)
        if form.is_valid():
            form.save()
            print("from save")
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    return render(request=request,
                  template_name='users/register.html',
                  context={"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print(email, password)
            user = authenticate(request,
                                email=email,
                                password=password)
            print(user)
            if user is not None:
                login(request=request, user=user)
                return redirect(to='shop:add_product')
    else:
        form = LoginForm()
    return render(request=request,
                  template_name="users/login.html",
                  context={"form": form})
