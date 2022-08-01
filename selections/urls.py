from django.urls import path

from selections.views import SelectionListView, SelectionEntityView, SelectionCreateView

urlpatterns = [
    path("", SelectionListView.as_view(), name='Selections'),
    path("<int:pk>/", SelectionEntityView.as_view(), name='Selection'),
    path("create/", SelectionCreateView.as_view(), name="Create Selection")
]