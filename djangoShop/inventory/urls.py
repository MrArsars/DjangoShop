from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from inventory.views import *

urlpatterns = [
    path('', inventory),
]
urlpatterns += staticfiles_urlpatterns()
