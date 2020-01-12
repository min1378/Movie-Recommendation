
from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.signup),
    path('check_password/<int:user_id>/', views.check_password),
    path('withdraw/<int:user_id>/', views.withdraw),
    path('userprofile/<int:user_id>/', views.userprofile),
    path('change/<int:user_id>/', views.change),
]
