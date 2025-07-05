# 🚆 Railway Reservation System

A comprehensive *Railway Reservation System* which is a dymanic fare System developed in *C++ (Console)* and *Python (Tkinter GUI)* that enables users and admins to manage train ticket bookings, station listings, and reservations. Ideal for academic projects or as a prototype for larger transportation systems.

---

## 📁 Project Structure

```
.
├── header.h               # Class & structure definitions  
├── management.cpp         # Core logic (reservations, users, date handling)  
├── main.cpp               # Application flow for admin & user roles (C++ CLI)  
├── railway_gui.py         # Python Tkinter GUI for ticketing  
├── bookings.csv           # (Generated) Stores user bookings from GUI  
├── stations.txt           # List of available stations (for GUI)  
└── user.dat / adm.bin     # Binary storage for users and system data (CLI)  
```

---


## 🚀 Features

### C++ Console Application
- *Admin Features:*
  - Add/delete/view railway stations
  - View all reservations
- *User Features:*
  - Book a train ticket
  - Cancel an existing reservation using CNIC/AADHAR
  - View your Ticket
- *Data Persistence:* Uses fstream to store user credentials, stations, and bookings in binary/text files

### Python GUI Application
- *Modern Interface:* Built with Tkinter and tkcalendar
- *User-friendly booking flow*
- *Admin Panel:*
  - Manage stations
  - View bookings
- *CSV-based Data Storage* for simplicity and portability

---

## 🔧 Requirements

### For C++ Version:
- Windows OS (due to <conio.h> and <Windows.h>)
- C++11 or later
- A C++ compiler (e.g., GCC, MSVC)

### For Python GUI Version:
- Python 3.6+
- Install dependencies:
  bash
  pip install tkcalendar
  

---

## 🎮 How to Run

### ✅ C++ Console Version

1. Compile:
   bash
   g++ main.cpp management.cpp -o railway.exe
   

2. Run:
   bash
   ./railway.exe
   

3. On first run:
   - You’ll be prompted to set up admin and user accounts
   - The system stores them in user.dat

---

### ✅ Python GUI Version

1. Run the GUI:
   bash
   python railway_gui.py
   

2. Use:
   - Login as admin / admin123 for station management
   - Login as user / user123 for booking tickets

---

## 🔐 Authentication

| Role   | Username | Password  |
|--------|----------|-----------|
| Admin  | admin    | admin123  |
| User   | user     | user123   |

> *Note:* C++ credentials are stored in a binary file, while Python GUI uses hardcoded values.

---


## 📌 Future Enhancements

- Add route and time management
- Integrate payment methods
- Migrate data storage to SQLite or MySQL
- Multi-language support
- Use encryption for passwords

---

## 📷 Screenshots

>
![1](https://github.com/user-attachments/assets/19db89b8-3280-4380-8fa7-dd27c75c83bb)
> 
![2](https://github.com/user-attachments/assets/d67f161f-4fbd-46f4-8ca4-b46dac12a815)
>
![3](https://github.com/user-attachments/assets/b04cf3cb-fffa-4449-b3ec-f92f4b07b5ff)
>
![4](https://github.com/user-attachments/assets/c865a2f7-4d86-45e1-8f9a-f11ee5255416)

---

## 👨‍💻 Author

- *C++ System Developer: Aryan Shukla
- *Python GUI Developer: Aryan Shukla
