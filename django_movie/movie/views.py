from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DetailView
from .models import Movie, Category, Actor
from django.views.generic.base import View
from .forms import ReviewForms
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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context

    # def get(self, request, slug):
    #     movie = Movie.objects.get(url=slug)
    #     return render(request, "movie/movie_detail.html", {"movie": movie})


class AddReview(View):
    """Reviews"""
    def post(self, request, pk):
        form = ReviewForms(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie  # прописав форму из базы данных можно передавать значение
            form.save()
        return redirect(movie.get_absolute_url())



class ActorView(DetailView):
    """Show the info about an actor"""
    model = Actor
    template_name = "movie/actor.html"
    slug_field = "name"