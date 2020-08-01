from django.db import models
from datetime import datetime

#Tuple
SUBJECTS = (
    ('python','Python'),
    ('sql', 'SQL'),
    ('javascript','JavaScript'),
    ('java','Java'),
)

class Question(models.Model):
    subject = models.CharField(max_length=100, choices=SUBJECTS, default=None)
    question = models.TextField()
    opt1 = models.TextField()
    opt2 = models.TextField()
    opt3 = models.TextField(null=True)
    opt4 = models.TextField(null=True)
    correct_answer = models.TextField()


    def __str__(self):
        return self.question

class PracticeResult(models.Model):
    user = models.CharField(max_length=100)
    question = models.TextField()
    selectedOption = models.TextField()
    correctAnswer = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)
    practiceTestNumber = models.IntegerField()

    def __str__(self):
        return self.question
    