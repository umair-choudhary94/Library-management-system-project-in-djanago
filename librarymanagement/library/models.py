from django.db import models



class Book(models.Model):
    namee = models.CharField(max_length=400)
    timestamp = models.DateTimeField(null=False,blank=False,auto_now_add=True)
    def __str__(self):
        return self.namee
