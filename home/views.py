from django.shortcuts import render
from .forms import *
from accounts.forms import SignUpForm, LoginForm

# Create your views here.
def home(request, toast_message={}, banner_title={} ,banner_message={} ):
    signup_form = SignUpForm()
    login_form = LoginForm()
    contact_form = ContactUsForm()
    if request.method == 'POST':
        print(request.POST)
        if 'subject' and 'message' in request.POST:
            contact_form = ContactUsForm(request.POST)
            if contact_form.is_valid():
                name = contact_form.cleaned_data['name']
                email = contact_form.cleaned_data['email']
                subject = contact_form.cleaned_data['subject']
                message = contact_form.cleaned_data['message']
                print('Message is recieved by function in home.views.py')
                # Try send contact message
                banner_title = f"Thanks for the message!"
                banner_message = 'You will be hearing from me soon'
                
                context = {
                    'banner_title': banner_title,
                    'banner_message': banner_message,                    
                    'contact_form': contact_form,
                    'signup_form': signup_form,
                    'login_form': login_form,
                    'toast_message': f'Thanks {name}'
                }
                return render(request, 'landing_page.html', context)
            else:

                print('message failed')
                context = {
                    'contact_form': contact_form,
                    'toast_message': contact_form.errors,
                    'signup_form': signup_form,
                    'login_form': login_form,
                }
                return render(request, 'landing_page.html', context)
    else:

        banner_title = "Banner title"
        banner_message = 'Making a great boilerplate for future use.'
        context = {
            'toast_message': toast_message,
            'banner_title': banner_title,
            'banner_message': banner_message,
            'contact_form': contact_form,
            'signup_form': signup_form,
            'login_form': login_form,
            
        }

        return render(request, 'landing_page.html', context)