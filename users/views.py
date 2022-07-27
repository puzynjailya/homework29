import json
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework import generics, viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView

from ads import settings
from advertisements.models import Advertisement
from users.models import User, Location
from users.serializers import UserCreateSerializer, LocationSerializer, UserListSerializer, UserDestroySerializer


class UserListView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserListSerializer


class UserDetailView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserListSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserCreateSerializer



@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = get_user_model()
    fields = ["username",
              "password",
              "first_name",
              "last_name",
              "role",
              "age",
              "location"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        data = json.loads(request.body)

        self.object.username = data.get('username')
        self.object.password = data.get('password')
        self.object.first_name = data.get('first_name')
        self.object.last_name = data.get('last_name')
        self.object.role = data.get('role')
        self.object.age = data.get('age')

        for location in data.get('location'):
            loc, _ = Location.objects.get_or_create(location=location, defaults={"_is_active": "True"})
            get_user_model().location.add(loc)

        self.object.save()

        response = {"id": self.object.id,
                    "username": self.object.username,
                    "first_name": self.object.first_name,
                    "last_name": self.object.last_name,
                    "role": self.object.role,
                    "age": self.object.age,
                    "locations": list(map(str, self.object.location.all()))}

        return JsonResponse(response, status=200)


class UserDeleteView(DestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserDestroySerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

