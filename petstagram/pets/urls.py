from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path('add/', views.pet_add_view, name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details_view, name='pet-details'),
        path('edit/', views.pet_edit_view, name='pet-edit'),
        path('delete/', views.pet_delete_view, name='pet-delete'),
    ])),
]
