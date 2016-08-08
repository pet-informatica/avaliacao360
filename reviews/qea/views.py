from django.shortcuts import render
from rest_framework.generics import *

from .serializers import *
from .models import *
from reviewers.models import *

class SubmitAnswer(CreateAPIView):
	serializer_class = AnswerSerializer

	def create(self, request, *args, **kwargs):
		token = self.kwargs['token']
		token_map = UserAnswerToken.objects.get(token=token)
		user = token_map.user

		return UserState.objects.filter(reviewer = user)