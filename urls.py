from django.urls import path, include
from .views import my_view_function, users, admin
from django.contrib.auth.views import login

urlpatterns = [
    path('my-url/', my_view_function, name='my-view-name'),
    path('users/', users, name='users'),
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    # Include any other URL patterns for your project here
]
