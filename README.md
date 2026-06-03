# 🐾 Animal Detection System using YOLOv8, Flask, and OpenCV

## 📌 Project Overview

This project is a web-based **Animal Detection System** built using **YOLOv8**, **Flask**, and **OpenCV**. Users can upload an image through a web interface, and the system detects and classifies animals present in the image. The detected animals are highlighted with bounding boxes and confidence scores.

---

## 🚀 Features

* Upload images through a Flask web application
* Real-time animal detection using YOLOv8
* Displays detected animals with bounding boxes
* Shows confidence scores for each detection
* Easy-to-use web interface
* Supports multiple animal classes

---

## 🏷️ Dataset Classes

The model is trained to detect the following 12 animal classes:

| Class ID | Animal   |
| -------- | -------- |
| 0        | Bear     |
| 1        | Buffalo  |
| 2        | Camel    |
| 3        | Cat      |
| 4        | Cow      |
| 5        | Deer     |
| 6        | Dog      |
| 7        | Donkey   |
| 8        | Elephant |
| 9        | Leopard  |
| 10       | Lion     |
| 11       | Tiger    |

Dataset Configuration:

```yaml
path: ../Animal Detection.yolov8
train: train/images
val: valid/images

nc: 12

names:
  - Bear
  - Buffalo
  - Camel
  - Cat
  - Cow
  - Deer
  - Dog
  - Donkey
  - Elephant
  - Leopard
  - Lion
  - Tiger
```

---

## 🛠️ Technologies Used

* Python
* YOLOv8 (Ultralytics)
* Flask
* OpenCV
* HTML/CSS
* NumPy

---

## 📂 Project Structure

```text
Animal-Detection/
│
├── static/
│   ├── uploads/
│   └── results/
│
├── templates/
│   └── index.html
│
├── models/
│   └── best.pt
│
├── app.py
├── requirements.txt
├── README.md
└── dataset.yaml
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/animal-detection.git
cd animal-detection
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📸 How It Works

1. User uploads an image.
2. Flask receives the image.
3. YOLOv8 processes the image and detects animals.
4. OpenCV draws bounding boxes and labels.
5. The processed image is displayed with detection results.
---

## 📊 Sample Output

The system outputs:

* Detected animal names
* Confidence scores
* Bounding boxes around detected animals

Example:

```text
Dog - 95%
Cat - 91%
Elephant - 98%
```

---

## 🔮 Future Enhancements

* Webcam live detection
* Video animal detection
* Animal counting
* Detection history storage
* User authentication
* Cloud deployment

---

## 👨‍💻 Author

Developed as a Computer Vision project using YOLOv8, Flask, and OpenCV for animal detection and classification.

---

## 📄 License

This project is intended for educational and research purposes.
