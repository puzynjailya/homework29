from rest_framework import serializers

from advertisements.models import Advertisement


class AdvertisementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"


class AdvertisementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"


class AdvertisementDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ["id"]

