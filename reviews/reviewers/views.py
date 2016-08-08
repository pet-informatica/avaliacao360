from django.shortcuts import render
from rest_framework.generics import *

from .serializers import *
from .models import *

class GetState(CreateAPIView):
	serializer_class = UserStateSerializer

	def create(self, request, *args, **kwargs):
		token = self.kwargs['token']
		token_map = UserAnswerToken.objects.get(token=token)
		user = token_map.user

		return UserState.objects.filter(reviewer = user)