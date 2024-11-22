import qrcode
from tkinter import Tk, Label, Entry, Button, Canvas, Frame, messagebox, filedialog
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
import time


# Function to generate QR code
def generate_qr():
    data = input_entry.get()  # Get input data from the user
    if not data.strip():
        messagebox.showerror("Error", "Please enter some text or URL to generate a QR code!")
        return

    # Update progress bar
    progress_label.config(text="Generating QR Code...")
    progress_bar.start()
    root.update_idletasks()
    time.sleep(1)

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    global qr_image
    qr_image = qr.make_image(fill="black", back_color="white")
    qr_image.save("qrcode.png")

    # Display the QR code in the UI
    qr_img = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_img)
    qr_label.image = qr_img

    # Update progress bar and message
    progress_bar.stop()
    progress_label.config(text="QR Code Generated!")
    input_entry.delete(0, 'end')  # Clear the input field


# Function to reset the displayed QR code
def reset_qr():
    qr_label.config(image='')  # Clear the QR code display
    qr_label.image = None
    input_entry.delete(0, 'end')  # Clear the input field
    progress_label.config(text="Ready")
    messagebox.showinfo("Reset", "QR Code display cleared!")


# Function to download the QR code
def download_qr():
    if qr_label.image is None:
        messagebox.showwarning("No QR Code", "Please generate a QR Code first!")
        return
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        title="Save QR Code"
    )
    if file_path:
        qr_image.save(file_path)
        messagebox.showinfo("Success", "QR Code saved successfully!")


# Function to copy input text to clipboard
def copy_to_clipboard():
    data = input_entry.get()
    if not data.strip():
        messagebox.showwarning("Empty Field", "No text to copy!")
        return
    root.clipboard_clear()
    root.clipboard_append(data)
    root.update()
    messagebox.showinfo("Copied", "Text copied to clipboard!")


# Function to add a gradient background
def draw_gradient(canvas, width, height):
    gradient_colors = ["#005f99", "#00a36c", "#4caf50"]  # Blue-to-green gradient
    steps = len(gradient_colors) - 1

    for i in range(steps):
        color1 = canvas.winfo_rgb(gradient_colors[i])
        color2 = canvas.winfo_rgb(gradient_colors[i + 1])
        r_diff = (color2[0] - color1[0]) // height
        g_diff = (color2[1] - color1[1]) // height
        b_diff = (color2[2] - color1[2]) // height

        for y in range(height // steps):
            r = color1[0] + (r_diff * y)
            g = color1[1] + (g_diff * y)
            b = color1[2] + (b_diff * y)
            hex_color = f"#{r >> 8:02x}{g >> 8:02x}{b >> 8:02x}"
            canvas.create_rectangle(0, y + (i * height // steps), width, (y + 1) + (i * height // steps), outline="", fill=hex_color)


# Set up the Tkinter window
root = Tk()
root.title("QR Code Generator")
root.geometry("600x700")

# Create a canvas for the gradient background
canvas = Canvas(root, width=600, height=700)
canvas.pack(fill="both", expand=True)
draw_gradient(canvas, 600, 700)

# Title label
Label(
    root,
    text="QR Code Generator",
    font=("Helvetica", 26, "bold"),
    bg="#005f99",  # Matching the gradient
    fg="white",
    pady=10,
    relief="groove",
).place(x=150, y=30)

# Frame for input and buttons
frame = Frame(root, bg="light grey", relief="solid", bd=1)
frame.place(x=70, y=120, width=460, height=150)

# Input field for data
Label(
    frame, text="Enter text or URL:", font=("Arial", 16), bg="light blue", fg="black"
).grid(row=0, column=0, padx=10, pady=10)
input_entry = Entry(
    frame, width=30, font=("Arial", 14), relief="flat", highlightbackground="WHITE", highlightthickness=2
)
input_entry.grid(row=0, column=1, padx=10, pady=10)

# Buttons for Generate, Clear, Download, and Copy
Button(
    frame,
    text="Generate",
    command=generate_qr,
    font=("Arial", 14, "bold"),
    bg="#4caf50",
    fg="BLACK",
    relief="raised",
    padx=15,
    pady=5,
).grid(row=1, column=0, padx=10, pady=10)

Button(
    frame,
    text="Clear",
    command=reset_qr,
    font=("Arial", 14, "bold"),
    bg="#f44336",
    fg="BLACK",
    relief="raised",
    padx=15,
    pady=5,
).grid(row=1, column=1, padx=10, pady=10)

Button(
    frame,
    text="Download",
    command=download_qr,
    font=("Arial", 14, "bold"),
    bg="#2196f3",
    fg="BLACK",
    relief="raised",
    padx=15,
    pady=5,
).grid(row=2, column=0, padx=10, pady=10)

Button(
    frame,
    text="Copy Text",
    command=copy_to_clipboard,
    font=("Arial", 14, "bold"),
    bg="#ff9800",
    fg="BLACK",
    relief="raised",
    padx=15,
    pady=5,
).grid(row=2, column=1, padx=10, pady=10)

# Progress bar for generating QR code
progress_bar = Progressbar(root, orient="horizontal", length=500, mode="indeterminate")
progress_bar.place(x=50, y=300)
progress_label = Label(root, text="Ready", font=("Arial", 12), bg="#ffffff", fg="#005f99")
progress_label.place(x=270, y=330)

# Label to display QR Code
qr_label = Label(root, bg="#ffffff", relief="solid", bd=2)
qr_label.place(x=150, y=370, width=300, height=300)

# Footer
Label(
    root,
    text="Developed by MJ",
    font=("Arial", 12, "italic"),
    bg="#005f99",  # Gradient matching color
    fg="white",
    pady=5,
    relief="flat",
).pack(side="bottom", fill="x")

# Start the Tkinter event loop
root.mainloop()