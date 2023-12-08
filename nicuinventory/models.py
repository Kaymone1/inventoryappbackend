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

    # Location split into 8 sections
    LOCATION_CHOICES = [
        ('Section1', 'Section 1'),
        ('Section2', 'Section 2'),
        ('Section3', 'Section 3'),
        ('Section4', 'Section 4'),
        ('Section5', 'Section 5'),
        ('Section6', 'Section 6'),
        ('Section7', 'Section 7'),
        ('Section8', 'Section 8'),
    ]
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    last_updated = models.DateTimeField(auto_now=True)

    CRITICALITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    criticality_level = models.CharField(max_length=20, choices=CRITICALITY_CHOICES, blank=True, null=True)
# see whats going on with items
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Out of Stock', 'Out of Stock'),
        ('Reorder', 'Reorder'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


