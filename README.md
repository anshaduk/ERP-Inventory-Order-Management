## ERP Inventory & Order Management System

This project is a backend API for a basic Inventory and Order Management system built using Django, Django REST Framework and PostgreSQL. It provides endpoints for managing products, suppliers, stock levels, and processing orders.

## Features

1. Product Management: Create and list products with their details
2. Supplier Management: Add and track supplier information
3. Inventory Tracking: Monitor stock levels for each product
4. Order Processing: Create orders with automatic stock updates

## API Endpoints
1. GET/api/products/    ...............>List all products
2. POST/api/products/   ...............>Add a new product
3. GET/api/suppliers/   ...............>List all suppliers
4. POST/api/suppliers/  ...............>Add a new supplier
5. GET/api/orders/      ...............>List all orders
6. POST/api/orders/     ...............>Place a new order (updates stock)
