from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    #CASCADE IS to make sure that choices is deleted when the question is deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

#STEPS TO INSERT A QUESTION THORUGH SHELL
#python .\manage.py shelL
#from polls.models import Question,Choice
#Question.objects.all()
#from django.utils import timezone
# q = Question(question_text = "What is your favourite Python framework",pub_date = timezone.now())
#q.save()

#TO SEE THE RESULTS
#q.id
#q.question_text