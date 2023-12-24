from django.urls import path
from movies import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("cards/", views.cards, name="cards"),
    path("contact/", views.contact, name="contact"),
    path("add/", views.add, name="add"),
    path("suggests/", views.suggests, name="suggests"),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]
