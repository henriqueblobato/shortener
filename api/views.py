from uuid import uuid4

from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect

from api.models import Redirect


class ShortenerView(View):
    def get(self, request):
        template = 'index.html'
        urls = Redirect.objects.all().order_by('clicks')
        redirects = {
            i.short_url: i.clicks
            for i in urls
        }
        return render(request, template, context={'redirects': redirects})

    def post(self, request):
        long_url = request.POST.get('long_url')
        redir_obj = Redirect.objects.create(
            long_url=long_url,
            short_url=str(uuid4()).split('-')[0],
        )
        if redir_obj:
            return JsonResponse(redir_obj.short_url)
        else:
            return JsonResponse('Something went wrong')


class RedirectView(View):
    def get(self, request):
        short_url = request.path.replace('/', '')
        redir_obj = Redirect.objects.filter(short_url=short_url).first()
        if redir_obj:
            Redirect.objects.filter(short_url=short_url).update(clicks=F('clicks') + 1)
        else:
            return JsonResponse('Something went wrong')
        return redirect(redir_obj.url)
