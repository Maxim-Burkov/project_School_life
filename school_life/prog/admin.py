from django.contrib import admin

from.forms import ProfileForm
from .models import Profile
from .models import Homework

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'external_id', 'name']
    form = ProfileForm

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'text', 'created_at']

    # def get_queryset(self, request):
      #  return


