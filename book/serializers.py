from rest_framework.serializers import ModelSerializer
from .models import RoomModel,OrderModel

class RoomSerializer(ModelSerializer):
    class Meta:
        model = RoomModel
        fields = ('id','name','type','capacity')

class OrderSerializer(ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ('room','begin_time','end_time')