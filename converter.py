from PIL import Image
from tkinter import messagebox

def convert_images_to_pdf(image_list,save_path):
    try:
        try:
            from natsort import natsorted
            image_list=natsorted(image_list)
        except ImportError:
            image_list.sort()
        images=[Image.open(img).convert("RGB") for img in image_list]
        images[0].save(save_path,save_all=True,append_images=images[1:])
        messagebox.showinfo("Successfully Converted",f"PDF saved to:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Error",f"Failed to convert images to PDF:\n{e}")