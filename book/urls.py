from django.urls import path
from .views import (AllRoomsView,DetailRoomView,AvailableRoomView,BookRoomView)

urlpatterns = [
    path('',AllRoomsView.as_view()),
    path('<int:pk>/',DetailRoomView.as_view()),
    path('<int:room_id>/availability/',AvailableRoomView.as_view()),
    path('<int:room_id>/book/',BookRoomView.as_view()),
]