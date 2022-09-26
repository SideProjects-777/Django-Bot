from django.db import models

# Create your models here.

class TeleSetting(models.Model):
    tg_token = models.CharField(max_length=200)
    tg_chat = models.CharField(max_length=200)
    tg_message = models.CharField(max_length=100)

    def __str__(self) :
        return self.tg_chat
