from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not Found</h1>")


def main(request):
    content = MyMeal.objects.all()
    context = {
        "title": "MyMeals",
        "content": content,
    }
    return render(request, 'base.html', context=context)


def category(request, post_id):
    return HttpResponse(f"<h1>Category</h1><p>{post_id}</p>")



