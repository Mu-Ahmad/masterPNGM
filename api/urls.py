from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path('other/', views.other, name="other"),
]
