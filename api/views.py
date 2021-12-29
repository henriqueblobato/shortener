from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect

from api.models import Redirect


class ShortenerView(View):
    def get(self, request):
        # --> 1. get url from requests
        # --> 2. put url on database
        # --> 3. populate the Redirect object
        pass

    def post(self, request):
        long_url = request.POST.get('long_url')
        redir_obj = Redirect.objects.create(
            long_url=long_url
        )
        if redir_obj:
            return JsonResponse(redir_obj.short_url)
        else:
            return JsonResponse('Something went wrong')


class RedirectView(View):
    def get(self, request):
        short_url = request.path.replace('/', '')
        redir_obj = Redirect.objects.filter(short_url=short_url).first()
        return redirect(redir_obj.url)
