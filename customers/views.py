from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Customer


# Create your views here.

def sign_out(request):
    logout(request)
    return redirect('home')


def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        # create user
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )

        # create customer
        customer = Customer.objects.create(
            name=username,
            user=user,
            address=address,
        )
        Success_message = 'User registered Successfully goto login page'
        messages.success(request, Success_message)

    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid user credentials')
        return redirect('home')
    return render(request, 'account.html', context)
