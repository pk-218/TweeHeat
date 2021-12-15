from django.contrib import admin

from tweets.models import Tweets, States

# Register your models here.
admin.site.register(Tweets)
admin.site.register(States)
