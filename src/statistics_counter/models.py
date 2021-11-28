from django.db import models


class ActivityCollection(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_at = models.DateField(auto_now_add=True, verbose_name='date_at')
    views = models.PositiveIntegerField(verbose_name='views')
    clicks = models.PositiveIntegerField(verbose_name='clicks')
    cost = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='cost')
    cpc = models.FloatField(verbose_name='cpc', blank=True, null=True)
    cpm = models.FloatField(verbose_name='cpm', blank=True, null=True)

    def __str__(self):
        return str(self.date_at)

    def save(self, *args, **kwargs):
        self.cpc = self.cost/self.clicks
        self.cpm = self.cost/self.views * 1000
        super(ActivityCollection, self).save(*args, **kwargs)
