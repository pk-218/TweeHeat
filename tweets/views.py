from django.core import serializers
from django.db import connection
from django.http import JsonResponse

from tweets.models import Tweets


# Create your views here.
def get_tweets(request):
    res = serializers.serialize('geojson', Tweets.objects.raw(
        'SELECT 1 as id, text, %s FROM TWEETS_TWEETS LIMIT 100;' % (connection.ops.select % 'location')
    ), fields=('text',), geometry_field='location')
    return JsonResponse(res, safe=False)
