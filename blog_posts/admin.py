from django.contrib import admin
# To migrate the models to the admin panel we need to set up admin.py
from .models import Post

# Register your models here.
admin.site.register(Post)