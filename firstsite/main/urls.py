from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"), # 網址後完全不打路徑所看見的view
    path("", views.home, name="home"), # setup home page
    path("create/", views.create, name="create"), # add the create views in path
]