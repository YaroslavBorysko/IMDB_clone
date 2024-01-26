from django.contrib import admin

from users.models import Actor, Director, BaseUser


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass

