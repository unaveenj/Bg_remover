# Background Removal App

![Background Removal App](https://github.com/unaveenj/Bg_remover/blob/master/App%20icon.png?raw=true)


## Introduction
This application utilizes advanced AI techniques to remove the background from images, making it perfect for creating professional-looking photos, graphics for marketing materials, or any other project where you need a clean image. This app is user-friendly and web-based, built using Streamlit, and can handle images uploaded directly or via URL.

## Features

- **Simple and Intuitive UI**: Easy-to-use interface for uploading images and downloading the result.
- **Supports Various Image Types**: Accepts JPG, JPEG, and PNG image formats.
- **URL Image Uploads**: Allows the addition of images via direct URL input.
- **Instant Results**: Quick background removal process with a spinner to indicate progress.
- **Comparison View**: Side-by-side comparison of the original and background removed image.
- **Download Capability**: Easy download of the result image in PNG format.

## Technologies

- **Python**: Primary programming language.
- **Streamlit**: For creating the web application.
- **rembg**: For the background removal process.
- **Pillow (PIL)**: For image processing.
- **IO and Base64**: For image encoding and downloading functionalities.
- **Requests**: To fetch images from URLs.

## Setup and Installation

1. **Python Installation**: Ensure Python is installed on your system.
2. **Dependency Installation**: Install all the required libraries mentioned in the provided requirements.txt file using the command `pip install -r requirements.txt`.
3. **Running the Application**: Run the application using the Streamlit command `streamlit run app.py`.

## Usage

1. **Start the Application**: Navigate to the web application's URL provided by Streamlit after running the application.
2. **Upload or Input Image**: You can either upload an image directly from your computer or input an image URL into the text box provided.
3. **Image Processing**: The application will display the original image and the image with the background removed side by side.
4. **Download**: Use the download button to save the resulting image with the background removed to your device.

---
This application is a demonstration of using AI for practical and creative image editing. It's designed to be simple and effective, providing users with quick results and a hassle-free experience. Whether you're a professional looking for a quick way to clean up images or someone just exploring the possibilities of AI in image editing, this tool is for you.

