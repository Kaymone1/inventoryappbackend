from django.db import models

# Create your models here.
class InventoryItem(models.Model):
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_name = models.CharField(max_length=255)
    supplier_contact = models.CharField(max_length=255)
    reorder_point = models.PositiveIntegerField()
    expiration_date = models.DateField()

    # Location
    location = models.CharField(max_length=10)
    # time stamp
    last_updated = models.DateTimeField(auto_now=True)
    # how important they are
    criticality_level = models.CharField(max_length=20, blank=True, null=True)
    #  who is updating the items?
    updated_by = models.CharField(max_length=40, blank=False, null=False)
# see whats going on with items
    status = models.CharField(max_length=20)


