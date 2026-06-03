from flask import Flask, render_template, request
from ultralytics import YOLO
import cv2
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

model = YOLO("best.pt")

@app.route("/", methods=["GET", "POST"])
def home():
    result_image = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            # Run YOLO prediction
            results = model(filepath)

            plotted_img = results[0].plot()

            result_path = os.path.join(
                RESULT_FOLDER,
                "result_" + file.filename
            )

            cv2.imwrite(result_path, plotted_img)

            result_image = result_path

    return render_template("index.html",
                           result_image=result_image)

if __name__ == "__main__":
    app.run(debug=True)