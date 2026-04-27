import tkinter as tk
from utils import ensure_dataset_folders, upload_images, upload_test_image, clear_dataset
from features import extract_rgb
from utils import handle_train
from predict import predict_image

cat_images = [] # Global variables to store cat images
dog_images = [] # Global variables to store dog images
test_image = None # Global variable to store test image path
last_folder = "pics"  # Default folder for file dialog
cat_avg = None # Global variable to store average RGB for cats
dog_avg = None # Global variable to store average RGB for dogs

# Ensure dataset folders exist
ensure_dataset_folders()

# Create main window
root = tk.Tk()
root.title("Cat vs Dog Simulation")
root.geometry("600x400")

# Title 
title_label = tk.Label(root, text="Cat vs Dog Classification", font=("Arial", 16))
title_label.pack(pady=10)

# Wrapper function for uploading test image
def set_test_image():
    global test_image
    test_image = upload_test_image(result_label, last_folder)

    if test_image:
        rgb = extract_rgb(test_image)
        print("Test image RGB:", rgb)

# Wrapper function for training the model
def train():
    global cat_avg, dog_avg
    cat_avg, dog_avg = handle_train(cat_images, dog_images, result_label)

# Wrapper function for predicting the class of the test image
def predict():
    if test_image is None:
        result_label.config(text="Please upload a test image before predicting.")
        return
    
    if cat_avg is None or dog_avg is None:
        result_label.config(text="Please train the model before predicting.")
        return
    
    result = predict_image(test_image, cat_avg, dog_avg, cat_images, dog_images)
    result_label.config(text=result)

# Buttons
btn_upload_cats = tk.Button(
    root, 
    text="Upload Cat Images", 
    command=lambda: upload_images("cats", cat_images, result_label, last_folder))
btn_upload_cats.pack(pady=5)

btn_upload_dogs = tk.Button(
    root, 
    text="Upload Dog Images", 
    command=lambda: upload_images("dogs", dog_images, result_label, last_folder))
btn_upload_dogs.pack(pady=5)

btn_train = tk.Button(root, text="Train Model", command=train)
btn_train.pack(pady=5)

btn_upload_test = tk.Button(root, text="Upload Test Image", command=set_test_image)
btn_upload_test.pack(pady=5)

btn_predict = tk.Button(root, text="Predict", command=predict)
btn_predict.pack(pady=5)

btn_clear = tk.Button(root, text="Clear Dataset", command=lambda: clear_dataset(cat_images, dog_images, result_label))
btn_clear.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="Result will appear here", font=("Arial", 12))
result_label.pack(pady=20)


# Run the app
root.mainloop()