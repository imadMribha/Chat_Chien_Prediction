from features import extract_rgb

def average_rgb(rgb_list):
    """
    Calculate the average RGB values from a list of RGB tuples.
    Returns a tuple: (average_red, average_green, average_blue)
    """
    red = sum(rgb[0] for rgb in rgb_list)/len(rgb_list)
    green = sum(rgb[1] for rgb in rgb_list)/len(rgb_list)
    blue = sum(rgb[2] for rgb in rgb_list)/len(rgb_list)

    return (red, green, blue)

def train_model(cat_images, dog_images):
    """
    Train a simple model based on average RGB values of cat and dog images.
    Returns the average RGB values for cats and dogs.
    """
    if len(cat_images) == 0 or len(dog_images) == 0:
        return None, None  # Cannot train without images
    
    cat_rgb = [extract_rgb(image) for image in cat_images]
    dog_rgb = [extract_rgb(image) for image in dog_images]

    cat_avg = average_rgb(cat_rgb)
    dog_avg = average_rgb(dog_rgb)

    return cat_avg, dog_avg