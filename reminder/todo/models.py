from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    #  defining the choices and names for each choice inside the model class keeps all 
    # of that information with the class that uses it, and helps reference the choices
    PRIORITY_CHOICES = [(3,"Low"), (2,"Medium"), (1,"High")]
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    schedule = models.DateTimeField()


