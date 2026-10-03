---
title: Cartoon Avatar Motion Studio
emoji: 🎨
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

# 🎨 Cartoon Avatar Motion Studio

A cloud-ready, web-based studio designed to bring static cartoon character images to life. Powered by AI voice synthesis and modular animation pipelines, this tool allows you to upload any character, type a script, and generate synchronized talking audio and video assets directly from your browser or mobile phone.

## ✨ Features
* **Custom Avatar Upload:** Upload any cartoon image, illustration, or AI-generated character (PNG/JPG format).
* **AI Voiceover Generation:** Built-in integration with Edge-Neural voices for natural, dynamic, or professional narration.
* **Mobile-Friendly UI:** Designed with Gradio so you can run, manage, and download creations straight from your phone browser.
* **Cloud Ready:** Optimized for free cloud deployment on Hugging Face Spaces.

## 🛠️ Requirements & Setup

This app requires Python and the libraries specified in your `requirements.txt`:
* `gradio`
* `torch`
* `torchvision`
* `numpy`
* `opencv-python`
* `pillow`
* `requests`
* `edge-tts`

## 🚀 Deployment (Hugging Face Spaces)
1. Create a new **Gradio** Space on [Hugging Face](https://huggingface.co/).
2. Upload your `app.py`, `requirements.txt`, and this `README.md` file.
3. Hugging Face will automatically build your app and provide a live web URL to use on your phone!
4. 
