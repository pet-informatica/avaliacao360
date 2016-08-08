from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer