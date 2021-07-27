from django.db import models

# In order to update database models you need to migrate the changes

# Create your models here.
class Post(models.Model): # Inherit django database models features
    title = models.CharField(max_Length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)