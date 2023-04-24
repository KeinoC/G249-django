from django.urls import path, include
from .views import my_view_function, users, admin

urlpatterns = [
    path('my-url/', my_view_function, name='my-view-name'),
    path('users/', users, name='users'),
    path('admin/', admin.site.urls),
    path('', include('django249.urls')),
]
