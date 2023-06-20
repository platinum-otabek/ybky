from django.db import models
from datetime import datetime
# Create your models here.
class RoomModel(models.Model):
    ROOM_TYPE = (
        ('team','Team'),
        ('focus','Focus'),
        ('conference','Conference')
    )
    name = models.CharField(max_length=25,default='')
    type = models.CharField(max_length=10,default='',choices=ROOM_TYPE)
    capacity = models.PositiveSmallIntegerField(default=1)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table='room'
    
class OrderModel(models.Model):
    room = models.ForeignKey(RoomModel,on_delete=models.SET_NULL,null=True,
                             related_name='reservations')
    begin_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return str(self.room.id)
    
    class Meta:
        db_table = 'order'