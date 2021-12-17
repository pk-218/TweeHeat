"""tweeheat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tweets.views import get_tweets, get_map, get_tweets_around, get_map_city, get_state_tweets, get_map_state, \
    k_means_clustering, get_map_kmeans

urlpatterns = [
    path('admin/', admin.site.urls),
    path('json/all-tweets/', get_tweets),
    path('json/tweets-around/<city>', get_tweets_around),
    path('json/state/<state>', get_state_tweets),
    path('json/kmeans/<k>/<cluster_id>', k_means_clustering),
    path('', get_map),
    path('<city>/', get_map_city),
    path('state/<state>/', get_map_state),
    path('kmeans/<k>/<cluster_id>', get_map_kmeans)
]
