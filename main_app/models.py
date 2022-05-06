from django.db import models


class Question(models.Model):
    question_id = models.CharField(max_length=100)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=500)
    date_of_creation = models.DateField()

    def __str__(self):
        return self.question_id



