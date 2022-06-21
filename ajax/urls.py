
from django.urls import path

from ajax.views import create, create_post, index, signup


urlpatterns = [
    path('login/', index, name='index'),
    path('create_post', create_post, name="create_post"),
    path('signup/', signup, name='signup'),
    path('create', create, name='create'),
]