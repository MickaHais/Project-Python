from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.accueil, name="accueil"),
    path('detail/<int:train_id>/', views.detail, name="detail"),
    path('random/', views.getrandom, name="random")
]
