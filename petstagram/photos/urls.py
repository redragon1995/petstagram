from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path('add/', views.photo_add_view, name='photo-add'),
    path('<int:pk>/', include([
        path('', views.photo_details_view, name='photo-details'),
        path('edit/', views.photo_edit_view, name='photo-edit'),
        path('delete/<int:pk>/', views.photo_delete_view, name='photo-delete'),
    ])),
]