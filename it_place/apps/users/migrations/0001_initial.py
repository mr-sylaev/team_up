# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-12 12:00
from __future__ import unicode_literals

import apps.users.models
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import stdimage.models
import stdimage.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Логин')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('specialty', models.CharField(choices=[('bkd', 'бекенд-разработчик'), ('frd', 'фронтенд-разработчик'), ('and', 'android-разработчик'), ('ios', 'ios-разработчик'), ('dsn', 'дизайнер'), ('vrk', 'верстальщик'), ('dsp', 'десктоп-разработчик')], max_length=100, verbose_name='Специальность')),
                ('birth', models.DateField(default=django.utils.timezone.now, verbose_name='Дата рождения')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('img', stdimage.models.StdImageField(null=True, upload_to=apps.users.models.avatar_path, validators=[stdimage.validators.MaxSizeValidator(1028, 768)], verbose_name='Аватар')),
                ('city', models.CharField(choices=[('msk', 'Москва'), ('spb', 'Санкт-петербург'), ('mhk', 'Махачкала'), ('mhk', 'Каспийск'), ('drb', 'Дербент'), ('kzl', 'Кизляр'), ('hsv', 'Хасавюрт')], default='msk', max_length=100, verbose_name='Город')),
                ('experience', models.CharField(max_length=100, verbose_name='Опыт работы')),
                ('education', models.CharField(max_length=100, verbose_name='Образование')),
                ('about', models.TextField(max_length=2000, verbose_name='О себе')),
                ('skills', models.CharField(help_text='Например: Python, Photoshop, CSS, Angular - разделять навыки запятыми', max_length=1000, verbose_name='Навыки')),
                ('edu', models.BooleanField(default=False, verbose_name='Готов обучать')),
                ('edu_list', models.CharField(blank=True, help_text='Например: Python, Photoshop, CSS, Angular', max_length=1000, null=True, verbose_name='Могу обучить')),
                ('github', models.CharField(blank=True, max_length=100)),
                ('bitbacket', models.CharField(blank=True, max_length=100, verbose_name='bitbucket')),
                ('pinterest', models.CharField(blank=True, max_length=100)),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100)),
                ('vk', models.CharField(blank=True, max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'ItUser',
                'verbose_name_plural': 'ItUsers',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'Specialty',
                'verbose_name_plural': 'Specialties',
            },
        ),
    ]
