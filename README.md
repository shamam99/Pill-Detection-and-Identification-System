# Pill Detection and Identification System

This project is dedicated to creating a solution for identifying pills based on their images, designed primarily to assist visually impaired individuals in safely identifying medications. The project consists of a trained model for pill classification and a simple testing interface using Flask and HTML.

---

## Story Behind the Project

The motivation for this project stems from the need to assist blind and visually impaired individuals in independently identifying pills. By leveraging deep learning and accessible technology, this project aims to improve safety and self-reliance in medication management.

In the future, this project will be expanded into an iOS application with additional features, such as integration with accessibility tools, enhanced datasets, and real-time processing capabilities.

---

## Features

1. **Trained Model**:
   - Built using TensorFlow and trained on a custom pill dataset.
   - Achieved a high accuracy of 99.9% during training and 95.2% on validation data.
   - Incorporates image size data for improved predictions.

2. **Testing Interface**:
   - A simple and intuitive web-based interface developed using Flask and HTML.
   - Allows users to upload an image of a pill for testing.
   - Displays the predicted pill name and its usage.

3. **Scalable Plans**:
   - Future development includes an iOS application with enhanced features.

---

## Dataset

- The dataset used for this project consists of images of pills categorized into classes like `Panadol`, `IbuProfen`, and `Megamox`.
- For privacy and licensing reasons, the dataset is currently unavailable for public access.

---

## How It Works

1. **Training**:
   - The training was performed using the [provided Jupyter Notebook](./project.ipynb), which includes preprocessing, augmentation, and model evaluation steps.
   - The model uses a MobileNetV2 backbone with a custom output layer for pill identification.

2. **Testing**:
   - The testing interface allows users to upload an image.
   - The model predicts the pill name and usage based on the uploaded image.

---

## Installation

To use this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pill-detection.git
   cd pill-detection
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # For macOS/Linux
   .venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Place the required files in the project directory:
   - `model.h5`: The trained model.
   - `classes.npy`: The classes used during training.

5. Run the Flask application:
   ```bash
   python app.py
   ```

6. Open the application in a browser:
   ```
   http://127.0.0.1:5002/
   ```

---

## Project Structure

```plaintext
PILL DETECTION/
├── static/
│   ├── uploaded/            # Uploaded images are stored here
│   ├── styles.css           # (Optional) Styling for the interface
├── templates/
│   ├── index.html           # Frontend template for Flask
├── app.py                   # Flask application
├── classes.npy              # Encoded classes
├── model.h5                 # Trained model
├── requirements.txt         # Dependencies
└── project.ipynb            # Jupyter Notebook for training
```

---

## Technologies Used

- **Deep Learning**: TensorFlow, Keras.
- **Web Framework**: Flask.
- **Frontend**: HTML5, CSS.
- **Image Processing**: OpenCV, NumPy.

---

## How to Use

1. Upload an image of a pill via the provided interface.
2. Click "Start Testing" to get the prediction.
3. The prediction will display:
   - **Pill Name**
   - **Usage**

4. Refresh the page to test another image.

---

## Libraries and Environment

Ensure the following libraries are installed before running the project:

- Flask
- TensorFlow
- NumPy
- Scikit-learn
- OpenCV

Install them using:
```bash
pip install -r requirements.txt
```

---

## Future Enhancements

1. Develop an iOS application with the following features:
   - Real-time pill detection using the camera.
   - Enhanced accessibility for visually impaired individuals.
   - Larger and more diverse datasets for improved accuracy.
2. Incorporate voice assistance and text-to-speech features.
3. Allow custom datasets for user-specific pill identification.

---

## Contributors

- **Shamam Alkafri**
  - **Role**: Backend and Model Development
  - **Contact**: shamam.kafri@gmail.com

Feel free to contribute to this project by forking the repository and submitting pull requests!

---

## License

This project is open-source and available under the MIT License. See the LICENSE file for more information.
