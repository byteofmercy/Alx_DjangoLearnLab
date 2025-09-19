from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # any extra fields here

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # ← add this
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
        related_query_name='customuser',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # ← add this
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
        related_query_name='customuser',
    )
