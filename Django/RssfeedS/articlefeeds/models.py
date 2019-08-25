from django.db import models
from datetime import datetime

CATEGORY = (
    ('1', 'Sports'),
    ('2', 'Politics'),
    ('3', 'Space'),
    ('4', 'Other'),
)


class PostArticle(models.Model):
    name = models.CharField(max_length=82)
    description = models.TextField()
    images = models.ImageField(upload_to='UploadedFiles/%Y/%b/', blank=True, null=True)
    # images = models.FileField()
    img_captions = models.CharField(max_length=15)
    tags = models.CharField(max_length=82)
    category = models.CharField(max_length=1, choices=CATEGORY)

    date_of_posted = models.DateTimeField(default=datetime.now)
    # user_name = models.CharField(default=User.username, max_length=25)
    email_id = models.EmailField(default='a@gmail.coom', max_length=25)

    def __str__(self):
        return '%s' % self.name
