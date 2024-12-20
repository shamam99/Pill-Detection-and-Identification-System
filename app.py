import os
from flask import Flask, request, render_template, redirect, url_for
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploaded"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load the trained model
model = load_model("model.h5")
print("Model loaded successfully!")

# Load the classes
label_encoder_classes = np.load("classes.npy", allow_pickle=True)
print(f"Classes loaded successfully: {label_encoder_classes}")

# Dummy descriptions
descriptions = {
    "Megamox": "Antibiotic for bacterial infections.",
    "Panadol": "Pain reliever and fever reducer.",
    "IbuProfen": "Anti-inflammatory for pain relief.",
    "unknown": "Unknown pill. Please check manually.",
}


def preprocess_image(image_path):
    """
    Preprocess the uploaded image to match the model's input requirements.
    Resizes the image to 480x480 and normalizes it.
    """
    img = load_img(image_path, target_size=(480, 480))
    img_array = img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle the uploaded file
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"

        if file:
            # Save the uploaded file
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            # Preprocess the image
            img_array = preprocess_image(file_path)

            # Use dummy size input
            size_placeholder = np.zeros((1, 2))  

            # Make predictions
            prediction_probs = model.predict([img_array, size_placeholder])
            predicted_label = label_encoder_classes[np.argmax(prediction_probs)]
            predicted_description = descriptions.get(predicted_label, "No usage available.")

            # Return the result
            return render_template(
                "index.html",
                prediction=predicted_label,
                usage=predicted_description,
                img_url=file_path,
            )

    return render_template("index.html")


@app.route("/refresh")
def refresh():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5002)
