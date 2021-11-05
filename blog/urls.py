from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('category/list', views.category_list, name="category_list"),
    path('category/draft', views.category_draft_list, name='category_draft_list'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('category/new/', views.category_new, name='category_new'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category/<int:pk>/publish/', views.category_publish, name='category_publish'),
    path('categpry/<int:pk>/unpublish', views.category_unpublish, name='category_unpublish'),
    path('category/<int:pk>/remove/', views.category_remove, name='category_remove'),
    
    path('post/list', views.post_list, name="post_list"),
    path('post/draft', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/unpublish', views.post_unpublish, name='post_unpublish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/priority_up/', views.post_priority_up, name='post_priority_up'),
    path('post/<int:pk>/priority_down/', views.post_priority_down, name='post_priority_down'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)