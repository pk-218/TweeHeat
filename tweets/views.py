import pandas as pd
from django.core import serializers
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render

from tweets.models import Tweets

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv')


# Create your views here.
def get_tweets(request):
    city = df.loc[df['City'] == 'Washington']
    print(city)
    res = serializers.serialize('geojson', Tweets.objects.raw(
        f'''SELECT 1 as id, text, {(connection.ops.select % 'location')} FROM TWEETS_TWEETS LIMIT 1000;'''
    ), fields=('text',), geometry_field='location')
    return JsonResponse(res, safe=False)


def get_tweets_around(request, city):
    city = df.loc[df['City'] == city]
    print(city)
    res = serializers.serialize('geojson', Tweets.objects.raw(
        f'''SELECT 1 as id, text, {(connection.ops.select % 'location')}
        FROM tweets_tweets
        WHERE ST_DistanceSphere(
            location, ST_MakePoint({float(city.lon)}, {float(city.lat)})) <= 10 * 1609.34 LIMIT 1000;'''
    ))
    return JsonResponse(res, safe=False)


# HTML pages
def get_map(request):
    return render(request, 'tweets/map.html')


def get_map_city(request, city):
    return render(request, 'tweets/map_city.html', context={'city': city})
