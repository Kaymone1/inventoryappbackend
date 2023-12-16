# Kay Legendary's NICU Inventory Management - Backend

## API Description

This backend provides a RESTful API for managing inventory data in a Neonatal Intensive Care Unit (NICU). It is built using Django and Django REST Framework.

## How to Access the API

The API is hosted at https://inventoryap-4e7068857990.herokuapp.com/ .

## Endpoints

### 1. Inventory Items

#### 1.1 Get All Items

- **Endpoint:** `/api/inventory/`
- **Method:** GET
- **Description:** Retrieve a list of all inventory items.
- **Example Request:**
  ```http
  GET /api/inventory/

POST /api/items/
Content-Type: application/json

{
  "item_name": "New Item",
  "category": "TestCategory",
  "quantity": 10,
  "description": "This is a new item.",
  "location": "Storage Room",
  "criticality_level": "Medium"
  // ... other fields
}

PUT /api/inventory/1/
Content-Type: application/json

{
  "quantity": 15,
  "location": "New Location"
  // ... other fields to update
}

DELETE /api/inventory/1/

GET /api/dashboard/
