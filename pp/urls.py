"""pp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.views import ShortenerView, RedirectView

from api.models import Redirect


def get_all_redirects():
    r = Redirect.objects.all()
    return [
        path(f"{i.get('short_url')}/", RedirectView.as_view())
        for i in r.values()
    ]


redirects_list = get_all_redirects()
print(redirects_list)

urlpatterns = [
    path('', ShortenerView.as_view()),
    path('admin/', admin.site.urls),
    path('short/', ShortenerView.as_view()),
] + redirects_list


# --> google.com --> /a
# /a --> google.com
