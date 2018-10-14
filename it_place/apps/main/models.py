from django.db import models


class Reit(models.Model):
    reit = models.CharField('Рейтинг',max_length=5)


def __str__(self):
        return self.reit


# class Meta:
#     verbose_name = 'reit'
#
#     verbose_name_plural = 'reit'