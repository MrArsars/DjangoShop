from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    #path('', LoginView.as_view()),
    path("", include("allauth.account.urls"))
]
