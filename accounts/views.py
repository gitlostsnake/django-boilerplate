from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .decorators import unauthenticated_user

# Create your views here.
from .forms import *
from home.forms import ContactUsForm
from home.views import home
from .services import signup_new_user


def signup(request):
    contact_form = ContactUsForm()
    signup_form = SignUpForm()
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            # Signup Function in services
            
            signup_new_user(request, signup_form)

            toast_message = "Welcome! Lets start a discussion."
            banner_title = f"Thanks {signup_form.cleaned_data['username']}"
            banner_message = f"Your signed up!"
            context = {
                'toast_message': toast_message,
                'banner_title': banner_title,
                'banner_message': banner_message,
                'contact_form': contact_form,
            }
            return render(request, 'signup_initiated.html', context)
        else:
            toast_message = "Check your details and try again."
            context = {
                'toast_message': toast_message,
                'signup_form': signup_form,
                'contact_form': contact_form,
            }
            return render(request, 'signup.html', context)
    else:
        toast_message = "Input details to sign up."
        context = {
            'toast_message': toast_message,
            'signup_form': signup_form,
            'contact_form': contact_form,
        }
        return render(request, 'signup.html', context)        
        


def login(request):
    contact_form = ContactUsForm()
    signup_form = SignUpForm()
    login_form = LoginForm()
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            
            return redirect('home')
            # return render(request, 'landing_page.html', {'toast_message' : "Logged in successfully"})
        else:
            toast_message = "Username or password was incorrect"

            context = {
                'toast_message' : toast_message,
                'contact_form': contact_form,
                'signup_form': signup_form,
                'login_form': login_form,
            }
            return render(request, 'login.html', context)
    else:
        toast_message = "Login Forms :D"
        context = {
            'toast_message' : toast_message,
            'contact_form': contact_form,
            'signup_form': signup_form,
            'login_form': login_form,
            }
        return render(request, 'login.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')


def contact_us(request):
    # Services Contact us function to save the message
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            print('Message is recieved by function in accounts.views.py')        
    return home(request)

def activate_account(request):
    pass