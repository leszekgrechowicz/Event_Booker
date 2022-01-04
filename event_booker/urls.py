from django.urls import path
from . import views

app_name = 'event_booker'

urlpatterns = [
    path('', views.ShowEventsView.as_view(), name='main-show-events'),
    path('book/<int:id>/', views.BookEventView.as_view(), name='book-event'),
    path('booking-confirmation/<uuid:uuid_>/', views.ConfirmBooking.as_view(), name='confirm-booking')
]
