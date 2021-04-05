from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, DetailView
from .models import Movie, Category, Actor, Genre, RatingStar, Rating
from django.views.generic.base import View
from .forms import ReviewForms, RatingForm
from .models import Movie, Category, Actor, Genre
from django.views.generic.base import View
from .forms import ReviewForms
from django.db.models import Q
# Create your views here.


class GenreYear():
    """Genres and Years of the movies"""

    def get_genres(self):
        return Genre.objects.all()

    def get_genres(self):
        return Genre.objects.all()

    
    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")



class MovieView(GenreYear, ListView):
    """Movies List"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    paginate_by = 3
    

class MovieDetailView(GenreYear, DetailView):
    """Movie Detail View"""
    model = Movie
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context


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



class ActorView(GenreYear, DetailView):
    """Show the info about an actor"""
    model = Actor
    template_name = "movie/actor.html"
    slug_field = "name"


class FilterMoviesView(GenreYear, ListView):
    """Filter Movies"""
    paginate_by = 3

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))).distinct()

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        return context



class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class Search(ListView):
    """Search Film"""
    
    paginate_by = 3
    
    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get("q"))


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

class FilterMoviesView(GenreYear, ListView):
    """Movies filters"""
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) | 
            Q(genres__in=self.request.GET.getlist("genre")))
        return queryset
    
