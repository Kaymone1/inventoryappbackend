from .models import InventoryItem
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our InventoryItemSerializer
class InventoryItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = InventoryItem
        # the fields that should be included in the serialized output
        fields = ['id', 'item_name', 'description', 'category', 'quantity', 'unit_cost', 'total_value',
                  'supplier_name', 'supplier_contact', 'reorder_point', 'expiration_date', 'location',
                  'last_updated', 'criticality_level', 'status']
