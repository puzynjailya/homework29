from _testcapi import raise_exception

from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import Location

User = get_user_model()


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserRetrieveSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):

    location = serializers.SlugRelatedField(
        many=True,
        slug_field="name",
        required=False,
        queryset=Location.objects.all()
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, **kwargs):
        self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user


    def save(self, **kwargs):
        user = super().save()

        for location in self._location:
            location_obj, created = Location.objects.get_or_create(name=location)
            user.location.add(location_obj)
            user.save()
        return user

class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id"]

