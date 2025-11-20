from django.urls import path
from . import views
from .views import email_list,email_list_template,sync_gmail

urlpatterns = [
    path('api/', views.email_list, name='email_api'),
    path('', views.email_list_template, name='email_list_template'),
    path("sync-gmail/", sync_gmail),

]
