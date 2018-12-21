from django.urls import path, include

path('', include(('youtube.urls', 'youtube'), namespace='youtube')),
