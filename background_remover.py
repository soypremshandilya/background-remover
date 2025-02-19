import tkinter as tk
from tkinter import filedialog, messagebox
from rembg import remove
from PIL import Image, ImageTk
import os

def select_image():
    """Opens a file dialog to select an image."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)
        display_image(file_path)

def remove_bg():
    """Removes background and saves the image as PNG."""
    input_path = entry_path.get()
    
    if not input_path:
        messagebox.showerror("Error", "Please select an image file!")
        return

    output_path = os.path.splitext(input_path)[0] + "_no_bg.png"
    
    try:
        with Image.open(input_path) as img:
            img_no_bg = remove(img)
            img_no_bg.save(output_path, format="PNG")
        messagebox.showinfo("Success", f"Background removed! Saved as: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

def display_image(image_path):
    """Displays the selected image in the UI."""
    img = Image.open(image_path)
    img.thumbnail((300, 300)) 
    img = ImageTk.PhotoImage(img)
    
    panel.config(image=img)
    panel.image = img  

root = tk.Tk()
root.title("Background Remover")
root.geometry("500x500")
root.resizable(False, False)

tk.Label(root, text="Select an Image:", font=("Arial", 12)).pack(pady=10)

entry_path = tk.Entry(root, width=50)
entry_path.pack(pady=5)

tk.Button(root, text="Browse", command=select_image).pack(pady=5)
tk.Button(root, text="Remove Background", command=remove_bg, bg="green", fg="white").pack(pady=10)

panel = tk.Label(root)
panel.pack(pady=10)

root.mainloop()
