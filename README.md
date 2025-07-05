# 🚆 Railway Reservation System

A comprehensive Railway Reservation System which is a dymanic fare System developed in C++ (Console) and Python (Tkinter GUI) that enables users and admins to manage train ticket bookings, station listings, and reservations. Ideal for academic projects or as a prototype for larger transportation systems.

---

## 🧰 Tech Stack

![C++](https://img.shields.io/badge/C%2B%2B-Console-blue?style=for-the-badge&logo=c%2B%2B)
![Python](https://img.shields.io/badge/Python-GUI-yellow?style=for-the-badge&logo=python)
![Tkinter](https://img.shields.io/badge/Tkinter-UI-orange?style=for-the-badge)
![CSV](https://img.shields.io/badge/Data-CSV-green?style=for-the-badge&logo=files)

---

## 📁 Project Structure
.
├── header.h  
# Class & structure definitions
├── management.cpp 
# Core logic (reservations, users, date handling)
├── main.cpp     
# Application flow for admin & user roles (C++ CLI)
├── railway_gui.py
# Python Tkinter GUI for ticketing
├── bookings.csv  
# (Generated) Stores user bookings from GUI
├── stations.txt 
# List of available stations (for GUI)
└── user.dat / adm.bin 
# Binary storage for users and system data (CLI)


---

## 🚀 Features

### 🔷 C++ Console Application

#### 👨‍💼 Admin
- Add / Delete / View Railway Stations
- View All Reservations

#### 🙋‍♂️ User
- Book Train Ticket
- Cancel Ticket (using CNIC/AADHAR)
- View Your Ticket

📦 **Data Persistence:**  
- Uses `fstream` to store user credentials, station list, and reservations in `.dat` and `.bin` files

---

### 🖥️ Python GUI Application

- Built with **Tkinter** and **tkcalendar**
- Modern, user-friendly interface
- Separate Admin and User Panels

#### 👨‍💼 Admin Panel
- Add / Remove Stations
- View All Bookings in Table Format

#### 🙋‍♂️ User Panel
- Select source, destination, date and book ticket
- Auto-saves data to `bookings.csv`

---

## 🔧 Requirements

### ⚙️ C++ Console Version
- Windows OS *(for `<conio.h>` and `<windows.h>`)*
- C++11 or above
- A compiler (GCC, MinGW, or MSVC)

### 🐍 Python GUI Version
- Python 3.6+
- Install required modules:
```bash
pip install tkcalendar
