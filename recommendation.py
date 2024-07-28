import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import math
import os

# Crop dataset (same as before)
crop_data = [
    {"crop": "rice", "nitrogen": 80, "phosphorus": 45, "potassium": 40, "ph": 6.5, "temperature": 23, "humidity": 80,
     "rainfall": 200},
    {"crop": "maize", "nitrogen": 70, "phosphorus": 45, "potassium": 20, "ph": 6.5, "temperature": 22, "humidity": 65,
     "rainfall": 80},
    {"crop": "chickpea", "nitrogen": 40, "phosphorus": 60, "potassium": 80, "ph": 7.0, "temperature": 18,
     "humidity": 15, "rainfall": 80},
    {"crop": "kidneybeans", "nitrogen": 20, "phosphorus": 60, "potassium": 20, "ph": 5.8, "temperature": 19,
     "humidity": 20, "rainfall": 100},
    {"crop": "pigeonpeas", "nitrogen": 20, "phosphorus": 60, "potassium": 20, "ph": 5.8, "temperature": 28,
     "humidity": 50, "rainfall": 120},
    {"crop": "mothbeans", "nitrogen": 20, "phosphorus": 40, "potassium": 20, "ph": 6.5, "temperature": 28,
     "humidity": 50, "rainfall": 50},
    {"crop": "mungbean", "nitrogen": 20, "phosphorus": 40, "potassium": 20, "ph": 6.5, "temperature": 28,
     "humidity": 80, "rainfall": 50},
    {"crop": "blackgram", "nitrogen": 40, "phosphorus": 60, "potassium": 20, "ph": 7.0, "temperature": 28,
     "humidity": 65, "rainfall": 70},
    {"crop": "lentil", "nitrogen": 20, "phosphorus": 60, "potassium": 20, "ph": 6.5, "temperature": 22, "humidity": 65,
     "rainfall": 50},
    {"crop": "pomegranate", "nitrogen": 20, "phosphorus": 10, "potassium": 40, "ph": 6.5, "temperature": 22,
     "humidity": 90, "rainfall": 110},
    {"crop": "banana", "nitrogen": 100, "phosphorus": 75, "potassium": 50, "ph": 6.5, "temperature": 27, "humidity": 80,
     "rainfall": 100},
    {"crop": "mango", "nitrogen": 20, "phosphorus": 20, "potassium": 30, "ph": 5.5, "temperature": 30, "humidity": 50,
     "rainfall": 100},
    {"crop": "grapes", "nitrogen": 20, "phosphorus": 125, "potassium": 200, "ph": 6.0, "temperature": 25,
     "humidity": 80, "rainfall": 80},
    {"crop": "watermelon", "nitrogen": 100, "phosphorus": 10, "potassium": 50, "ph": 6.5, "temperature": 25,
     "humidity": 90, "rainfall": 50},
    {"crop": "muskmelon", "nitrogen": 100, "phosphorus": 10, "potassium": 50, "ph": 6.5, "temperature": 28,
     "humidity": 90, "rainfall": 50},
    {"crop": "apple", "nitrogen": 20, "phosphorus": 125, "potassium": 200, "ph": 6.0, "temperature": 22, "humidity": 90,
     "rainfall": 110},
    {"crop": "orange", "nitrogen": 20, "phosphorus": 10, "potassium": 10, "ph": 6.5, "temperature": 25, "humidity": 90,
     "rainfall": 110},
    {"crop": "papaya", "nitrogen": 50, "phosphorus": 50, "potassium": 50, "ph": 6.5, "temperature": 35, "humidity": 90,
     "rainfall": 150},
    {"crop": "coconut", "nitrogen": 20, "phosphorus": 10, "potassium": 30, "ph": 6.0, "temperature": 27, "humidity": 95,
     "rainfall": 150},
    {"crop": "cotton", "nitrogen": 120, "phosphorus": 40, "potassium": 20, "ph": 6.5, "temperature": 25, "humidity": 80,
     "rainfall": 80},
    {"crop": "jute", "nitrogen": 80, "phosphorus": 40, "potassium": 40, "ph": 6.5, "temperature": 25, "humidity": 80,
     "rainfall": 170},
    {"crop": "coffee", "nitrogen": 100, "phosphorus": 20, "potassium": 30, "ph": 6.5, "temperature": 25, "humidity": 60,
     "rainfall": 150}
]


