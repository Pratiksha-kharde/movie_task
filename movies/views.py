from django.shortcuts import render
from movies.models import Movie, GenreData
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    getmovies = Movie.objects.all()[:100]
    context = {'movies': getmovies}
    return render(request, 'movies/movieindex.html', context)
    #return HttpResponse("Hello, world. You're at the movies index.")

# API to import json data to database - only once
def pushdata_db(request):
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
    for loop in data:
        values = Movie(name=loop['name'], director = loop['director'], imdb_score = loop['imdb_score'],
                       popularity_99 = loop['popularity_99'])
        values.save()
        gen = loop['genre']
        print(loop['genre'])
        for loop1 in gen:
            gentitle = loop1.replace(" ", "")
            getpk = GenreData.objects.get(title=gentitle)
            values.genre.add(getpk.pk)
    return HttpResponse("Process Completed.")

# Search API
@csrf_exempt
def search(request):
    if request.is_ajax():
        keyword = request.POST.get('moviename')
        search_tech = request.POST.get('search_tech')
        print(keyword, search_tech)
        if search_tech=='name':
            getmovies = Movie.objects.filter(name__contains=keyword)
        elif search_tech == 'director':
            getmovies = Movie.objects.filter(director__contains=keyword)
        elif search_tech == 'imdb_score':
            getmovies = Movie.objects.filter(imdb_score=keyword)
        elif search_tech == 'popularity_99':
            getmovies = Movie.objects.filter(popularity_99=keyword)
        elif search_tech == 'genre':
            gdata = GenreData.objects.filter(title=keyword)
            if gdata:
                for loop in gdata:
                    pk=loop.pk
                getmovies = Movie.objects.filter(genre=pk)
            else:
                getmovies = None
        context = {'movies1': getmovies}
        return render(request, 'movies/search_result.html', context)

