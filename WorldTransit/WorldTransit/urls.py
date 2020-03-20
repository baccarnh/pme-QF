
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from WorldTransit import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^login/$',views.login),
    url(r'^blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
