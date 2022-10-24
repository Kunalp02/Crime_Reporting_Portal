import random
from celery import shared_task
from django.core.mail import send_mail
from dashboard import settings
from .models import Account
from django.db.models import Q
from trycourier import Courier
from newscatcherapi import NewsCatcherApiClient
from decouple import config
import datetime


# Email Automation by using Celery
@shared_task(bind=True)
def email(self):
    client = Courier(auth_token=config("AUTH_TOEKN", default='pk_prod_TG1GS5TYWYMN47QGJZGXG1YBXQJM'))
    users_subscribed_newsletter = Account.objects.filter(newsletter=True)

    newscatcherapi = NewsCatcherApiClient(x_api_key=config("API_KEY"))
    all_articles = newscatcherapi.get_search(q="latest")
    articles = all_articles.get('articles')[:5]
    current_day = str(datetime.datetime.now())
    print(current_day)

    for user in users_subscribed_newsletter:
        resp = client.send_message(
            message={
                'to': {
                    'email': user.email,
                },
                "template": "4GJV7Z51SV42DWKF8K36D8G40KQH",
                "data": {
                        "current_date" : current_day,
                        "articles" : {
                            "Post_1" : f"{articles[0]['title']}",
                            "Post_1_Media" : f"{articles[0]['media']}",
                            "Post_1_Link" : f"{articles[0]['link']}",
                            "Post_2" : f"{articles[1]['title']}",
                            "Post_2_Media" : f"{articles[1]['media']}",
                            "Post_2_Link" : f"{articles[1]['link']}",
                            "Post_3" : f"{articles[2]['title']}",
                            "Post_3_Media" : f"{articles[2]['media']}",
                            "Post_3_Link" : f"{articles[2]['link']}",
                            "Post_4" : f"{articles[3]['title']}",
                            "Post_4_Media" : f"{articles[3]['media']}",
                            "Post_4_Link" : f"{articles[3]['link']}",
                            "Post_5" : f"{articles[4]['title']}",
                            "Post_5_Media" : f"{articles[4]['media']}",
                            "Post_5_Link" : f"{articles[4]['link']}",
                        }
                    },
                }
            )
        print(resp['requestId'])
    return "Done"




