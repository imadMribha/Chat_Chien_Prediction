# Cat vs Dog Classification

A small Python desktop application that demonstrates a simple supervised image classification workflow. The app lets users build a temporary cat and dog image dataset, train a lightweight model from the uploaded images, and predict whether a selected test image is closer to the cat or dog group.

The project is designed as an educational simulation rather than a production machine learning model. It uses average RGB color values as image features, then compares those values with Euclidean distance.

## Features

- Tkinter graphical interface for uploading images and viewing previews.
- Separate dataset folders for cat and dog examples.
- Simple training step based on average RGB values.
- Test image upload and prediction result display.
- Progress bars for training and prediction actions.
- Dataset clearing option from the interface.
- Included demo video: `Cat_vs_Dog_Classification_Demo.mp4`.

## How It Works

1. Cat and dog images are uploaded through the interface.
2. Each image is resized to `50x50` pixels.
3. The app calculates the average red, green, and blue values for each image.
4. During training, it calculates one average RGB vector for all cat images and one for all dog images.
5. During prediction, the test image RGB vector is compared with both trained averages.
6. The result is shown as a percentage-style comparison between the two classes.

Because this approach only uses color averages, the prediction depends heavily on lighting, background, and image color distribution. It does not understand shapes, faces, fur patterns, or other visual details.

## Project Structure

```text
.
|-- main.py          # Tkinter application and user interface
|-- features.py      # RGB feature extraction from images
|-- train.py         # Training logic for average cat/dog RGB values
|-- predict.py       # Distance-based prediction logic
|-- utils.py         # File upload, dataset handling, and helper functions
|-- requirements.txt # Python dependencies
|-- dataset/         # Generated/used dataset folders
|   |-- cats/
|   `-- dogs/
|-- pics/            # Sample images for testing
`-- README.md
```

## Requirements

- Python 3
- Pillow
- NumPy

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Running the App

Start the desktop application with:

```bash
python main.py
```

## Usage

1. Click **Upload Cat Images** and select one or more cat images.
2. Click **Upload Dog Images** and select one or more dog images.
3. Click **Train Model**.
4. Click **Upload Test Image** and choose an image to classify.
5. Click **Predict** to display the result.
6. Use **Clear Dataset** to remove uploaded dataset images and reset the app.

## Notes and Limitations

- The model is intentionally simple and uses only RGB averages.
- Predictions are not comparable to a real computer vision model.
- Images with similar colors or backgrounds can produce confusing results.
- The app stores uploaded training images inside `dataset/cats` and `dataset/dogs`.
- Clearing the dataset deletes the copied images from those folders.

## Possible Improvements

- Replace RGB averaging with stronger image features or a real machine learning model.
- Fix the prediction percentage formula so the closer class receives the higher confidence score.
- Save trained values so the model does not need to be retrained every time the app opens.
- Add validation for unsupported or corrupted image files.
- Show more detailed prediction information, such as class distances and selected image name.
- Improve the interface layout for smaller screens.
- Add automated tests for feature extraction, training, and prediction logic.
