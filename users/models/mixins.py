from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampMixin(models.Model):
    """
    Mixin to handle created and updated time for specific models.
    """
    created_on = models.DateTimeField(null=True, auto_now_add=True, verbose_name=_("created on"))
    updated_on = models.DateTimeField(null=True, auto_now=True, verbose_name=_("updated on"))

    class Meta:
        abstract = True


class PersonMixin(models.Model):
    """
    Mixin to include the basic fields for
    specific roles of the user in the application.
    """
    name = models.CharField(db_index=True, max_length=150, blank=True, verbose_name=_("name"), )
    birthdate = models.DateField(null=True, blank=True, verbose_name="date of birth")
    biography = models.TextField(max_length=5000, verbose_name=_("biography"))

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"
