from django.db import models,connection
class Article(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    date = models.DateField()
    content = models.TextField()
class Tags(models.Model):
    tag=models.ManyToManyField(Article)
