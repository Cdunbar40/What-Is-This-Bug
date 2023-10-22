from tkinter import ttk
from PIL import Image, ImageTk


def load_image(filepath, image_frame, label, text):
    try:
        image = Image.open(filepath)

        image = image.resize((875, 825), Image.ANTIALIAS)

        photo = ImageTk.PhotoImage(image)

        # Display the image inside the sunken frame
        image_label = ttk.Label(image_frame, image=photo)
        image_label.photo = photo  # Keep a reference to avoid garbage collection
        image_label.grid(row=0, column=0, padx=10, pady=10)

        label.config(text=text)

    except Exception as e:
        # Handle the case where the image cannot be loaded
        print(f"Error: {e}")


def clear_content(root):
    for widget in root.winfo_children():
        widget.destroy()
