from django.urls import path 
from . import views


urlpatterns = [
    path('' , views.AvailbleRooms),
    path('create/' , views.Createroom),
    path('modify/<int:pk>/', views.RoomModify),
    path('join/<int:pk>/' , views.JoinRoom)
]

"""
    main apis for ROOMS

    ==> api/rooms/              (all rooms)
    ==> api/rooms/create/       (add room)
    ==> api/rooms/modify/       (modify room)
    ==> api/rooms/join/   (joinnnnnn)
"""