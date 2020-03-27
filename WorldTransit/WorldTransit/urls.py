from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns