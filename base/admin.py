from django.contrib import admin
from .models import Article, Message, Topic

# Register your models here.
admin.site.register(Article)
admin.site.register(Message)
admin.site.register(Topic)
