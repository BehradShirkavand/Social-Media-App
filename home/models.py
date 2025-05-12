from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        
        
    def __str__(self):
        return self.slug
    
    def get_absolute_url(self):
        return reverse("home:post_detail", args=[self.id, self.slug])
    
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    reply= models.ForeignKey("self", on_delete=models.CASCADE, related_name="reply_comments", blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=400)
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} - {self.body}'
    
    
    
    
    
    
    
    
    
    