import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from Controller.controller import clear_content
from Model import Classifier


# Initializes the main window.
def create_main_window(root, model):
    from View.about_window import about_window

# Open the filebrowser to view images. This method requires the filepath_entry widget.
    def browse_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
        filepath_entry.delete(0, tk.END)  # Clear the current entry
        filepath_entry.insert(0, file_path)  # Insert the selected file path into the entry

# Displays the image in the provided filepath and attempts to classify it
    def upload_image():
        image_path = filepath_entry.get()
        try:
            image = Image.open(image_path)
            image = image.resize((775, 475), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            # Display the image inside the sunken frame
            image_label = ttk.Label(image_frame, image=photo)
            image_label.photo = photo  # Keep a reference to avoid garbage collection
            image_label.grid(row=0, column=0, padx=10, pady=10)
            label, confidence = Classifier.predict(model, image_path)
            confidence = f'{confidence:.2f}'
            result_output.config(text=label)
            confidence_output.config(text=confidence)
        except Exception as e:
            # Handle the case where the image cannot be loaded
            print(f"Error: Could not upload image... {e}")

    clear_content(root)
    root.geometry('1200x800')
    # Create a ttk Style object
    style = ttk.Style()
    style.configure("B.TButton", background='lightblue')

    # Primary Label
    greeting = ttk.Label(root, text='What-Is-This-Bug?', font=('Helvetica', 18))
    greeting.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    # Create a Frame for the image import widgets
    get_image_frame = ttk.Frame(root)
    get_image_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

    # Load Image label
    load_image_label = ttk.Label(get_image_frame, text="Load Image for Identification:", font=('Helvetica', 14))
    load_image_label.grid(row=1, column=1, padx=(20, 10), pady=10)

    # Entry box for image filepath
    filepath_entry = ttk.Entry(get_image_frame, width=60)
    filepath_entry.grid(row=1, column=2, padx=10, pady=10, columnspan=2)

    # Browse button
    browse_button = ttk.Button(get_image_frame, text="Browse", command=browse_image, style="B.TButton")
    browse_button.grid(row=1, column=4, padx=10, pady=10)

    # Upload button
    upload_button = ttk.Button(get_image_frame, text="Upload", command=upload_image, style="B.TButton")
    upload_button.grid(row=1, column=5, padx=10, pady=10)

    # Create an image display Frame below the existing elements
    image_frame = ttk.Frame(root, relief='sunken', width=800, height=500)
    image_frame.grid(row=2, column=0, padx=200, pady=10, columnspan=3, rowspan=3, sticky='nsew')

    # Create a frame for displaying the identification result and the confidence of the classification
    result_frame = ttk.Frame(root)
    result_frame.grid(row=5, column=0, padx=10, pady=10)

    # Create the result label, display box, confidence label, and confidence display box
    result_label = ttk.Label(result_frame, text='Result:', font=('Helvetica', 14))
    result_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')

    result_output = ttk.Label(result_frame, text='', font=('Helvetica', 14))
    result_output.grid(row=5, column=1, padx=10, pady=10, sticky='w')

    confidence_label = ttk.Label(result_frame, text='Confidence:', font=('Helvetica', 14))
    confidence_label.grid(row=5, column=2, padx=10, pady=10, sticky='w')

    confidence_output = ttk.Label(result_frame, text='', font=('Helvetica', 14))
    confidence_output.grid(row=5, column=3, padx=10, pady=10, sticky='w')

    # Create the About the Model button
    about = ttk.Button(root, text="About The Model", command=lambda: about_window(root, model), style="B.TButton")
    about.grid(row=6, column=0, padx=10, pady=50, sticky='sw')
