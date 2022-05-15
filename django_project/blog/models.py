from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#  the title, content, etc are models that are mapped im the sqlite database
class Post(models.Model):  # Post represents table in the database
    title = models.CharField(max_length=100)  # CharField is a table inside the model
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
