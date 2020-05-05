from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.Serializer):
    las_moux = serializers.IntegerField()
    las_mouy = serializers.IntegerField()
    title = serializers.CharField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.las_moux = validated_data.get('las_moux', instance.las_moux)
        instance.las_mouy = validated_data.get('las_mouy', instance.las_mouy)

        instance.save()
        return instance
