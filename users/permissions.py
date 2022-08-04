from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()


class SelectionPermission(permissions.BasePermission):
    message = 'Это мой мессадж! Тут может хулиганить только владелец подборки!'

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.owner_id:
            return True
        return False


class AdvertisementPermission(permissions.BasePermission):
    message = 'Здесь хулиганить могут только владельцы объявления или Админы и модераторы'

    def has_object_permission(self, request, view, obj):
        if (request.user.role not in ['admin', 'moderator']) and (request.user.id != obj.author_id):
            return False
        return True
