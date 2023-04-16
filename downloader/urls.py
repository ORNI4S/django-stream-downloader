from django.urls import path
from .views import stream_url


app_name = 'download'
urlpatterns = [
    path('', stream_url.as_view(), name='stream_url'),
]