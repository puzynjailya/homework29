from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()


class SelectionPermission(permissions.BasePermission):
    message = 'Это мой мессадж! Тут может хулиганить только владелец подборки!'

    def has_permission(self, request, view):
        if request.owner != User.pk:
            False
        return True

