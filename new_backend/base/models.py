from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='news')
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])

class NewsLike(models.Model):
    news = models.ForeignKey(News, related_name='likes', on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('news', 'ip_address')
