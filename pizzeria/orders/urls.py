from django.urls import path
from .views import OrderCreateView, OrderTrackView

urlpatterns = [
    path('create_order/', OrderCreateView.as_view(), name='create_order'),
    path('track_order/<int:order_id>/',OrderTrackView.as_view(), name='track_order')
]