from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import *

class UserSerializer(serializers.ModelSerializer):

	name = serializers.CharField(source='get_full_name')

	class Meta:
		model = User
		fields = ('id', 'name', 'email')

class UserStateSerializer(serializers.ModelSerializer):

	reviewer = UserSerializer()
	complete = UserSerializer(many=True)
	remain = UserSerializer(many=True, source='get_remain')

	class Meta:
		model = UserState
		fields = ('reviewer', 'complete')