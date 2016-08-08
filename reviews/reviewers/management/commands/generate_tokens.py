from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
User = get_user_model()

from reviewers.models import UserAnswerToken

class Command(BaseCommand):
	args = 'Arguments are not needed'
	help = 'Use this option to generate a authentication token to all users'

	def handle(self, *args, **options):
		
		UserAnswerToken.objects.all().delete()

		for user in User.objects.all():
			UserAnswerToken.objects.create(user = user, token = get_random_string(length=64))
		
		self.stdout.write("Tokens generate with success!")