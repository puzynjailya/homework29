from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView

from selections.models import Selection
from selections.serializers import SelectionListSerializer, SelectionEntitySerializer, SelectionDestroySerializer, \
    SelectionCreateSerializer


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionListSerializer


class SelectionEntityView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionEntitySerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer


class SelectionDestroyView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDestroySerializer
