from django.shortcuts import render
from newsapi import NewsApiClient


# Create your views here.

newsapi = NewsApiClient(api_key='ec84c3f1d9e8452b888ed528b2cc097b')





def bbc(request):	
	top_headlines = newsapi.get_top_headlines(sources='bbc-news')
	bbc_articles=top_headlines['articles']
	context={'item':bbc_articles}
	
	return render(request,'news/news.html',context)

def the_verge(request):
	verge_headlines=newsapi.get_top_headlines(sources='the-verge')
	verge_articles=verge_headlines['articles']
	context={'item':verge_articles}

	return render(request,'news/verge.html',context)

def vice(request):
	vice_headlines=newsapi.get_top_headlines(sources='vice-news')
	vice_articles=vice_headlines['articles']
	context={'item':vice_articles}

	return render(request,'news/vice.html',context)

def aljazeera_news(request):
	alj_headlines=newsapi.get_top_headlines(sources='al-jazeera-english')
	alj_articles=alj_headlines['articles']
	context={'item':alj_articles}

	return render(request,'news/aljazeera_news.html',context)