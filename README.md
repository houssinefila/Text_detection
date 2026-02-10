# Real-Time Text Detection with EasyOCR

## 📌 Description

This project demonstrates real-time text detection using a webcam with **OpenCV** and **EasyOCR**. The program captures video frames from the camera, detects text in each frame, and displays the detected text with bounding boxes.

This is useful for:

* OCR experiments
* Computer vision learning
* Text detection from live video streams
* Automation and AI projects

---

## ⚙️ Requirements

Make sure you have Python installed (recommended Python 3.9–3.10 for compatibility).

### Required libraries:

Install them using pip:

```bash
pip install opencv-python easyocr matplotlib
```

If you want GPU acceleration (recommended):

* Install PyTorch with CUDA first: [https://pytorch.org/](https://pytorch.org/)

---

## ▶️ How It Works

1. The webcam is opened using OpenCV.
2. EasyOCR processes each frame to detect text.
3. Detected text is displayed:

   * Bounding box around text
   * Recognized text label above it
4. Press **q** to quit the application.

---

## 🚀 How to Run

Simply execute:

```bash
python your_script_name.py
```

Make sure your webcam is connected.

If camera index `1` doesn’t work, try:

```python
cap = cv2.VideoCapture(0)
```

---

## 🧠 Main Technologies Used

* **OpenCV** → Camera capture and image processing
* **EasyOCR** → Optical Character Recognition
* **Matplotlib** → Imported but not required for core functionality

---

## ⚠️ Notes

* GPU mode (`gpu=True`) requires CUDA-compatible hardware.
* Detection speed depends on your computer performance.
* Lighting conditions affect OCR accuracy.

---

## 📷 Output Example

The program displays:

* Live webcam feed
* Detected text highlighted in purple

---

## 👨‍💻 Author

Created for computer vision experimentation and OCR learning.

You can improve it by:

* Adding multiple languages
* Saving detected text
* Improving UI
* Integrating with AI pipelines

---

## ⭐ Future Improvements

* Export recognized text to file
* Add GUI interface
* Improve accuracy using preprocessing
* Deploy as a desktop application

---

**Enjoy experimenting with OCR and Computer Vision! 🚀**
