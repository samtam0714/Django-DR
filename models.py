from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
 
 #class finalscore(models.Model): 
 #   finalscore = models.PositiveSmallIntegerField(default=0)

 #   def __str__(self):
 #       return self.description

#class score(models.Model):
    