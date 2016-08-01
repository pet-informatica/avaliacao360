from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Question(models.Model):
	title = models.CharField(max_length=200,verbose_name='Title')
	description = models.TextField(verbose_name='Description')
	mandatory = models.BooleanField(default=True, verbose_name='Is mandatory?')

class Answer(models.Model):
	question = models.ForeignKey('qea.Question', verbose_name="Answering question")
	grade = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)], verbose_name='Given grade')
	comment = models.TextField(verbose_name='Comment', default='')
	target = models.ForeignKey(AUTH_USER_MODEL, verbose_name='Evaluated user')

