import qrcode
from tkinter import Tk, Label, Entry, Button, Frame, filedialog
from PIL import Image, ImageTk

# Function to generate UPI payment URL
def generate_upi_url(payee_vpa, payee_name, amount=None, transaction_note=None):
    upi_url = f"upi://pay?pa={payee_vpa}&pn={payee_name}"
    if amount:
        upi_url += f"&am={amount}"
    if transaction_note:
        upi_url += f"&tn={transaction_note}"
    upi_url += "&cu=INR"
    return upi_url

# Function to generate QR code
def generate_qr():
    payee_vpa = vpa_entry.get().strip()
    payee_name = name_entry.get().strip()
    amount = amount_entry.get().strip()
    transaction_note = note_entry.get().strip()

    if not payee_vpa or not payee_name:
        update_status("Error: Payee VPA and Name are required!", "red")
        return

    try:
        amount = float(amount) if amount else None
        upi_payment_url = generate_upi_url(payee_vpa, payee_name, amount, transaction_note)
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(upi_payment_url)
        qr.make(fit=True)

        global qr_image
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_img = ImageTk.PhotoImage(qr_image)
        qr_label.config(image=qr_img)
        qr_label.image = qr_img
        update_status("QR Code Generated Successfully!", "Dark Blue")
    except Exception as e:
        update_status(f"Error: {str(e)}", "red")

# Function to reset inputs and QR code
def reset_qr():
    vpa_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    amount_entry.delete(0, 'end')
    note_entry.delete(0, 'end')
    qr_label.config(image='')
    qr_label.image = None
    update_status("Reset Complete", "Black")

# Function to save the QR code
def download_qr():
    if qr_label.image is None:
        update_status("No QR Code to save!", "red")
        return
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        title="Save QR Code"
    )
    if file_path:
        qr_image.save(file_path)
        update_status("QR Code Saved Successfully!", "Blue")

# Function to update status bar
def update_status(message, color):
    status_label.config(text=message, fg=color)

# Set up the Tkinter window
root = Tk()
root.title("UPI Payment QR Code Generator")
root.geometry("600x750")
root.resizable(False, False)

# Title Label
Label(
    root,
    text="UPI Payment QR Code Generator",
    font=("Helvetica", 22, "bold"),
    bg="#002f6c",
    fg="white",
    pady=10,
).pack(fill="x")

# Input Frame
frame = Frame(root, bg="light blue", relief="groove", bd=2)
frame.place(x=50, y=80, width=500, height=300)

Label(frame, text="Payee VPA:", font=("Arial", 14), bg="Black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
vpa_entry = Entry(frame, width=30, font=("Arial", 12), bg="Black", relief="solid")
vpa_entry.grid(row=0, column=1, padx=10, pady=10)

Label(frame, text="Payee Name:", font=("Arial", 14), bg="Black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
name_entry = Entry(frame, width=30, font=("Arial", 12), bg="black", relief="solid")
name_entry.grid(row=1, column=1, padx=10, pady=10)

Label(frame, text="Amount (optional):", font=("Arial", 14), bg="Black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
amount_entry = Entry(frame, width=30, font=("Arial", 12), bg="Black", relief="solid")
amount_entry.grid(row=2, column=1, padx=10, pady=10)

Label(frame, text="Transaction Note (optional):", font=("Arial", 14), bg="Black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
note_entry = Entry(frame, width=30, font=("Arial", 12), bg="black", relief="solid")
note_entry.grid(row=3, column=1, padx=10, pady=10)

# Buttons
Button(
    frame, text="Generate QR Code", command=generate_qr, font=("Arial", 12), bg="Grey", fg="BlACK", width=15
).grid(row=4, column=0, padx=10, pady=20)

Button(
    frame, text="Reset", command=reset_qr, font=("Arial", 12), bg="Grey", fg="BLACK", width=10
).grid(row=4, column=1, padx=10, pady=20)

# QR Code Display
qr_label = Label(root, bg="Black", relief="solid", bd=2)
qr_label.place(x=150, y=400, width=300, height=300)

# Download Button
Button(
    root, text="Download QR Code", command=download_qr, font=("Arial", 14), bg="#2196f3", fg="Black", width=20
).place(x=180, y=710)

# Status Bar
status_label = Label(root, text="Ready", font=("Arial", 12), bg="#002f6c", fg="Black", relief="flat", anchor="w")
status_label.pack(side="bottom", fill="x")

# Run the Tkinter event loop
root.mainloop()