import string
from django.utils.crypto import get_random_string

from django.db import models


class Redirect(models.Model):
    short_url = models.CharField(max_length=5000,
                                 unique=True,
                                 db_index=True,
                                 primary_key=True,
                                 editable=False,
                                 default=get_random_string(
                                     length=5,
                                     allowed_chars=string.ascii_letters + string.digits))
    url = models.CharField(max_length=5000)
    clicks = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.url

    def generate_short_url(self):
        return get_random_string(length=5, allowed_chars=string.ascii_letters + string.digits)

    class Meta:
        db_table = 'redirects'
        verbose_name = 'Redirect'
        verbose_name_plural = 'Redirects'
