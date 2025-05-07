from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=255)
    content_type = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

