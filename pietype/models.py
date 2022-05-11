from django.db import models

class Account(models.Model):
    def __str__(self):
        return f"Account[{self.id}] - {self.name}"

    name = models.CharField("Name", max_length=32)

class Attempt(models.Model):
    raw_wpm = models.IntegerField("Raw WPM")
    wpm = models.IntegerField("WPM")
    accuracy = models.IntegerField("Accuracy")
    datetime = models.DateTimeField("Date", auto_now=True)
    time = models.CharField("Time Elapsed", max_length=20, default="00:00")
    sentence = models.CharField("Sentence", max_length = 4000)
