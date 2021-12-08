from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

    class Meta():
        verbose_name_plural = "Categories"

class Task(models.Model):
    #  defining the choices and names for each choice inside the model class keeps all 
    # of that information with the class that uses it, and helps reference the choices
    PRIORITY_CHOICES = [(3,"Low"), (2,"Medium"), (1,"High")]
    categories = models.ManyToManyField(Category,)
    title = models.CharField(max_length=30)
    description = models.TextField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    schedule = models.DateTimeField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
