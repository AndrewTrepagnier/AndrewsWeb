from django.db import models

class StartPage(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    footer_content = models.TextField()
