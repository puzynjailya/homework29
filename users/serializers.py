from _testcapi import raise_exception

from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    password = serializers.CharField(required=False)
    location = serializers.SlugRelatedField(
        many=True,
        slug_field="name",
        required=False,
        queryset=Location.objects.all()
    )

    class Meta:
        model = get_user_model()
        fields = '__all__'

    def is_valid(self, **kwargs):
        self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save()

        for location in self._location:
            location_obj, created = Location.objects.get_or_create(name=location)
            user.location.add(location_obj)
            user.save()
        return user
