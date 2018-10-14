from django.db import models
from django.contrib.auth.models import AbstractUser
from stdimage.models import StdImageField
from stdimage.validators import MaxSizeValidator
from stdimage.utils import pre_delete_delete_callback, pre_save_delete_callback
from django.db.models.signals import post_delete, pre_save
from settings import default_avatars
from django.utils.translation import ugettext_lazy as _
from utils.choices import CITIES, SPECIALITIES
from datetime import datetime, date
from django.utils import timezone


def avatar_path(instance, filename):
    return 'avatars/{0}/{1}/{2}/{3}'.format(instance.city, instance.specialty, instance.username[:1],
                                            instance.username[:2], instance.username)


class Specialty(models.Model):
    title = models.CharField(_('Специальность'), max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Specialty'
        verbose_name_plural = 'Specialties'


class ItUser(AbstractUser):

    # signed = models.ForeignKey('ItUser', null=True, blank=True)
    # colleagues = models.ForeignKey('ItUser', null=True, blank=True)
    # number = models.PositiveIntegerField(max_length=5)
    username = models.CharField(
        _('Логин'),
        max_length=150,
        unique=True,
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('Имя'), max_length=30)
    last_name = models.CharField(_('Фамилия'), max_length=30)
    specialty = models.CharField(_('Специальность'), choices=SPECIALITIES, max_length=100)
    birth = models.DateField(_('Дата рождения'), default=timezone.now)
    email = models.EmailField(_('Email'), unique=True)
    img = StdImageField(
        _("Аватар"),
        upload_to=avatar_path,
        variations={'thumb': (150, 150, True), 'small': (50, 50, True)},
        validators=[MaxSizeValidator(1028, 768)],
        null=True
    )
    city = models.CharField(_('Город'), max_length=100, choices=CITIES, default='msk')
    experience = models.CharField(_('Опыт работы'), max_length=100)
    education = models.CharField(_('Образование'), max_length=100)
    about = models.TextField(_('О себе'), max_length=2000)
    skills = models.CharField(
        _('Навыки'),
        max_length=1000,
        help_text=_('Например: Python, Photoshop, CSS, Angular - разделять навыки запятыми')
    )
    edu = models.BooleanField(_('Готов обучать'), default=False)
    edu_list = models.CharField(
        _('Могу обучить'),
        max_length=1000,
        help_text=_('Например: Python, Photoshop, CSS, Angular'),
        null=True,
        blank=True
    )
    github = models.CharField(max_length=100, blank=True)
    bitbacket = models.CharField("bitbucket", max_length=100, blank=True)
    pinterest = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    vk = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'ItUser'
        verbose_name_plural = 'ItUsers'

    def get_small_img_url(self):
        try:
            return self.img.small.url
        except AttributeError:
            return default_avatars.DEFAULT_USER_AVATAR_SMALL

    def get_thumb_img_url(self):
        try:
            return self.img.thumb.url
        except AttributeError:
            return default_avatars.DEFAULT_USER_AVATAR_THUMB

    def get_age(self):
        today = date.today()
        years_difference = today.year - self.birth.year
        is_before_birthday = (today.month, today.day) < (self.birth.month, self.birth.day)
        elapsed_years = years_difference - int(is_before_birthday)
        return elapsed_years

    def get_skiils(self):
        str = self.skill.split(',')
        print(str)
        return list(str)

post_delete.connect(pre_delete_delete_callback, sender=ItUser)
pre_save.connect(pre_save_delete_callback, sender=ItUser)



