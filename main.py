import tkinter as tk
from utils import ensure_dataset_folders, upload_images, upload_test_image, clear_dataset
from features import extract_rgb
from utils import handle_train
from predict import predict_image
from PIL import Image, ImageTk
from tkinter import ttk

cat_images = [] # Global variables to store cat images
dog_images = [] # Global variables to store dog images
test_image = None # Global variable to store test image path
last_folder = "../pics"  # Default folder for file dialog
cat_avg = None # Global variable to store average RGB for cats
dog_avg = None # Global variable to store average RGB for dogs

# Ensure dataset folders exist
ensure_dataset_folders()

#Function to create sidebar buttons
def create_sidebar_button(text, command, bg="#3498db"):
    return tk.Button(
        left_frame,
        text=text,
        command=command,
        bg=bg,
        fg="white",
        font=("Arial", 11, "bold"),
        activebackground=bg,
        activeforeground="white",
        relief="flat",
        padx=10,
        pady=10,
        cursor="hand2"
    )

# Function for uploading test image
def set_test_image():
    global test_image
    test_image = upload_test_image(result_label, last_folder)

    if test_image:
        rgb = extract_rgb(test_image)
        print("Test image RGB:", rgb)
        show_images([test_image], test_images_frame)

# Function for training the model
def train():
    train_progress["value"] = 0

    def fill_progress(value=0):
        if value<=100:
            train_progress["value"] = value
            root.after(20, fill_progress, value+1)
        else:
            global cat_avg, dog_avg
            cat_avg, dog_avg = handle_train(cat_images, dog_images, result_label)

    fill_progress()

# Function for predicting the class of the test image
def predict():
    if test_image is None:
        result_label.config(text="Please upload a test image.")
        return
    
    if cat_avg is None or dog_avg is None:
        result_label.config(text="Please train the model first.")
        return
    
    predict_progress["value"] = 0

    def fill_progress(value=0):
        if value <= 100:
            predict_progress["value"] = value
            root.after(20, fill_progress, value + 1)
        else:
            result = predict_image(test_image, cat_avg, dog_avg, cat_images, dog_images)
            result_label.config(text=f"Prediction Result:\n\n{result}")

    fill_progress()

# Function to display images in the preview sections
def show_images(image_paths, container):
    for widget in container.winfo_children():
        widget.destroy()

    max_images = 5
    size = (70, 70)

    for path in image_paths[:max_images]:
        img = Image.open(path).convert("RGB")
        img = img.resize(size)
        img_tk = ImageTk.PhotoImage(img)

        image_box = tk.Frame(container, bg="white", bd=1, relief="solid")
        image_box.pack(side="left", padx=6, pady=4)

        label = tk.Label(image_box, image=img_tk, bg="white")
        label.image = img_tk
        label.pack()

    if len(image_paths) > max_images:
        more_label = tk.Label(
            container,
            text=f"+{len(image_paths) - max_images}\nmore",
            bg="white",
            fg="#3498db",
            font=("Arial", 11, "bold"),
            width=8,
            height=4,
            relief="solid",
            bd=1
        )
        more_label.pack(side="left", padx=10, pady=4)

# Function for clearing the averages
def clear_all():
    global test_image, cat_avg, dog_avg

    cleared = clear_dataset(
        cat_images,
        dog_images,
        cat_images_frame,
        dog_images_frame,
        test_images_frame,
        result_label
    )

    if cleared:
        test_image = None
        cat_avg = None
        dog_avg = None


# Create main window
root = tk.Tk()
root.title("Cat vs Dog Simulation")
root.geometry("1000x650")
root.configure(bg="#f4f6f8")

# Main layout
root.grid_columnconfigure(0, minsize=400, weight=0) #left 1/3
root.grid_columnconfigure(1, weight=1) #right 2/3
root.grid_rowconfigure(0, weight=1)

# Left panel
left_frame = tk.Frame(root, bg="#132238", padx=20, pady=20 , width=400)
left_frame.grid(row=0, column=0, sticky="nsew")
left_frame.grid_propagate(False)

# Right panel
right_frame = tk.Frame(root, bg="#f4f6f8", padx=20, pady=20)
right_frame.grid(row=0, column=1, sticky="nsew")

