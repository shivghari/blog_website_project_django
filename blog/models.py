from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    authoe = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    # important defination to redirect the page after new post form submission.
    def get_absolute_url(self):
        return reverse('post_details', args=[str(self.id)])
    
    