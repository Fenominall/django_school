from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DetailView
from .models import Movie
# Create your views here.


class MovieView(ListView):
    """Movies List"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movie/movie_list.html"
    # def get(self, request):
    #     movies = Movie.objects.all()
    #     return render(request, "movie/movies.html", {"movie_list": movies})


class MovieDetailView(DetailView):
    """Movie Detail View"""
    model = Movie
    slug_field = "url"

    # def get(self, request, slug):
    #     movie = Movie.objects.get(url=slug)
    #     return render(request, "movie/movie_detail.html", {"movie": movie})
