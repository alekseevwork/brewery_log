from django.db import models
from django.urls import reverse


class Tank(models.Model):
    """номера цкт"""
    number = models.IntegerField(db_index=True)
    title = models.ForeignKey('Beer', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.number} - {self.title}'

    def get_absolute_url(self):
        # return reverse('tanks', kwargs={"tank_id": self.pk})
        return 'home/'


class Beer(models.Model):
    """сорт пива"""
    title = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.title


class Measuring(models.Model):
    """необходимые измерения"""
    # title = models.ForeignKey(Beer, on_delete=models.PROTECT)
    temperature = models.FloatField(verbose_name='Температура')
    density = models.FloatField(verbose_name='Плотность')
    data_meas = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500, blank=True)
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE, verbose_name='Номер')
    pressure = models.FloatField(default=0, blank=True, verbose_name='Давление')
    # def __str__(self):
    #     return f'{self.pk}'

    def get_absolute_url(self):
        # return reverse('tanks', kwargs={"tank_id": self.tank.pk})
        return 'add-measuring/'
