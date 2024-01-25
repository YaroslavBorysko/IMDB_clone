from django.db import models
from django.utils.translation import gettext as _


class UserMovieMixin(models.Model):
    """
    A mixin for common fields related to user and movie in the database.
    """
    user = models.ForeignKey("users.BaseUser", on_delete=models.CASCADE, verbose_name=_("user"))
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, verbose_name=_("movie"))

    class Meta:
        abstract = True
