from django.urls import path
from .views import LinkCreateView, LinkListView

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('link/create/', LinkCreateView.as_view(), name='link-create'),
]