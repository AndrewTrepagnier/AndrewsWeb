from django.db import models

class Aboutme1(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    footer_content = models.TextField()

