from django.contrib import admin

from .models import *

admin.site.register(UserState)
admin.site.register(UserAnswerToken)