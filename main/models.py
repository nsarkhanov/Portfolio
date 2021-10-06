from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
# class ToDoList(models.Model):
#     name =models.CharField(max_length=255)
#     def __str__(self):
#         return self.name

# class Item(models.Model):
#     todolist=models.ForeignKey(ToDoList,on_delete=models.CASCADE)
#     text=models.CharField(max_length=300)
#     complete=models.BooleanField

#     def __str__(self) :
#         return self.text



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text