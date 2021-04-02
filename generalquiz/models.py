from django.db import models


# Create your models here.
class GeneralQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    ans = models.CharField(max_length=1)

    def __str__(self):
        return self.question
