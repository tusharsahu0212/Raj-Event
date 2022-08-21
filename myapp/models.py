from distutils.command.upload import upload
from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Images(models.Model):
    img = models.ImageField(upload_to='pics')

class Videos(models.Model):
    video = models.FileField(upload_to='videos',validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
