from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=20)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add =True)
    image = models.ImageField(upload_to = "images/", null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.contents[:100]
