from django.urls import path
from .views import report_view

urlpatterns = [
    path('<str:production_line>/',report_view,name='report_view'),
]
