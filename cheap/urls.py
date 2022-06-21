from django.urls import include, path
from cheap.views import ajax_posting, compute

urlpatterns = [
    path('', include('ajax.urls')),
    path('compute/', compute, name="compute"),
    path('ajax-posting/', ajax_posting, name="ajax_posting")
]