from django.contrib import admin
from .models import Post

# To migrate the models to the admin panel we need to set up admin.py
# Register your models here.
admin.site.register(Post)