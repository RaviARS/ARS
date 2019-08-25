from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('signup/', views.signup, name='signup'),
    path('category/', views.category, name='category'),
    path('article-post/', views.article_post, name='article-post'),
    path('article-list/', views.article_list, name='article-list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)