import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from converter import convert_images_to_pdf
import os
import sys

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for both development and frozen (PyInstaller) environments. """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Initialize the main window
ctk.set_appearance_mode("dark")  # Optional: "light" or "dark"
root = ctk.CTk()
root.title("Image to PDF Converter")
root.geometry("800x400")
root.configure(fg_color="#011042")  # Background color

image_list = []

# --- Functions ---
def select_images():
    files = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if files:
        image_list.clear()
        image_list.extend(files)
        selected_label.configure(text=f"{len(files)} image(s) selected")

def handle_conversion():
    if not image_list:
        messagebox.showerror("No Images", "Please select image files first.")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save PDF As"
    )

    if save_path:
        convert_images_to_pdf(image_list, save_path)

# 1. JPEG icon 
try:
    img1_path = resource_path("jpeg.png")
    img1 = Image.open(img1_path).resize((110, 100))
    img1_tk = ImageTk.PhotoImage(img1)
    img1_label = ctk.CTkLabel(root, image=img1_tk, text="")
    img1_label.image = img1_tk
    img1_label.place(x=400, y=140)
except Exception as e:
    print(f"Could not load jpeg.png: {e}")

# 2. JPG icon 
try:
    img2_path = resource_path("jpg.png")
    img2 = Image.open(img1_path).resize((110, 100))
    img2_tk = ImageTk.PhotoImage(img2)
    img2_label = ctk.CTkLabel(root, image=img2_tk, text="")
    img2_label.image = img2_tk
    img2_label.place(x=370, y=190)
except Exception as e:
    print(f"Could not load jpg.png: {e}")

# 3. PNG icon 
try:
    img3_path = resource_path("png.png")
    img3 = Image.open(img3_path).resize((110, 100))
    img3_tk = ImageTk.PhotoImage(img3)
    img3_label = ctk.CTkLabel(root, image=img3_tk, text="")
    img3_label.image = img3_tk
    img3_label.place(x=420, y=190)
except Exception as e:
    print(f"Could not load jpeg.png: {e}")

# 4. BMP icon
try:
    img4_path = resource_path("bmp.png")
    img4 = Image.open(img4_path).resize((110, 100))
    img4_tk = ImageTk.PhotoImage(img4)
    img4_label = ctk.CTkLabel(root, image=img4_tk, text="")
    img4_label.image = img4_tk
    img4_label.place(x=400, y=240)
except Exception as e:
    print(f"Could not load jpeg.png: {e}")

# 5. Convert icon
try:
    img5_path = resource_path("paper.png")
    img5 = Image.open(img5_path).resize((220, 160))
    img5_tk = ImageTk.PhotoImage(img5)
    img5_label = ctk.CTkLabel(root, image=img5_tk, text="")
    img5_label.image = img5_tk
    img5_label.place(x=480, y=180)
except Exception as e:
    print(f"Could not load jpeg.png: {e}")

# 6. PDF icon
try:
    img6_path = resource_path("pdf.png")
    img6 = Image.open(img6_path).resize((120, 110))
    img6_tk = ImageTk.PhotoImage(img6)
    img6_label = ctk.CTkLabel(root, image=img6_tk, text="")
    img6_label.image = img6_tk
    img6_label.place(x=600, y=190)
except Exception as e:
    print(f"Could not load jpeg.png: {e}")

# 7. Logo (top center)
try:
    logo_path = resource_path("logo.png")
    logo_img = Image.open(logo_path).resize((120, 60))
    logo_tk = ImageTk.PhotoImage(logo_img)
    logo_label = ctk.CTkLabel(root, image=logo_tk, text="")
    logo_label.image = logo_tk
    logo_label.place(x=340, y=10)
except Exception as e:
    print(f"Could not load logo.png: {e}")

# --- UI Elements ---
select_btn = ctk.CTkButton(
    root, text="Select Images", font=("Arial", 16),
    fg_color="#9ECFE8", text_color="#1A06F6",
    corner_radius=20, command=select_images, width=200, height=40
)
select_btn.place(x=50, y=100)

selected_label = ctk.CTkLabel(
    root, text="No images selected", font=("Arial", 14),
    text_color="#f9006c", bg_color="transparent"
)
selected_label.place(x=80, y=180)

convert_btn = ctk.CTkButton(
    root, text="Convert to PDF", font=("Arial", 16),
    fg_color="#9ECFE8", text_color="#1A06F6",
    corner_radius=20, command=handle_conversion, width=200, height=40
)
convert_btn.place(x=50, y=280)

selected_label1 = ctk.CTkLabel(
    root, text="Select any number of Images and convert them to PDF", font=("Comic Sans MS", 22),
    text_color="#f9006c", bg_color="transparent"
)
selected_label1.place(x=150, y=40)

root.mainloop()

