from django.urls import path

from selections.views import SelectionListView, SelectionEntityView, SelectionCreateView, SelectionUpdateView, \
    SelectionDestroyView

urlpatterns = [
    path("", SelectionListView.as_view(), name='Selections'),
    path("<int:pk>/", SelectionEntityView.as_view(), name='Selection'),
    path("create/", SelectionCreateView.as_view(), name="Create Selection"),
    path("<int:pk>/update/", SelectionUpdateView.as_view(), name="Update Selection"),
    path("<int:pk>/delete/", SelectionDestroyView.as_view(), name="Destroy Selection"),
]