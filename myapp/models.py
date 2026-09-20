from django.db import models

# Create your models here.
class student (models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    roll = models.IntegerField()
    semester = models.CharField(max_length=255, null=True)
    cgpa = models.FloatField(null=True)


    def __str__(self):
        return f"{self.name} {self.department}"