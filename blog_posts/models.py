from django.db import models
from datetime import datetime

# In order to update database models you need to migrate the changes

# Create your models here.
class Post(models.Model): # Inherit django database models features
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)