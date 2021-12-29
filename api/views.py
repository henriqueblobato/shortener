from django.views import View
from django.shortcuts import render


class ShortenerView(View):
    def get(self, request):
        # --> 1. get url from requests
        # --> 2. put url on database
        # --> 3. populate the Redirect object
        pass

class RedirectView(View):
    def get(self, request):
        # --> 1. get url from database
        # --> 2. redirect to the url
        pass