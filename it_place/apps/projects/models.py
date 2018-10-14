from django.db import models
from stdimage.models import StdImageField
from stdimage.validators import MaxSizeValidator
from stdimage.utils import pre_delete_delete_callback, pre_save_delete_callback
from django.db.models.signals import post_delete, pre_save
from settings import default_avatars
from django.utils.translation import ugettext_lazy as _
from utils.choices import CITIES, PROJECT_TYPE
from apps.users.models import Specialty
from apps.users.models import ItUser


def avatar_path(instance, filename):
    return 'avatars/{0}/{1}/{2}/{3}/{4}'.format(instance.city, instance.type,
                                                instance.title[:1], instance.title[:2], instance.title)


class Event(models.Model):
    title = models.CharField(_('Название'), max_length=100)
    # slug = AutoSlugField(populate_from='title', unique_with='date_start__month')
    type = models.CharField(_('Вид проекта'), max_length=100, choices=PROJECT_TYPE, default='hak')
    img = StdImageField(
        _("Аватар"),
        upload_to=avatar_path,
        variations={'thumb': (150, 150, True), 'small': (50, 50, True)},
        validators=[MaxSizeValidator(1028, 768)],
        null=True
    )
    city = models.CharField(_('Город'), max_length=100, choices=CITIES, default='msk')
    specialty = models.ManyToManyField(Specialty, verbose_name=_('Проекту нужны'), related_name='proj_specs')
    about = models.TextField(_('Описание'), max_length=2000)
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    vk = models.CharField(max_length=100, blank=True)
    create_by = models.ForeignKey(ItUser, verbose_name=_('Создатель'), related_name='my_projects')
    members = models.ManyToManyField(ItUser, verbose_name=_('Участники'), blank=True, related_name='projects')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'

    def get_small_img_url(self):
        try:
            return self.img.small.url
        except AttributeError:
            return default_avatars.DEFAULT_EVENT_AVATAR_SMALL

    def get_thumb_img_url(self):
        try:
            return self.img.thumb.url
        except AttributeError:
            return default_avatars.DEFAULT_EVENT_AVATAR_THUMB


post_delete.connect(pre_delete_delete_callback, sender=Event)
pre_save.connect(pre_save_delete_callback, sender=Event)
