from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Report, Anonymous_report, Account
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from trycourier import Courier
from newscatcherapi import NewsCatcherApiClient
from pprint import pprint
from decouple import config


client = Courier(auth_token=config("AUTH_TOEKN", default='pk_prod_TG1GS5TYWYMN47QGJZGXG1YBXQJM'))


@csrf_exempt
def dashboard(request):
    try:
        newscatcherapi = NewsCatcherApiClient(x_api_key=config("API_KEY"))

        all_articles = newscatcherapi.get_search(q="latest")
        # pprint(all_articles.get('articles')[:5])
        context = {
            'all_articles' : all_articles.get('articles')[:9],
        }
        return render(request, 'dashboard.html', context)
    except: 
        pass
    
    return render(request, 'dashboard.html')


   


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
    else:
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
            newscatcherapi = NewsCatcherApiClient(x_api_key=config("API_KEY"))
            all_articles = newscatcherapi.get_search(q=keyword)

        context = {
            'all_articles' : all_articles.get('articles')[:9],
        }

    return render(request, 'dashboard.html', context)
