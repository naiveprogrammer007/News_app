from django.urls import path
from .views import bbc,the_verge,vice,aljazeera_news

app_name='news'
urlpatterns=[
	path('',bbc,name='bbc-news'),
	path('verge/',the_verge,name='verge-news'),
	path('vice/',vice,name='vice-news'),
	path('aljazeera',aljazeera_news,name='aljazeera-news')
]