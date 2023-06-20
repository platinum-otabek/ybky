from .serializers import RoomSerializer,OrderSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from .models import RoomModel,OrderModel
from config.paginations import CustomPagination
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime,date


class AllRoomsView(ListCreateAPIView):
    queryset = RoomModel.objects.all()
    serializer_class = RoomSerializer
    pagination_class = CustomPagination

class DetailRoomView(RetrieveAPIView):
    queryset = RoomModel.objects.all()
    serializer_class = RoomSerializer

class AvailableRoomView(APIView):
    def get(self, request, *args, **kwargs):
        room_id = kwargs['room_id']
        user_date = self.request.query_params.get('date')
        day = datetime.strptime(user_date,'%Y-%m-%d') if user_date else date.today()
        orders = OrderModel.objects.filter(begin_time__date=day, room=room_id).order_by('begin_time')
        serializer = OrderSerializer(orders, many=True)

        result = []
        previous_end_time = datetime(day.year, day.month, day.day, 0, 0, 0)
        
        for data in serializer.data:
            begin_time = data['begin_time']
            result.append({
                'begin_time': previous_end_time,
                'end_time': begin_time
            })
            previous_end_time = data['end_time']

        result.append({
            'begin_time': previous_end_time,
            'end_time': datetime(day.year, day.month, day.day, 23, 59, 0)
        })

        return Response(result)
        

class BookRoomView(APIView):
    def get(self,request,*args,**kwargs):
        begin_time = self.request.query_params.get('begin_time')
        end_time = self.request.query_params.get('end_time')
        room_id = kwargs['room_id']
        
        order = OrderModel.objects.filter(
            Q(begin_time__range=(begin_time, end_time)) |
            Q(end_time__range=(begin_time, end_time)),
            room=room_id
        )
        if order.exists():
            return Response(  {"error": "uzr, siz tanlagan vaqtda xona band"},410)
        else:
            data = {'room':room_id,'begin_time':begin_time,'end_time':end_time}
            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return(Response({'message':serializer.error_messages}))
            return Response({"message": "xona muvaffaqiyatli band qilindi"},201)