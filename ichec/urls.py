from django.urls import path
from ichec import views
from .settings import APP_NAME

app_name = APP_NAME
urlpatterns = [
    path("", views.home, name="home"),
    path("masters/", views.masters, name="masters"),
    path("master-detail/<int:pk>", views.master_detail, name="master_detail"),
]