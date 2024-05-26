import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pickle

class RainfallPredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rainfall Prediction App")

        # Load the background image
        self.background_image = Image.open("C:/Users/sulta/Downloads/MP1/background.jpg")
        self.background_image = self.background_image.resize((1600, 1000))  # Resize the background image
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for input fields
        self.frame = ttk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Labels and Entry fields for input data
        self.label_location = ttk.Label(self.frame, text="Location:")
        self.label_location.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.location_entry = ttk.Entry(self.frame)
        self.location_entry.grid(row=0, column=1, padx=5, pady=5)

        self.label_date = ttk.Label(self.frame, text="Date:")
        self.label_date.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.date_entry = ttk.Entry(self.frame)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        # Predict button
        self.predict_button = ttk.Button(self.frame, text="Predict", command=self.predict)
        self.predict_button.grid(row=2, columnspan=2, padx=5, pady=5)

    def predict(self):
        try:
            # Get input data
            location = self.location_entry.get()
            date = self.date_entry.get()

            # Check if both location and date are provided
            if not location or not date:
                messagebox.showwarning("Warning", "Please provide both location and date.")
                return

            # Load trained models
            model_rf = pickle.load(open('model_rf.pkl', 'rb'))
            model_xgb = pickle.load(open('model_xgb.pkl', 'rb'))

            print("Models loaded successfully")

            # Perform prediction for rainfall condition
            #input_data = [12,4.4,12.8,0,2.2,6.1,8,22,8,8,6,7,77,50,1022.5,1019.5,7,4,7.1,12.4,0]
            #input_data = [2,15.9,21.7,2.2,5.6,10.0,13,31.0,3,7,15.0,13.0,89.0,91.0,1010.5,1004.2,8.0,8.0,15.9,17.0,1]
            input_data = [25, 80, 1015, 10, 10.0, 6.0, 20, 20, 30, 20, 12, 14, 90, 60, 1010.0, 1005.0, 15, 10, 8.0, 15.0, 1]

            prediction_rf = model_rf.predict([input_data])[0]
            prediction_xgb = model_xgb.predict([input_data])[0]

            print("Prediction RF:", prediction_rf)
            print("Prediction XGB:", prediction_xgb)

            # Display the prediction using images
            if prediction_rf == 0:
                result_image_path = "C:/Users/sulta/Downloads/MP1/norainfall.jpg"
            else:
                result_image_path = "C:/Users/sulta/Downloads/MP1/rainfall.jpg"

            # Create a new window to display the result image
            result_window = tk.Toplevel(self.root)
            result_window.title("Prediction Result")

            # Load and display the result image
            result_image = Image.open(result_image_path)
            result_image = result_image.resize((1600, 900))  # Resize the result image
            result_photo = ImageTk.PhotoImage(result_image)

            result_label = tk.Label(result_window, image=result_photo)
            result_label.image = result_photo
            result_label.pack()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
app = RainfallPredictionApp(root)
root.mainloop()
