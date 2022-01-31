from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from app.models import Movie
from app.serializers import MovieSerializer
from app.forms import FormMovie

# rest framework
from rest_framework import viewsets


TYPES = [
        {'id':'action', 'name': 'Acción'},
        {'id':'science_fiction', 'name': 'Ciencia Ficción'},
        {'id':'comedy', 'name': 'Comedia'},
        {'id':'terror', 'name': 'Terror'},
        {'id':'drama', 'name': 'Drama'},
        {'id':'suspense', 'name': 'Suspenso'},
        {'id':'romantic', 'name': 'Romantica'},
    ]


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def create(self, request):
        if request.method == "POST":  
            obj = request.POST.dict()
            movie = Movie.objects.create(
                name=obj['name'], 
                duration=int(obj['duration']),
                type=obj['type'],
                producers=obj['producers']
            )
            movie.save()
        return redirect('/home')
    
    def retrieve(self, request, pk=None):
        if not request.session.get('auth'):
            return redirect('init')
        movie = Movie.objects.get(pk=pk)
        return render(request, 'forms/edit_movie.html', {
            'movie': model_to_dict(movie),
            'types': TYPES
        })


def edit(request, pk):
    if request.method == "POST":  
        obj = request.POST.dict()
        Movie.objects.filter(id=pk).update(
            name=obj['name'], 
            duration=float(obj['duration']),
            type=obj['type'],
            producers=obj['producers']
        )
    return redirect('/home')
    

def delete(request, pk):
    Movie.objects.filter(id=pk).delete()
    return redirect('/home')


def show(request):
    if not request.session.get('auth'):
        return redirect('init')
    movies = Movie.objects.all()
    form_movie = FormMovie()
    return render(request, 'forms/index.html', {
        'register_movie': form_movie, 
        'movies': movies,
        'types': TYPES
        })    
