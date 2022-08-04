from django.contrib.auth import get_user_model
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


class AdvertismentCreateUpdateSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    class Meta:
        model = Advertisement
        exclude = ["id", "image"]

    def create(self, validated_data):
        author = validated_data.pop("author")
        category = validated_data.pop("category")

        advertisement = Advertisement.objects.create(**validated_data)

        author_obj, _ = get_user_model().objects.get_or_404(id=author.id)
        advertisement.author.add(author_obj)

        category_obj, _ = Category.objects.get_or_404(id=category.id)
        advertisement.category.add(category_obj)

        advertisement.save()
        return advertisement

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

