from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120,null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=600,null=True)
    assign_to = models.ForeignKey(User,on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.title



