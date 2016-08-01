from __future__ import unicode_literals

from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class UserState(models.Model):
	reviewer = models.ForeignKey(AUTH_USER_MODEL, verbose_name='Reviewer', related_name='review_state')
	complete = models.ManyToManyField(AUTH_USER_MODEL, verbose_name='Has reviewed', related_name='reviewed_by')

	class Meta:
		verbose_name = 'User Review State'

class UserAnswerToken(models.Model):
	token = models.CharField(max_length=64, verbose_name='Token')
	user = models.ForeignKey(AUTH_USER_MODEL, verbose_name='User')

	class Meta:
		verbose_name = 'User Answer Token'