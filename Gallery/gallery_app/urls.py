from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('update-post/<str:id>', views.update_post, name='update-post'),
    path('delete-post/<str:id>', views.delete_post, name='delete-post'),
]