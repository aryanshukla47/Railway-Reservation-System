🚆 Railway Reservation System
A comprehensive Railway Reservation System which is a dymanic fare System developed in C++ (Console) and Python (Tkinter GUI) that enables users and admins to manage train ticket bookings, station listings, and reservations. Ideal for academic projects or as a prototype for larger transportation systems.

📁 Project Structure
.
├── header.h               # Class & structure definitions
├── management.cpp         # Core logic (reservations, users, date handling)
├── main.cpp               # Application flow for admin & user roles (C++ CLI)
├── railway_gui.py         # Python Tkinter GUI for ticketing
├── bookings.csv           # (Generated) Stores user bookings from GUI
├── stations.txt           # List of available stations (for GUI)
└── user.dat / adm.bin     # Binary storage for users and system data (CLI)
🚀 Features
C++ Console Application
Admin Features:
Add/delete/view railway stations
View all reservations
User Features:
Book a train ticket
Cancel an existing reservation using CNIC/AADHAR
View your Ticket
Data Persistence: Uses fstream to store user credentials, stations, and bookings in binary/text files
Python GUI Application
Modern Interface: Built with Tkinter and tkcalendar
User-friendly booking flow
Admin Panel:
Manage stations
View bookings
CSV-based Data Storage for simplicity and portability
🔧 Requirements
For C++ Version:
Windows OS (due to <conio.h> and <Windows.h>)
C++11 or later
A C++ compiler (e.g., GCC, MSVC)
For Python GUI Version:
Python 3.6+
Install dependencies:
pip install tkcalendar
🎮 How to Run
✅ C++ Console Version
Compile:

g++ main.cpp management.cpp -o railway.exe
Run:

./railway.exe
On first run:

You’ll be prompted to set up admin and user accounts
The system stores them in user.dat
✅ Python GUI Version
Run the GUI:

python railway_gui.py
Use:

Login as admin / admin123 for station management
Login as user / user123 for booking tickets
🔐 Authentication
Role	Username	Password
Admin	admin	admin123
User	user	user123
Note: C++ credentials are stored in a binary file, while Python GUI uses hardcoded values.

📌 Future Enhancements
Add route and time management
Integrate payment methods
Migrate data storage to SQLite or MySQL
Multi-language support
Use encryption for passwords
📷 Screenshots
![loginSS](https://github.com/user-attachments/assets/41d4ddd2-54a6-4509-8918-f78a9d55bc20)

![Tickets](https://github.com/user-attachments/assets/a9f649bc-0726-455d-bf5b-bc70b8a8d1df)
![UserBookingTicket](https://github.com/user-attachments/assets/aafc4965-ebba-4cb1-b128-fbebe0969a59)
![AdminPanel](https://github.com/user-attachments/assets/c37ebcf3-e30d-4c69-99f8-96bd6b35ca67)

![BookedFare](https://github.com/user-attachments/assets/3d7734d5-fea4-4089-92cb-5cd616fc5e49)

👨‍💻 Author
  C++ System Developer: Aryan Shukla
Python GUI Developer: Aryan Shukla


