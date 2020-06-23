from django.urls import  path
from .views import current_datetime,test_view

urlpatterns = [
    path('',current_datetime,name='current_datetime'),
    path('users/',test_view,name='test'),
]
