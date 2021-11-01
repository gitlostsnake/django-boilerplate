from django.contrib.auth.models import User
from django.conf import settings
from .models import *
from django.contrib import auth
from .tokens import account_activation_token
# sendinblue imports
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
import requests




def signup_new_user(request, signup_form):
    # You will have to add in settings.EMAIL_API_KEY and remove the if statement in production.
    # Only works with SENDINBLUE API KEY

    EMAIL_SETUP = False
    if EMAIL_SETUP:
        user = signup_form.save(commit=False)
        user.is_active = False
        user.save()
        update_profile(user.id, False)
        authenticate_new_user(request)


    else:
        # This is what is being used currently without email authentication/.
        user = signup_form.save()
        user.is_active = True
        update_profile(user.id, False)
        auth.login(request, user)




def update_profile(user_id, email_authenticated):
    user = User.objects.get(pk=user_id)
    user.profile.email_confirmed = email_authenticated
    # Here you can add in custom Profile information. Which will be called 
    # when signing up and/or just whever new information is recieved.

    

def authenticate_new_user(request, user_id, template_id):
    """ Pass in the request, user and the send in blue template ID into this function to authenticate the user. """
    # If you are using SendinBlue and have EMAIL_API_KEY in your settings file this function will be triggered on signup.

    user = User.objects.get(pk=user_id)

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.EMAIL_API_KEY    

    current_site = get_current_site(request)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)    

    api_instance = sib_api_v3_sdk.SMTPApi(sib_api_v3_sdk.ApiClient(configuration))
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": f"{email}", "username": f"{user}"}], template_id=2,
        params={"domain": f"{current_site.domain}", "uid": f"{uid}", "token": f"{token}"},
        headers={
            "X-Mailin-custom": "custom_header_1:custom_value_1", "charset": "iso-8859-1"})
        
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


def activate_new_user(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        email = user.email
        # Add user email to the right industry email list

        url = "https://api.sendinblue.com/v3/contacts"


        # List ids will add the user to a mailing list.
        # You can add in addition info on the user profile that links up with this id. 
        # Example:  Profile Model
        # UPBEAT = 1              CHILLED = 2
        # CHOICES = ((UPBEAT, 'Upbeat'), (CHILLED, 'Chilled'))
        # personality_type = PositiveIntergerField (choices=CHOICES) 
        # Then have the Interger the same as the SendInBlue ListId.
        # payload = f'{{"email":"{email}", "listIds": [{<INSERT PROFILE DATA HERE>}, {<INSERT PROFILE DATA HERE>}], "updateEnabled":true}}'

        # f string version
        payload = f'{{"email":"{email}", "listIds": [{1}, {2}], "updateEnabled":true}}'
        # .format version
        # payload = r'{{"email":"{}","listIds":[{},{}],"updateEnabled":true}}'.format(email, industry, role)
        headers = {
            'accept': "application/json",
            'content-type': "application/json",
            'api-key': f"{settings.EMAIL_API_KEY}"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
        auth.login(request, user)


def send_email(template_id, user_email, message, sender):
    # Called example // send_email(15, crew_man.user.email, message, request.user)
    # Used for sending custom emails either user generated or relaying information to the user from the system.
    # Get user by email. Or could take the user in as params for this function.
    
    user = find_user_on_email(user_email)
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.EMAIL_API_KEY

    api_instance = sib_api_v3_sdk.SMTPApi(sib_api_v3_sdk.ApiClient(configuration))
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{'email': f'{user_email}', 'name': f'{user.username}'}], template_id=template_num,
        params={'sender': f"{sender}", 'message': f"{message}"},
        headers={
            "X-Mailin-custom": "custom_header_1:custom_value_1", "charset": "iso-8859-1"})

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        # Exception when calling this function. Log activity and return info to the user. 
        print('Exception when calling SMTPApi->send_transac_email: %s\n' % e)

