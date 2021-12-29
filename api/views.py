from django.views import View
from django.shortcuts import render, redirect

from api.models import Redirect


class ShortenerView(View):
    def get(self, request):
        # --> 1. get url from requests
        # --> 2. put url on database
        # --> 3. populate the Redirect object
        pass

class RedirectView(View):
    def get(self, request):
        short_url = request.path.replace('/', '')
        redir_obj = Redirect.objects.filter(short_url=short_url).first()
        return redirect(redir_obj.url)
