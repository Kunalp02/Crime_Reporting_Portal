from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Report, Anonymous_report, Account
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from trycourier import Courier
from newscatcherapi import NewsCatcherApiClient
from pprint import pprint


client = Courier(auth_token="pk_prod_TG1GS5TYWYMN47QGJZGXG1YBXQJM")


@csrf_exempt
def dashboard(request):

    newscatcherapi = NewsCatcherApiClient(x_api_key='SzG3tdKC9lx6o5cefl5auNswud-xs0XUGZcL4pMpYyw')

    all_articles = newscatcherapi.get_search(q="latest")
    pprint(all_articles.get('articles')[:5])

    context = {
        'all_articles' : all_articles.get('articles')[:9],
    }

    return render(request, 'dashboard.html', context)


@csrf_exempt
@login_required(login_url='login')
def report_crime(request):
    if request.method == 'POST':
        state = request.POST['state']
        country = request.POST['country']
        crime = request.POST['crime']
        crime_description = request.POST.get('crime_description')
        proof = request.FILES['proof']
        user = request.user
        report = Report.objects.create(user=user, country=country, state=state, crime=crime, description=crime_description, proof=proof)
        report.save()
        return render(request, 'successfully_reported.html')
    try:
        user = Account.objects.get(email=request.user.email)
        user.newsletter = True
        user.save()        
        context = {
            'status' : user.newsletter
        }    
        return render(request, 'report.html', context)
    except:
        pass

    resp = client.send_message(
        message={
            "to": {
            "email": "kunalpatil970730@gmail.com",
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
 
    return render(request, 'report.html')


@csrf_exempt
def report_anonymously(request):
    if request.method == 'POST':
        state = request.POST['state']
        country = request.POST['country']
        crime = request.POST['crime']
        crime_description = request.POST.get('crime_description')
        proof = request.FILES['proof']
        report = Anonymous_report.objects.create(country=country, state=state, crime=crime, description=crime_description, proof=proof)
        report.save()


    return render(request, 'report_anonymously.html')

@csrf_exempt
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            newscatcherapi = NewsCatcherApiClient(x_api_key='SzG3tdKC9lx6o5cefl5auNswud-xs0XUGZcL4pMpYyw')
            all_articles = newscatcherapi.get_search(q=keyword)

        context = {
            'all_articles' : all_articles.get('articles')[:9],
        }

    return render(request, 'dashboard.html', context)
