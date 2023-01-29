from django.urls import path
from .views import home, room, createRoom, updateRoom, deleteRoom, loginPage, logoutUser, registerPage, updateMessage, deleteMessage, userProfile, updateUser, topicsPage


urlpatterns = [
    path('login/',loginPage, name='login'),
    path('logout/',logoutUser, name='logout'),
    path('register/',registerPage, name='register'),

    path('', home, name='home'),
    path('room/<str:pk>', room, name='room'),
    path('profile/<str:pk>', userProfile, name='user-profile'),

    path('create-room/', createRoom, name='create-room'),
    path('update-room/<str:pk>', updateRoom, name='update-room'),
    path('delete-room/<str:pk>', deleteRoom, name='delete-room'),

    path('update-message/<str:pk>', updateMessage, name='update-message'),
    path('delete-message/<str:pk>', deleteMessage, name='delete-message'),

    path('update-user/', updateUser, name='update-user'),
    path('topics/', topicsPage, name='topics'),
]