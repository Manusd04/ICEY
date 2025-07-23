# ❄️ ICEY — Intelligent Captioning Engine for You

ICEY is a web-based application that uses the **BLIP (Bootstrapped Language Image Pretraining)** model from Salesforce to generate intelligent captions for images.

Simply upload an image, click a button, and get a human-like caption powered by state-of-the-art machine learning.

---

## 🚀 Demo

Try it live (if hosted): [ICEY Live Demo](https://your-link-if-hosted.gradio.live)  
*Note: If running locally, follow the steps below.*

---

## 🧠 Model Used

This project uses the [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base) model from Hugging Face Transformers.

---

## 🛠️ Installation

### 1. Clone the repository
```bash
https://github.com/Manusd04/ICEY.git
cd icey-caption-generator
````

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🖼️ How to Use

```bash
python app.py
```

This will launch the app locally.
To get a shareable public link:

```python
demo.launch(share=True)
```

---

## 🧾 Features

* Upload images directly
* Generates a caption using BLIP
* Clean UI with feedback options
* Lightweight and fast

---

## 🧠 Tech Stack

* [Gradio](https://gradio.app/)
* [PyTorch](https://pytorch.org/)
* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [BLIP Image Captioning Model](https://huggingface.co/Salesforce/blip-image-captioning-base)

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

Thanks to:

* [Salesforce Research](https://github.com/salesforce/BLIP)
* [Gradio Team](https://github.com/gradio-app/gradio)
* [Hugging Face](https://huggingface.co/)

---

Let me know if you'd like to include screenshots or customize sections like **Deployment on Hugging Face Spaces**, or a GIF demo!
```
