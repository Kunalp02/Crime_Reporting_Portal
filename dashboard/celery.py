# path/to/your/proj/src/cfehome/celery.py
import os
from celery import Celery
from decouple import config
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')

app = Celery('dashboard')
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object('django.conf:settings', namespace='CELERY')

# everyday on 7 am Top 5 news will be sent to the users 

app.conf.beat_schedule = {
     'trigger_new': {
        'task': 'accounts.tasks.email',
        'schedule': crontab(hour=7, minute=00),
    },
}



app.autodiscover_tasks()
