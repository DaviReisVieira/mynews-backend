from django.db import models
from django.contrib.postgres.fields import JSONField

from mynewsauth.models import CustomUserModel

class StoredNews(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    title = models.TextField()
    content = JSONField()

    def __str__(self):
        return  str(self.id)+". "+str(self.user)+" - "+str(self.title)
