from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details_view, name='profile-details'),
        path('edit/', views.profile_edit_view, name='profile-edit'),
        path('delete/', views.profile_delete_view, name='profile-delete'),
    ])),
]