from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.shortcuts import render
from .models import Account
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from trycourier import Courier
from .tasks import register_email

client = Courier(auth_token="pk_prod_TG1GS5TYWYMN47QGJZGXG1YBXQJM")


@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            url = request.META.get('HTTP_REFERER')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid login credentials')
            return redirect('login')
    
    return render(request, 'accounts/login.html')

@csrf_exempt
def signup(request):
    if request.method=='POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email']
        password = request.POST['password']
        username = email.split('@')[0]
        user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user.is_active = True
        user.save()
        register_email.delay(email) # task will be triggered through source code
        return redirect('login')
        
    return render(request, 'accounts/sign_up.html')


@csrf_exempt
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out')
    return redirect('login')


@csrf_exempt
@login_required(login_url='login')
def newsletter(request):
    if request.method == "POST":
        try:
            user = Account.objects.get(email=request.user.email)
            user.newsletter = True
            user.save()
            resp = client.send_message(
            message={
                "to": {
                "email": user.email,
                },
                "template": "FX7HJ0EJ0B4GJTMG2SVPRGST9ZZ8",
                "data": {
                "recipientName": "recipientName",
                "mail_subject": "mail_subject",
                "message": "message",
                },
            }
            )
            print(resp['requestId'])
            return redirect('report_crime')
        except:
            pass

    return redirect('report_crime')




