from _testcapi import raise_exception

from django.contrib.auth import get_user_model
from rest_framework import serializers

from advertisements.models import Advertisement
from selections.models import Selection
User = get_user_model()


class SelectionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ["id", "name"]

class SelectionEntitySerializer(serializers.ModelSerializer):

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

    def is_valid(self, **kwargs):
        self._selection = self.initial_data.pop('items')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        selection = Selection.objects.get(**validated_data)
        selection.save()
        return selection

    def save(self, **kwargs):
        selection = super().save()
        for ad_id in self._selection:
            ad_obj, created = Advertisement.objects.get_or_create(id=int(ad_id))
            selection.items.add(ad_obj)
            selection.save()
        return selection


class SelectionDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ["id"]


