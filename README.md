# E-Commerce Website

## Introduction
This is a fully functional **E-Commerce Website** built using **Django**. The platform supports user authentication, product browsing, cart management, and payment integration via Razorpay. The website is designed for seamless deployment on **AWS**.

## Features
- **User Authentication**
  - Signup and Login
  - OTP authentication (via email)
- **Product Management**
  - View and search for products
  - Add products to cart
- **Cart System**
  - Manage items in the cart
  - Proceed to checkout
- **Payment Gateway**
  - Razorpay integration for secure payments
- **Admin Panel**
  - Manage products and orders

### **Steps to Run the Project Locally**
```bash
# Step 1: Clone the Repository
git clone <repository-url>
cd ecom_webapp

# Step 2: Create and Activate Virtual Environment
python -m venv ve
cd ve
scripts/activate/  # On Windows
source bin/activate  # On macOS/Linux
cd ..

# Step 3: Install Dependencies
pip install -r requirements.txt

# Step 4: Setup Database and Migrations
python manage.py makemigrations
python manage.py migrate

# Step 5: Run the Development Server
python manage.py runserver
```

## **Screenshots**


![Screenshot 2024-04-20 163200](https://github.com/pranjalg1331/Ecom_webapp/assets/121032858/0b4ac323-8b07-434d-8d85-949a1c85c7d1)
![Screenshot 2024-04-20 163004](https://github.com/pranjalg1331/Ecom_webapp/assets/121032858/bff81c8f-ca50-4d98-bc0c-edc3b3a9195c)
![Screenshot 2024-04-20 163128](https://github.com/pranjalg1331/Ecom_webapp/assets/121032858/d20483ca-dea2-4126-a89c-9edb7b76effb)

## **Contributing**
Contributions are welcome! If you want to improve this project, feel free to submit a pull request.


### **Happy Coding! 🚀**




