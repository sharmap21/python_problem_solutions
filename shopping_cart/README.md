# 🛒 Shopping Cart System - Python Solution  

## **📌 Problem Statement**
Design a **Shopping Cart System** that supports the following operations:

1️⃣ **Item Class**
   - Each item has a `name` (string) and a `price` (integer).  
   - Example: `Item("bike", 1000)`

2️⃣ **ShoppingCart Class**
   - Supports `add(item)`, `total()`, and `len(cart)`.  
   - Can store multiple items, including duplicates.

### **🔹 Input Format**

n                # Number of items  
name price       # Item details (repeated for 'n' items)  
q                # Number of operations  
operation_name item_name (if required)  # Operations to be performed  

### **🔹 Sample Inputt**

2
bike 1000
headphones 100
8
total
add bike
len
total
add headphones
add headphones
len
total

### **🔹 Sample outputt**

0
1
1000
3
1200

🚀 Solution Approach

✅ Implemented OOP principles with Item and ShoppingCart classes.
✅ Used lists to store items dynamically.
✅ Overloaded __len__() to support len(cart).
✅ Optimized item retrieval using list iteration.


How to Run code?
command:
python shopping_cart.py







