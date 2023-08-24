from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzeria.settings')

app = Celery('pizzeria')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()




app.conf.beat_schedule = {
    'change-order-status': {
        'task': 'orders.tasks.change_order_status',
        'schedule': crontab(minute='*'),  
    },
}
