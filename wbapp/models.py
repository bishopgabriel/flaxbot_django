from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created = models.DateField(null=True)
    updated = models.DateTimeField(auto_now=True)  #auto_now_add=True

    def __str__(self) -> str:
        return self.username
    # class Meta:
    #     db_table = "wbapp_userprofile"
    #     indexes = models.Index(fields=['username'])