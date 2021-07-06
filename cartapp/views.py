from django.shortcuts import render, redirect
from .models import FilmDetail
from .forms import film_form


# Create your views here.
def index(request):
    films = FilmDetail.objects.all()
    context = {'film_list': films}
    return render(request, 'index.html', context)


def detail(request, film_id):
    films = FilmDetail.objects.get(id=film_id)
    return render(request, 'detail.html', {'films': films})


def add_movie(request):
    if request.method == 'POST':
        film_name = request.POST.get('film_name')
        film_desc = request.POST.get('film_desc')
        film_year = request.POST.get('film_year')
        film_icon = request.FILES.get('film_icon')
        films = FilmDetail(film_name=film_name, film_desc=film_desc, film_year=film_year, film_icon=film_icon)
        films.save()
    return render(request, 'add.html')


def update(request, id):
    films = FilmDetail.objects.get(id=id)
    form = film_form(request.POST or None, request.FILES, instance=films)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'films': FilmDetail})


def delete(request, id):
    if request.method == 'POST':
        film = FilmDetail.objects.get(id=id)
        film.delete()
        return redirect('/')
    return render(request, 'delete.html')
