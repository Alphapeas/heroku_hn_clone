from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from .managers import UserManager


class User(AbstractUser):
    """News user"""
    email = models.EmailField(_('email address'), null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_(
        "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    phone = models.CharField(
        _('phone'),
        max_length=17,
        null=True,
        blank=True,
        validators=[phone_regex],
    )
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    updated_at = models.DateTimeField(_('date updated'), auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'user'
