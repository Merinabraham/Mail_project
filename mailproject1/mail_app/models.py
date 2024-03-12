from django.db import models

class MailForm(models.Model):
    Name = models.CharField(max_length=255)
    Age = models.IntegerField()
    Email = models.EmailField()
    Address = models.TextField()
