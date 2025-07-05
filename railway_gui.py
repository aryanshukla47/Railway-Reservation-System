
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkcalendar import DateEntry
import csv
import os

# File paths
STATION_FILE = "stations.txt"
BOOKING_FILE = "bookings.csv"
CREDENTIALS = {"admin": "admin123", "user": "user123"}  # Simple user-password dictionary

# Load stations
def load_stations():
    if not os.path.exists(STATION_FILE):
        with open(STATION_FILE, 'w') as f:
            f.write("Delhi\nKanpur\nLucknow\nPatna\nKolkata\n")
    with open(STATION_FILE, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

stations = load_stations()
BASE_FARE = 50

def calculate_fare(source, destination):
    try:
        return abs(stations.index(destination) - stations.index(source)) * BASE_FARE
    except ValueError:
        return 0

def save_booking(data):
    header = ["Name", "CNIC", "Phone", "From", "To", "Date", "Fare"]
    file_exists = os.path.exists(BOOKING_FILE)
    with open(BOOKING_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(data)

def book_ticket_ui():
    def submit():
        name = entry_name.get()
        cnic = entry_cnic.get()
        phone = entry_phone.get()
        source = source_cb.get()
        dest = dest_cb.get()
        date = cal.get_date()

        if not name or not cnic or not phone or source == dest:
            messagebox.showerror("Error", "All fields must be filled and valid.")
            return

        fare = calculate_fare(source, dest)
        save_booking([name, cnic, phone, source, dest, date, fare])
        messagebox.showinfo("Success", f"Ticket booked for ₹{fare}")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Book Ticket")
    top.geometry("350x400")

    tk.Label(top, text="Passenger Name").pack(pady=5)
    entry_name = tk.Entry(top)
    entry_name.pack()

    tk.Label(top, text="CNIC / Aadhar").pack(pady=5)
    entry_cnic = tk.Entry(top)
    entry_cnic.pack()

    tk.Label(top, text="Phone Number").pack(pady=5)
    entry_phone = tk.Entry(top)
    entry_phone.pack()

    tk.Label(top, text="From Station").pack(pady=5)
    source_cb = ttk.Combobox(top, values=stations, state="readonly")
    source_cb.current(0)
    source_cb.pack()

    tk.Label(top, text="To Station").pack(pady=5)
    dest_cb = ttk.Combobox(top, values=stations, state="readonly")
    dest_cb.current(1)
    dest_cb.pack()

    tk.Label(top, text="Travel Date").pack(pady=5)
    cal = DateEntry(top)
    cal.pack()

    tk.Button(top, text="Book Ticket", command=submit, bg="green", fg="white").pack(pady=20)

def view_bookings_ui():
    if not os.path.exists(BOOKING_FILE):
        messagebox.showinfo("No Bookings", "No bookings found.")
        return

    view = tk.Toplevel(root)
    view.title("View Bookings")
    view.geometry("600x300")

    tree = ttk.Treeview(view, columns=("Name", "CNIC", "Phone", "From", "To", "Date", "Fare"), show='headings')
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=80)
    tree.pack(fill='both', expand=True)

    with open(BOOKING_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            tree.insert("", tk.END, values=row)

def cancel_booking_ui():
    cnic = simpledialog.askstring("Cancel Booking", "Enter CNIC / Aadhar to cancel:")
    if not cnic or not os.path.exists(BOOKING_FILE):
        return

    updated = []
    cancelled = False
    with open(BOOKING_FILE, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row[1] == cnic and not cancelled:
                cancelled = True
                continue
            updated.append(row)

    if cancelled:
        with open(BOOKING_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(updated)
        messagebox.showinfo("Cancelled", "Booking cancelled successfully.")
    else:
        messagebox.showinfo("Not Found", "No booking found with given CNIC.")

def admin_panel():
    panel = tk.Toplevel(root)
    panel.title("Admin Panel")
    panel.geometry("300x250")

    def add_station():
        s = simpledialog.askstring("Add Station", "Enter new station name:")
        if s and s not in stations:
            stations.append(s)
            stations.sort()
            with open(STATION_FILE, 'w') as f:
                f.write("\n".join(stations))
            messagebox.showinfo("Success", "Station added.")

    def delete_station():
        s = simpledialog.askstring("Delete Station", "Enter station name to delete:")
        if s in stations:
            stations.remove(s)
            with open(STATION_FILE, 'w') as f:
                f.write("\n".join(stations))
            messagebox.showinfo("Deleted", "Station removed.")

    tk.Button(panel, text="Add Station", command=add_station).pack(pady=10)
    tk.Button(panel, text="Delete Station", command=delete_station).pack(pady=10)
    tk.Button(panel, text="View Bookings", command=view_bookings_ui).pack(pady=10)

def login(role):
    def validate():
        uname = user.get()
        psw = password.get()
        if uname in CREDENTIALS and CREDENTIALS[uname] == psw:
            login_win.destroy()
            if uname == "admin":
                admin_panel()
            else:
                user_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    login_win = tk.Toplevel(root)
    login_win.title("Login")
    login_win.geometry("300x200")
    tk.Label(login_win, text="Username").pack(pady=5)
    user = tk.Entry(login_win)
    user.pack()

    tk.Label(login_win, text="Password").pack(pady=5)
    password = tk.Entry(login_win, show="*")
    password.pack()

    tk.Button(login_win, text="Login", command=validate).pack(pady=10)

def user_menu():
    user_win = tk.Toplevel(root)
    user_win.title("User Menu")
    user_win.geometry("300x300")
    tk.Button(user_win, text="Book Ticket", command=book_ticket_ui).pack(pady=10)
    tk.Button(user_win, text="View Bookings", command=view_bookings_ui).pack(pady=10)
    tk.Button(user_win, text="Cancel Booking", command=cancel_booking_ui).pack(pady=10)

# Main Window
root = tk.Tk()
root.title("Railway Reservation System")
root.geometry("400x300")

tk.Label(root, text="Welcome to Railway Reservation", font=("Arial", 14)).pack(pady=20)
tk.Button(root, text="Login as Admin", command=lambda: login("admin"), width=20).pack(pady=10)
tk.Button(root, text="Login as User", command=lambda: login("user"), width=20).pack(pady=10)

root.mainloop()