def calculate_distance(soil_data, crop):
    return math.sqrt(
        ((crop["nitrogen"] - soil_data["nitrogen"]) / 100) ** 2 +
        ((crop["phosphorus"] - soil_data["phosphorus"]) / 10) ** 2 +
        ((crop["potassium"] - soil_data["potassium"]) / 100) ** 2 +
        (crop["ph"] - soil_data["ph"]) ** 2 +
        ((crop["temperature"] - soil_data["temperature"]) / 10) ** 2 +
        ((crop["humidity"] - soil_data["humidity"]) / 10) ** 2 +
        ((crop["rainfall"] - soil_data["rainfall"]) / 100) ** 2
    )


def get_crop_recommendations(soil_data):
    distances = [(crop["crop"], calculate_distance(soil_data, crop)) for crop in crop_data]
    sorted_recommendations = sorted(distances, key=lambda x: x[1])
    return [crop for crop, _ in sorted_recommendations[:3]]


class CropRecommendationApp:
    def __init__(self, master):
        self.master = master
        master.title("Crop Recommendation System")
        master.geometry("600x800")

        self.create_widgets()

    def create_widgets(self):
        # Create and place widgets
        ttk.Label(self.master, text="Crop Recommendation System", font=("Arial", 16)).pack(pady=10)

        # Image upload button
        ttk.Button(self.master, text="Upload Soil Health Card Image", command=self.upload_image).pack(pady=10)

        # Image preview
        self.image_preview = ttk.Label(self.master)
        self.image_preview.pack(pady=10)

        # Input fields
        self.entries = {}
        for field in ["nitrogen", "phosphorus", "potassium", "ph", "temperature", "humidity", "rainfall"]:
            frame = ttk.Frame(self.master)
            frame.pack(fill='x', padx=20, pady=5)
            ttk.Label(frame, text=f"{field.capitalize()}:").pack(side='left')
            self.entries[field] = ttk.Entry(frame)
            self.entries[field].pack(side='right', expand=True, fill='x')

        # Location and GPS coordinates
        frame = ttk.Frame(self.master)
        frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame, text="Location:").pack(side='left')
        self.location_entry = ttk.Entry(frame)
        self.location_entry.pack(side='right', expand=True, fill='x')

        frame = ttk.Frame(self.master)
        frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame, text="GPS Coordinates:").pack(side='left')
        self.coordinates_entry = ttk.Entry(frame)
        self.coordinates_entry.pack(side='right', expand=True, fill='x')

        ttk.Button(self.master, text="Get Recommendations", command=self.get_recommendations).pack(pady=20)

        self.result_text = tk.Text(self.master, height=10, width=50)
        self.result_text.pack(padx=20, pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
        if file_path:
            # Display image preview
            image = Image.open(file_path)
            image.thumbnail((200, 200))  # Resize image for preview
            photo = ImageTk.PhotoImage(image)
            self.image_preview.config(image=photo)
            self.image_preview.image = photo  # Keep a reference

            # Simulate extracting data from the image
            self.simulate_data_extraction()

    def simulate_data_extraction(self):
        # In a real application, you would use image processing techniques here
        # For this example, we'll use predefined values
        extracted_data = {
            "nitrogen": 561.0,
            "phosphorus": 19.71,
            "potassium": 166.88,
            "ph": 6.10,
            "temperature": 24.89,  # Example value
            "humidity": 82.0,  # Example value
            "rainfall": 185.95  # Example value
        }

        # Fill in the entry fields with extracted data
        for field, value in extracted_data.items():
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, str(value))

        # Set location and GPS coordinates
        self.location_entry.delete(0, tk.END)
        self.location_entry.insert(0, "Dikling, Pakyong, Sikkim")
        self.coordinates_entry.delete(0, tk.END)
        self.coordinates_entry.insert(0, "88.5953259, 27.2354343")

    def get_recommendations(self):
        try:
            soil_data = {field: float(entry.get()) for field, entry in self.entries.items()}
            recommendations = get_crop_recommendations(soil_data)

            result = "Recommended Crops:\n\n"
            for i, crop in enumerate(recommendations, 1):
                result += f"{i}. {crop}\n"

            location = self.location_entry.get()
            coordinates = self.coordinates_entry.get()
            if location or coordinates:
                result += f"\nLocation: {location}\n"
                result += f"GPS Coordinates: {coordinates}\n"

            self.result_text.delete('1.0', tk.END)
            self.result_text.insert(tk.END, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for all fields.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CropRecommendationApp(root)
    root.mainloop()