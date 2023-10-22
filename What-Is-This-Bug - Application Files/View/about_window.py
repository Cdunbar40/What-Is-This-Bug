from tkinter import ttk
from Controller.controller import load_image
from Controller.controller import clear_content
from View.main_window import create_main_window


# Loads the 'About the Model' window
def about_window(root, model):
    # Clear current content
    clear_content(root)

    root.geometry('1200x1000')

    # Prep Figure labels
    label1 = 'This figure shows the number of sample images for each species that the model was trained on.'
    label2 = 'This figure shows the accuracy of the model for each species (as determined from a test set of images).'
    label3 = 'This figure shows the True Positives, True Negatives, False Positives, and False Negatives for each\n' \
             'class based off of the test set.'

    # Construct the path to an image file within the "Images" directory
    path1 = '../Images/Images_By_Species.png'
    path2 = '../Images/Accuracy_By_Class.png'
    path3 = '../Images/Confusion_Matrix.png'

    # Add content for "About the Model"
    about_label = ttk.Label(root, text="About the Model", font=('Helvetica', 18))
    about_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='w')

    # Add your content for "About the Model" here
    about_text = ttk.Label(root, text="This figure shows the number of sample images for each species that the model "
                                      "was trained on.", font=('Helvetica', 14))
    about_text.grid(row=2, column=1, padx=100, pady=10, sticky='w')

    # Create a frame to hold the buttons
    button_frame = ttk.Frame(root, relief='sunken', width=25, height=15)
    button_frame.grid(row=3, column=0, padx=10, pady=10, sticky='n')

    # Create a frame for the graph images
    image_frame = ttk.Frame(root, relief='sunken', width=900, height=850)
    image_frame.grid(row=3, column=1, padx=85, pady=10, rowspan=6, columnspan=3, sticky='nsew')

    load_image(path1, image_frame, about_text, label1)

    # Create the data histogram button
    data_dist_button = ttk.Button(button_frame, text='Data',
                                  command=lambda: load_image(path1, image_frame, about_text, label1),
                                  style='B.TButton')
    data_dist_button.grid(row=3, column=0, padx=10, pady=20)

    # Create the Accuracy histogram button
    model_acc_button = ttk.Button(button_frame, text='Accuracy',
                                  command=lambda: load_image(path2, image_frame, about_text, label2),
                                  style='B.TButton')
    model_acc_button.grid(row=4, column=0, padx=10, pady=20)

    # Create the confusion matrix button
    confusion_button = ttk.Button(button_frame, text='Confusion Matrix',
                                  command=lambda: load_image(path3, image_frame, about_text, label3),
                                  style='B.TButton')
    confusion_button.grid(row=5, column=0, padx=10, pady=20)

    # Create the back button
    back_button = ttk.Button(root, text='Back', command=lambda: create_main_window(root, model), style='B.TButton')
    back_button.grid(row=8, column=0, padx=10, pady=10, sticky='sw')
