from tkinter import filedialog, messagebox
import os
import shutil
import uuid
from train import train_model

# Ensure dataset folders exist
def ensure_dataset_folders():
    os.makedirs("dataset/cats", exist_ok=True)
    os.makedirs("dataset/dogs", exist_ok=True)

# Function to upload images
def upload_images(category, image_list, result_label, last_folder="pics"):
    folder = f"dataset/{category}"

    # Open file dialog to select images
    files = filedialog.askopenfilenames(
        title= f"Select {category.capitalize()} Images",
        initialdir=last_folder,
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    for file in files:
        filename = str(uuid.uuid4()) + os.path.splitext(file)[1]  # Generate unique filename
        destination = os.path.join(folder, filename)

        shutil.copy(file, destination)
        image_list.append(destination)

    result_label.config(text=f"{len(image_list)} {category.capitalize()} Images Loaded")

# Function to upload test image
def upload_test_image(result_label, last_folder="pics"):

    # Open file dialog to select test image
    file = filedialog.askopenfilename(
        title="Select Test Image",
        initialdir=last_folder,
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if file:
        result_label.config(text="Test Image Loaded")
        return file
    else:
        result_label.config(text="No Test Image Selected")
        return None

# Function to handle training the model
def handle_train(cat_images, dog_images, result_label):
    cat_avg, dog_avg = train_model(cat_images, dog_images)

    if cat_avg is None or dog_avg is None:
        result_label.config(text="Please upload images to both datasets.")
    else:
        result_label.config(text="Training complete")
        print("Cat Average RGB:", cat_avg)
        print("Dog Average RGB:", dog_avg)

    return cat_avg, dog_avg

# Function to clear dataset folders

def clear_preview(container):
    for widget in container.winfo_children():
        widget.destroy()

def clear_dataset(cat_images, dog_images, cat_section, dog_section, test_section, result_label):

    # Ask for confirmation before clearing the dataset
    confirm = messagebox.askyesno("Confirm", "Delete all dataset images?")
    if not confirm:
        return
    
    # Clear cat folder
    for folder in ["dataset/cats", "dataset/dogs"]:
        if os.path.exists(folder):

            # Remove all files in the folder
            for file in os.listdir(folder):
                path = os.path.join(folder, file)
                os.remove(path)

    # Clear every global variable
    cat_images.clear()
    dog_images.clear()

    clear_preview(cat_section)
    clear_preview(dog_section)
    clear_preview(test_section)

    result_label.config(text="Dataset cleared")


