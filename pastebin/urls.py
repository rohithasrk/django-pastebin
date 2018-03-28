from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('snippets/', include('snippets.urls')),
    path('admin/', admin.site.urls),
]
