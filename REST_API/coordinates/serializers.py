from rest_framework import serializers
from .models import Coordinates


class CoordinateSerializer(serializers.Serializer):
  cur_moux = serializers.IntegerField()
  cur_mouy = serializers.IntegerField()
  las_moux = serializers.IntegerField()
  las_mouy = serializers.IntegerField()

  id = serializers.IntegerField()

  def create(self, validated_data):
    return Coordinates.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.cur_moux = validated_data.get('cur_moux', instance.cur_moux)
    instance.cur_mouy = validated_data.get('cur_mouy', instance.cur_mouy)
    instance.las_moux = validated_data.get('las_moux', instance.las_moux)
    instance.las_mouy = validated_data.get('las_mouy', instance.las_mouy)

    instance.save()
    return instance
