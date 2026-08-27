# Enterprise Inventory Management System

## 📌 Project Overview

Enterprise Inventory Management System is a web-based application developed using Python and 
Django to manage products, customers, and orders efficiently. The system provides an easy-to-use
interface for managing inventory data and performing CRUD operations. 
It includes user authentication and role-based access control to provide secure access to different features.

## 🚀 Features

- 🔐 User Registration and Login
- 👤 User Authentication and Role-Based Access
- 📦 Product Management
- ➕ Add New Products
- ✏️ Edit/Update Products
- 🗑️ Delete Products
- 🖼️ Product Image Upload
- 👥 Customer Management
- 🛒 Order Management
- 📋 Display All Products
- 📊 MySQL Database Integration
- 🎨 Responsive UI using Bootstrap 5
- 🔒 Secure access to application features

## 🛠️ Technologies Used

### Backend
- Python
- Django

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Django Templates

### Database
- MySQL
- MySQL Workbench

### Development Tools
- Visual Studio Code
- Git
- GitHub

## 📂 Project Structure

```text
Enterprise Inventory Management/
│
├── Authentication/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── Inventory/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── Frontend/
│   ├── templates/
│   │   ├── authentication/
│   │   ├── customers/
│   │   ├── orders/
│   │   ├── all_products.html
│   │   ├── add_product.html
│   │   └── base.html
│   └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md

🔑 Authentication

   The application provides user authentication through:

   * User Registration
   * Login
   * Logout
   * Role-based access
   * Protected application features

   Different user roles can be given different permissions for managing products, customers and orders.

📦 Product Management

   The inventory module allows users to:

   * Add new products
   * View all products
   * Update product information
   * Delete products
   * Upload product images
   * Manage product price and GST information
   * Identify food/non-food products

👥 Customer Management

   The customer module allows users to:

   * Add customers
   * View customer information
   * Edit customer details
   * Delete customers

🛒 Order Management

      The order management module provides functionality for managing customer orders and maintaining order-related information.

🎨 User Interface

     The frontend is developed using HTML, CSS and Bootstrap 5 to provide a clean and responsive interface.

     Bootstrap components are used for:

     *  Navigation bar
     *  Buttons
     *  Tables
     *  Forms
     *  Responsive layouts
     *  Alerts and other UI elements
🔒 Security

       The project includes authentication and role-based access control to restrict access to specific operations.

       For production deployment, additional security configurations such as environment variables,
       HTTPS, secure cookies and proper database credentials should be configured.