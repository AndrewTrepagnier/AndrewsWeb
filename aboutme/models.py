from django.db import models

class Aboutme(models.Model):
    # title = models.CharField(max_length=200)
    # content = models.TextField()
    # date = models.DateField()
    # slug = models.SlugField(unique=True)
    #
    # def __str__(self):
    #     return self.title
    #
    # def get_absolute_url(self):
    #     return f"/post/{self.slug}/"


    title = models.CharField(max_length=100)
    Recommenders = models.TextField()
    content = models.TextField()
    date = models.DateField()

    #Title - Andrew Trepagnier Dot Com
    # Exerpts from letters of recommendations (2)
    # About Me:
    # What is this
    # My Timeline


