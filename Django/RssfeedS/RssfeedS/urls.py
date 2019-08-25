from django.contrib import admin
from django.urls import path, include
from articlefeeds import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('rss-feeds/', include('articlefeeds.urls')),

    path('article-post/', views.article_post),
    path('article-list/', views.article_list),
    path('article-edit/<int:id>', views.article_edit),
    path('article-update/<int:id>', views.article_update),
    path('article-delete/<int:id>', views.article_destroy),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
