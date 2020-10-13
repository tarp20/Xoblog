from django.db import models


class Article(models.Model):
    article_title = models.CharField(max_length=100)
    article_text = models.TextField()
    pub_date = models.DateTimeField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=300)