right_frame.grid_columnconfigure(0, weight=1)
right_frame.grid_rowconfigure(0, minsize=140, weight=0)
right_frame.grid_rowconfigure(1, minsize=140, weight=0)
right_frame.grid_rowconfigure(2, minsize=140, weight=0)
right_frame.grid_rowconfigure(3, minsize=160, weight=0)

# Left Title 
title_label = tk.Label(
    left_frame, 
    text="CAT vs DOG\nClassification", 
    font=("Arial", 22, "bold"),
    bg="#132238",
    fg="white"
)
title_label.pack(pady=(10, 30))

# Cat preview section
cat_section = tk.Frame(
    right_frame,
    bg="white",
    height=130,
    bd=1,
    relief="ridge"
)
cat_section.grid(row=0, column=0, sticky="nsew", pady=8)
cat_section.grid_propagate(False)

cat_title = tk.Label(
    cat_section,
    text="Cat Dataset",
    bg="white",
    fg="#e67e22",
    font=("Arial", 12, "bold")
)
cat_title.pack(anchor="w", padx=10, pady=(5, 0))
cat_images_frame = tk.Frame(cat_section, bg="white")
cat_images_frame.pack(fill="both", expand=True, padx=10, pady=5)

# Dog preview section
dog_section = tk.Frame(
    right_frame,
    bg="white",
    height=130,
    bd=1,
    relief="ridge"
)
dog_section.grid(row=1, column=0, sticky="nsew", pady=8)
dog_section.grid_propagate(False)

dog_title = tk.Label(
    dog_section,
    text="Dog Dataset",
    bg="white",
    fg="#3498db",
    font=("Arial", 12, "bold")
)
dog_title.pack(anchor="w", padx=10, pady=(5, 0))
dog_images_frame = tk.Frame(dog_section, bg="white")
dog_images_frame.pack(fill="both", expand=True, padx=10, pady=5)

#Test image preview section
test_section = tk.Frame(
    right_frame,
    bg="white",
    height=130,
    bd=1,
    relief="ridge"
)
test_section.grid(row=2, column=0, sticky="nsew", pady=8)
test_section.grid_propagate(False)

test_title = tk.Label(
    test_section,
    text="Test Image",
    bg="white",
    fg="#16a085",
    font=("Arial", 12, "bold")
)
test_title.pack(anchor="w", padx=10, pady=(5, 0))
test_images_frame = tk.Frame(test_section, bg="white")
test_images_frame.pack(fill="both", expand=True, padx=10, pady=5)

# Result area placeholder on right panel
result_label = tk.Label(
    right_frame, 
    text="Prediction Result\n\nResult will appear here", 
    font=("Arial", 20, "bold"),
    bg="#eafaf1",
    fg="#1e8449",
    padx=20,
    pady=20,
    relief="ridge",
    bd=2,
    justify="center"
)
result_label.grid(row=3, column=0, sticky="ew", pady=8)

# -------------------- Buttons --------------------
btn_upload_cats = create_sidebar_button(
    "Upload Cat Images",
    lambda: (
        upload_images("cats", cat_images, result_label, last_folder),
        show_images(cat_images, cat_images_frame)
    )
)
btn_upload_cats.pack(fill="x", pady=8)

btn_upload_dogs = create_sidebar_button(
    "Upload Dog Images", 
    lambda: (
        upload_images("dogs", dog_images, result_label, last_folder),
        show_images(dog_images, dog_images_frame)
    )
)
btn_upload_dogs.pack(fill="x", pady=8)

btn_train = create_sidebar_button("Train Model", train)
btn_train.pack(fill="x", pady=8)

# Progress bar for training 
train_progress = ttk.Progressbar(left_frame, orient="horizontal", length=200, mode="determinate")
train_progress.pack(fill="x", pady=(0, 8))

btn_upload_test = create_sidebar_button("Upload Test Image", set_test_image)
btn_upload_test.pack(fill="x", pady=8)

btn_predict = create_sidebar_button("Predict", predict)
btn_predict.pack(fill="x", pady=8)

# Progress bar for prediction
predict_progress = ttk.Progressbar(left_frame, orient="horizontal", length=200, mode="determinate")
predict_progress.pack(fill="x", pady=(0, 8))

btn_clear = create_sidebar_button("Clear Dataset", clear_all, bg="#e74c3c")
btn_clear.pack(fill="x", pady=8)

# Run the app
root.mainloop()