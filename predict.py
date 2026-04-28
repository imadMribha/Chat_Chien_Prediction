from features import extract_rgb
import math

def euclidean_distance(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

def predict_image(image_path, cat_avg, dog_avg, cat_images, dog_images):
    test_rgb = extract_rgb(image_path)

    # Check if the test image already exists in dataset
    threshold = 0.5 # Tolerence 

    for img in cat_images:
        if euclidean_distance(test_rgb, extract_rgb(img)) < threshold:
            return "Cat 100% , exact match"
    for img in dog_images:
        if euclidean_distance(test_rgb, extract_rgb(img)) < threshold:
            return "Dog 100% , exact match"
    
    # Normal prediction based on distance to average RGB values
    cat_dist = euclidean_distance(test_rgb, cat_avg)
    dog_dist = euclidean_distance(test_rgb, dog_avg)

    total = cat_dist + dog_dist

    if total == 0:
        return "Please use more distinct images."
    
    cat_percentage = (cat_dist / total) * 100
    dog_percentage = (dog_dist / total) * 100

    return f"Cat: {cat_percentage:.1f}%\nDog: {dog_percentage:.1f}%"