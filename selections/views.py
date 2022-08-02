from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from selections.models import Selection
from selections.serializers import SelectionListSerializer, SelectionEntitySerializer, SelectionDestroySerializer, \
    SelectionCreateSerializer
from users.permissions import SelectionPermission


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionListSerializer


class SelectionEntityView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionEntitySerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated, SelectionPermission]


class SelectionDestroyView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDestroySerializer
    permission_classes = [IsAuthenticated, SelectionPermission]
