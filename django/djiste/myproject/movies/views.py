from django.shortcuts import render, redirect
from .form import AddPostForm, ContactPostForm
from movies.models import *

# Create your views here.


menu = [{'title': 'Əsas səhifə', 'url_name': 'home'},
        {'title': 'Məlumat', 'url_name': 'about'},
        {'title': 'Filmlər', 'url_name': 'cards'},
        {'title': 'Əlaqə', 'url_name': 'contact'},
        {'title': 'Sizdən gələnlər', 'url_name': 'suggests'},
        {'title': 'Film əlavə etmək', 'url_name': 'add'},
        ]


def index(request):
    posts = Movies.objects.all()
    cats = Category.objects.all()
    data = {'title': 'Əsas Səhifə', "menu": menu,
            "posts": posts, 'cats': cats, 'cat_selected': 0, }
    return render(request, 'movies/index.html', context=data)



def about(request):
    data = {'title': 'Məlumat', "menu": menu}
    return render(request, 'movies/about.html', context=data)


def add(request):
        if request.method == 'POST':
                form = AddPostForm(request.POST, request.FILES)
                if form.is_valid():
            # print(form.cleaned_data)
                        form.save()
                return redirect('home')

        else:
                form = AddPostForm()

        data = {'title': 'Film əlavə etmək', "menu": menu, 'form': form}
        return render(request, 'movies/add.html', context=data)

def contact(request):
    if request.method == 'POST':
                form = ContactPostForm(request.POST, request.FILES)
                if form.is_valid():
            # print(form.cleaned_data)
                        form.save()
                return redirect('suggests')
    else:
                form = ContactPostForm()
    data = {'title': 'Əlaqə', "menu": menu, 'form': form}
    return render(request, 'movies/contact.html', context=data)


def cards(request):
    posts = Movies.objects.all()
    cats = Category.objects.all()
    data = {'title': 'Filmlər', "menu": menu,
            "posts": posts, 'cats': cats, 'cat_selected': 0, }
    return render(request, 'movies/cards.html', context=data)


def suggests(request):
    contacts = Contacts.objects.all()
    data = {'title': 'Filmlər', "menu": menu,
            "contacts": contacts}
    return render(request, 'movies/suggests.html', context=data)



def show_post(request, post_id):
    posts = Movies.objects.filter(id = post_id)
    data = {'title': 'Əsas Səhifə', "menu": menu,
            "posts": posts, 'post_id': post_id, }
    return render(request, 'movies/index.html', context=data)


def show_category(request, cat_id):
    posts = Movies.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    data = {'title': 'Əsas Səhifə', "menu": menu,
            "posts": posts, 'cats': cats, 'cat_selected': cat_id, }
    return render(request, 'movies/index.html', context=data)

