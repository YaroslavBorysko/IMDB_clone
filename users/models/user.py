from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from users.models.mixins import TimeStampMixin, PersonMixin


class BaseUser(AbstractUser, TimeStampMixin):
    """
    Custom User model that extends Django's built-in AbstractUser model.
    """

    first_name = models.CharField(db_index=True, max_length=150, blank=True, verbose_name=_("first name"),)
    last_name = models.CharField(db_index=True, max_length=150, blank=True, verbose_name=_("last name"))
    username = models.CharField(max_length=150, null=True, unique=False, verbose_name=_("username"))
    email = models.EmailField(blank=True, unique=True, verbose_name=_("email address"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.username}({self.email})"


class Actor(PersonMixin):
    """
    Represents an actor with common personal attributes and actor-specific details.
    """
    # Additional fields specific to the Actor can go here
    pass


class Director(PersonMixin):
    """
    Denotes a film director, inheriting common
    attributes and including director-specific information.
    """
    # Additional fields specific to the Director can go here
    pass


