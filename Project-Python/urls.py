from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('train/', include("train.urls")),
    path('admin/', admin.site.urls),
]
