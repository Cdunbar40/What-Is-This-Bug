import tkinter as tk
import Classifier
import View.main_window

# Main window
root = tk.Tk()
root.title('What-Is-This-Bug?')
model = Classifier.load_model()
View.main_window.create_main_window(root, model)
root.mainloop()
