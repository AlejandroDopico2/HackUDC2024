from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    username = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False, default='')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'user'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"