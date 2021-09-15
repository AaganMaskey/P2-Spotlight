from django.contrib import auth
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models  import User, UserManager
from django.core.validators import validate_email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage, message
from django.conf import UserSettingsHolder, settings    
import threading
from decimal import Context
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class EmailThread(threading.Thread):
    def __init__(self, email_message):
        self.email_message = email_message

    def run(self):
        self.email_message.send()


class RegistrationView(View):
    def get(self, request):

        return render(request, 'auth/register.html')

    def post(self, request):
        context = {
            'data' : request.POST,
            'has_error' : False
        }

        threading.Thread.__init__(self)
        email = request.POST.get('email')
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Minimum password length check
        if len(password)<6:
            messages.add_message(request, messages.ERROR, 
                'Password should be greater than 6 characters')
            context['has_error']=True

        # Password and confirm password check
        if password != password2:
            messages.add_message(request, messages.ERROR, 
                'Passwords do not match, check again')
            context['has_error'] = True

        # Email format validation
        if validate_email == False: 
            messages.add_message(request, messages.ERROR, 
                'Please provide a valid email address')
            print(context)
            context['has_error']=True
        
        # Email already exists check
        try:
            if User.objects.filter(email = email):
                messages.add_message(request, messages.ERROR, 
                    'Email is already taken')
                context['has_error']=True
        except Exception as identifier:
            pass

        # Username already taken check
        try:
            if User.objects.filter(username = username):
                messages.ActivateAccountViews.add_message(request, messages.ERROR, 
                'The desired username is already taken')    
                context['has_error']=True
        except Exception as identifier:
            pass

        if context['has_error']:
            return render(request, 'auth/register.html', context, status=400)

        user = User.objects.create_user(username=username, email=email)
    
        user.set_password(password) 
        user.first_name= name
        user.is_active = False
        user.save() 

        current_site = get_current_site(request)
        email_subject = "Activate your Spotlight account"
        message = render_to_string('auth/activate.html', 
            {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            }
            )

        email_message = EmailMessage(
        email_subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        ['spotlight.excelerators+BCC_activateAccount@gmail.com']
        )
        EmailThread(email_message).start()
        messages.add_message(request, messages.SUCCESS,
                             'Account created succesfully. Please check your email to activate your account')

        return redirect('login')
        
class LoginView(View):
    # GET request
    def get(self, request):
        return render(request, 'auth/login.html')
    # POST Request
    def post(self, request):
        context = {
            'data':request.POST,
            'has_error': False
        }
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '':
            messages.add_message(request, messages.ERROR, 'Username is required')
            context['has_error']=True
            
        if password == '':
            messages.add_message(request, messages.ERROR, 'Password is required')
            context['has_error']=True
        user = authenticate(request, username=username, password=password)

        if not user and not context['has_error']:
            messages.add_message(request, messages.ERROR, 'Invalid login')
            context['has_error']=True

        if context['has_error']:
            return render(request, 'auth/login.html', status=401, context=context)
        login(request, user)
        return redirect('home')
        return render(request, 'auth/login.html')

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.SUCCESS, 
                'Account activated successfully. You can now login with your credentials')
            return redirect ('login')
        return render(request, 'auth/activate_failed.html', status=401)

class HomeView(View):
    def get (self,request):
        return render(request, 'home.html')


class ProjectView(View):
    def get (self,request):
        return render(request, 'project.html')

class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.add_message(request,messages.SUCCESS, 'Logged out successfully')
        return redirect ('login')

class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.add_message(request,messages.SUCCESS, 'Logged out successfully')
        return redirect ('login')

class RequestResetEmailView(View):
    def get(self, request):
        return render (request, 'auth/request-reset-email.html')

    def post(self, request):
        email = request.POST['email']

        if validate_email == False: 
            messages.error(request, 'Please enter a valid email')
            return render(request, 'auth/request-reset-email.html')

        user =  User.objects.filter(email=email)

        if user.exists():
            current_site = get_current_site(request)
            email_subject = 'Reset your password for Spotlight'
            message = render_to_string('auth/reset-user-password.html', 
                {
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user[0].pk)),
                'token': PasswordResetTokenGenerator().make_token(user[0])
                }
                )

            email_message = EmailMessage(
            email_subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            ['spotlight.excelerators+BCC_resetPassword@gmail.com']
            )
            EmailThread(email_message).start()

        messages.success(
            request, 'Password reset email sent')
        return render(request, 'auth/request-reset-email.html')

class SetNewPasswordView(View):
    def get(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token
        }

        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))

            user = User.objects.get(pk=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.info(
                    request, 'Password reset link, is invalid, please request a new one')
                return render(request, 'auth/request-reset-email.html')

        except DjangoUnicodeDecodeError as identifier:
            messages.success(
                request, 'Invalid link')
            return render(request, 'auth/request-reset-email.html')

        return render(request, 'auth/set-new-password.html', context)

    def post(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token,
            'has_error': False
        }

        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'passwords should be at least 6 characters long')
            context['has_error'] = True
        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'passwords don`t match')
            context['has_error'] = True

        if context['has_error'] == True:
            return render(request, 'auth/set-new-password.html', context)

        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))

            user = User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()

            messages.success(
                request, 'Password reset success, you can login with new password')

            return redirect('login')

        except DjangoUnicodeDecodeError as identifier:
            messages.error(request, 'Something went wrong')
            return render(request, 'auth/set-new-password.html', context)

        return render(request, 'auth/set-new-password.html', context)