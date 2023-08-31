from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('category/<int:post_id>/', category, name='category')
]