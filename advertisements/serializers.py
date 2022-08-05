from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from advertisements.models import Advertisement
from categories.models import Category


class AdvertisementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"


class AdvertisementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=get_user_model().objects.all())
    category = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Category.objects.all())

    class Meta:
        model = Advertisement
        exclude = ["id", "image"]

    def is_valid(self, raise_exception=False):
        self._author = self.initial_data.get("author")
        self._category = self.initial_data.get("category")
        super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        advertisement = Advertisement.objects.create(**validated_data)

        try:
            category_obj = Category.objects.get(id=self._category)
            advertisement.category_id = category_obj.id
        except Category.DoesNotExist:
            raise Http404("Given query not found....")

        try:
            author_obj = get_user_model().objects.get(id=self._author)
            advertisement.author_id = author_obj.id
        except get_user_model().DoesNotExist:
            raise Http404("Given query not found....")

        advertisement.save()

        return advertisement


class AdvertisementUpdateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    class Meta:
        model = Advertisement
        exclude = ["id", "image"]

    def update(self, instance, validated_data):

        category_data = validated_data.pop("category")
        instance.category_id = category_data

        fields = ["name", "price", "description", "is_published"]
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
                instance.save()
            except KeyError as e:
                print(e)

        return instance




class AdvertisementDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ["id"]

