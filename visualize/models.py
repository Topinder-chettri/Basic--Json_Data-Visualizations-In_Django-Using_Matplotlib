from django.db import models

# Create your models here.
class JSONData(models.Model):
    file = models.FileField(upload_to='json/')
    data = models.JSONField(null=True)