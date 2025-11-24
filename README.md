# 🏎️ German Luxury Car Classifier

![FastAI](https://img.shields.io/badge/FastAI-2.0-blue?style=for-the-badge&logo=fastai)
![Python](https://img.shields.io/badge/Python-3.10-yellow?style=for-the-badge&logo=python)
![HuggingFace](https://img.shields.io/badge/Deployed%20on-Hugging%20Face-orange?style=for-the-badge&logo=huggingface)

An AI project that brings German engineering and Deep Learning together. This model can distinguish between the titans of the Autobahn: **Mercedes G-Wagon**, **Porsche 911**, and **Audi RS7**.

---

## 🚀 Live Demo
Don't just take my word for it. Test the engine yourself!

(Click Below👇)

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Open%20App-blue)](SENİN_HUGGING_FACE_LINKIN_BURAYA)

---

## 🧐 How It Works?
I fine-tuned a **ResNet18** model using the **FastAI** library.
1.  **Data Collection:** Scraped images using DuckDuckGo.
2.  **Cleaning:** Removed bad data and handled "tricky" images (like interiors).
3.  **Training:** Used Transfer Learning to achieve **~90% accuracy**.
4.  **Deployment:** Served via Gradio interface.

## ⚔️ The Challenge
The biggest challenge was teaching the model to distinguish a **Porsche 911** from an **Audi RS7** (especially from the rear angle!). By using the `squish` resizing method and data cleaning, I managed to solve the identity crisis.

## 🛠️ Tech Stack
* **Core:** Python, PyTorch, FastAI
* **Interface:** Gradio
* **Deployment:** Hugging Face Spaces

---
*Created by ❤️ CodeAkdo*
