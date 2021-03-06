from django.urls import path
from .views import (
    UserView, UserLoginView, AdminView,
    AdvisorsView, BookingCreateView,
    AdvisorsBookingView
)

urlpatterns = [
    path('user/register/', UserView.as_view()),
    path('user/login/', UserLoginView.as_view()),
    path('admin/advisor/', AdminView.as_view()),
    path('user/<uuid:user_id>/advisor/', AdvisorsView.as_view()),
    path('user/<uuid:user_id>/advisor/booking/', AdvisorsBookingView.as_view()),
    path('user/<uuid:user_id>/advisor/<uuid:advisor_id>/', BookingCreateView.as_view()),
]