from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    # 아래는 필요 없어서, 일단 패스
    # spouse_name = models.CharField(blank=True, max_length=100)
    # date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email

