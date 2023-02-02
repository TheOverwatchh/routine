from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Lembrete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=17, default="NotATitle")
    content = models.CharField(max_length=255, default="No more details")
    def __str__(self):
        return f'{self.user.username} precisa se lembrar de {self.title}'

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=36, default="NotATitle")
    time = models.TimeField(auto_now_add=False, null=True, blank=True)
    status = models.CharField(max_length=6, default="undone")
    def __str__(self):
        return f'{self.user.username} precisa {self.title}'

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default="NotATitle")
    description = models.CharField(max_length=299, default="No more details")
    deadline = models.DateField(auto_now_add=False, null=True, blank=True)
    status = models.CharField(max_length=6, default='undone')
    percentage= models.CharField(max_length=6, default='0%')
    def __str__(self):
        return f'{self.user.username} tem uma meta de {self.title} até {self.deadline}'

class miniGoal(models.Model):
     goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     title = models.CharField(max_length=20, default="NotATitle")
     description = models.CharField(max_length=299, default="No more details")
     deadline = models.DateField(auto_now_add=False, null=True, blank=True)
     status = models.CharField(max_length=6, default='undone')
     def __str__(self):
        return f'{self.user.username} tem uma minimeta dentro de {self.goal}'
