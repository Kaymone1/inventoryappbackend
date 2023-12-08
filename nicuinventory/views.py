from django.shortcuts import render

# Create your views here.

from .models import InventoryItem
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import InventoryItemSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = InventoryItem.objects.all()
    # The serializer class for serializing output
    serializer_class = InventoryItemSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]

