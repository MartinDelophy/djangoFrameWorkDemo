from django.db import models
from rest_framework import serializers


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    text = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.question_text
    class Meta:
        verbose_name = '提问'
        verbose_name_plural = '提问'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    class Meta:
        verbose_name = '问题选择'
        verbose_name_plural = '问题选择'
