from uuid import uuid4

from django.db.models import F
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, redirect

from api.models import Redirect
#from pp.urls import refresh_redirects


class ShortenerView(View):
    def get(self, request):
        template = 'index.html'
        urls = Redirect.objects.all().order_by('clicks').reverse()
        return render(request, template,
                      context={'redirects': urls,
                               'host': request.get_host(),
                               'protocol': request.scheme})

    def post(self, request):
        long_url = request.POST.get('long_url')
        if not long_url:
            return self.get(request)

        try:
            redir_obj = Redirect.objects.create(url=long_url)
        except Exception as e:
            return JsonResponse({'error': str(e)})
        #refresh_redirects()
        if redir_obj:
            return self.get(request)
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
        return redirect(f'{redir_obj.url}')
