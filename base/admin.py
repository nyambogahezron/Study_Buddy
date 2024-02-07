from django.contrib import admin

from .models import Room, Topic, Messages, User


admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Messages)
