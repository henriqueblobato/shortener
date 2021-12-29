from django.db import models


class Redirect(models.Model):
    url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=255)
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    clicks = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # contains the raw URL
    # contains the redirect url
    # user
    # how many times the user has clicked on the link (int)
    # date(default=now, default=auto_now)
    pass

    def __str__(self):
        return f'{self.url}'

    def __dict__(self):
        return {
            'url': self.url,
            'short_url': self.short_url,
            'clicks': self.clicks,
            'created_at': self.created_at
        }

    class Meta:
        db_table = 'redirects'
        verbose_name = 'Redirect'
        verbose_name_plural = 'Redirects'
