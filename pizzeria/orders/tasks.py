from celery import shared_task
from datetime import datetime, timedelta
from orders.models import Order

@shared_task
def change_order_status():
    now = datetime.now()
    orders_to_change = Order.objects.exclude(status='Delivered')
    
    for order in orders_to_change:
        order.ordered_time = order.ordered_time.replace(tzinfo=None)
        if now - order.ordered_time > timedelta(minutes=1):
            order.status = 'Preparing'
        if now - order.ordered_time > timedelta(minutes=3):
            order.status = 'Dispatched'
        if now - order.ordered_time > timedelta(minutes=5):
            order.status = 'Delivered'
        order.save()
