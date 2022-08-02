from _testcapi import raise_exception

from django.contrib.auth import get_user_model
from rest_framework import serializers

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementListSerializer
from selections.models import Selection
User = get_user_model()


class SelectionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ["id", "name"]

class SelectionEntitySerializer(serializers.ModelSerializer):
    items = AdvertisementListSerializer(many=True, read_only=True)

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionCreateSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        many=True,
        queryset=Advertisement.objects.all(),
        slug_field="id",
        required=True
    )

    class Meta:
        model = Selection
        fields = "__all__"


    def create(self, validated_data):
        data = validated_data.pop('items')
        selection = Selection.objects.create(**validated_data)
        for advertisement in data:
            selection.items.add(advertisement)
            selection.save()
        return selection

    def update(self, instance, validated_data):

        items_data = validated_data.pop('items')
        instance.items.clear()

        instance.items.set(items_data)

        fields = ["owner", "name"]
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
                instance.save()
            except KeyError as e:
                print(e)
        return instance


class SelectionDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ["id"]


