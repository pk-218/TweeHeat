import pandas as pd
from django.core import serializers
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render

from tweets.models import Tweets

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv')


def sql_select(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    list = []
    i = 0
    for row in results:
        dict = {}
        field = 0
        while True:
            try:
                dict[cursor.description[field][0]] = str(results[i][field])
                field = field + 1
            except IndexError as e:
                break
        i = i + 1
        list.append(dict)
    return list


# Create your views here.
def get_tweets(request):
    city = df.loc[df['City'] == 'Washington']
    print(city)
    res = serializers.serialize('geojson', Tweets.objects.raw(
        f'''SELECT 1 as id, text, {(connection.ops.select % 'location')} FROM TWEETS_TWEETS ORDER BY text LIMIT 5000;'''
    ), fields=('text',), geometry_field='location')
    return JsonResponse(res, safe=False)


def get_tweets_around(request, city):
    city = df.loc[df['City'] == city]
    print(city)
    res = serializers.serialize('geojson', Tweets.objects.raw(
        f'''SELECT 1 as id, text, {(connection.ops.select % 'location')}
        FROM tweets_tweets
        WHERE ST_DistanceSphere(
            location, ST_MakePoint({float(city.lon)}, {float(city.lat)})) <= 5 * 1609.34;'''
    ))
    return JsonResponse(res, safe=False)


def get_state_tweets(request, state):
    res = serializers.serialize('geojson', Tweets.objects.raw(
        f'''SELECT 1 as id, text, {(connection.ops.select % 'location')} FROM TWEETS_TWEETS WHERE state_name='{state.upper()}';'''))
    return JsonResponse(res, safe=False)


def k_means_clustering(request, k, cluster_id):
    res = serializers.serialize('geojson', Tweets.objects.raw(
        f'''
            SELECT 1 as id, text, {(connection.ops.select % 'location')} FROM (SELECT
            ST_ClusterKMeans({(connection.ops.select % 'location')}, {k}) OVER () AS cluster_id, *
            FROM TWEETS_TWEETS) AS X WHERE cluster_id = {cluster_id};
        '''
    ))
    return JsonResponse(res, safe=False)


# HTML pages

def get_map(request):
    return render(request, 'tweets/map.html')


def get_map_city(request, city):
    return render(request, 'tweets/map_city.html', context={'city': city})


def get_map_state(request, state):
    return render(request, 'tweets/map_state.html', context={'state': state})


def get_map_kmeans(request, k, cluster_id):
    return render(request, 'tweets/map_kmeans.html', context={'k': k, 'cluster_id': cluster_id})
