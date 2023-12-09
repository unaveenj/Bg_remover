import streamlit as st
from rembg import remove
from PIL import Image
import io
import base64
import requests


def remove_bg(image):
    output_image = remove(image)
    return output_image


def get_image_download_link(img, filename, text):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="{filename}">{text}</a>'
    return href


def main():
    logo_url = "https://i.ibb.co/QMKDV8Z/App-icon.png"
    st.image(logo_url, width=200)
    st.title("Background Removal App")

    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])
    url = st.text_input("...or paste an Image URL here")

    if uploaded_file is not None or url:
        try:
            if uploaded_file is not None:
                image_data = uploaded_file.getvalue()
                original_image = Image.open(io.BytesIO(image_data))
            else:
                response = requests.get(url)
                image_data = response.content
                original_image = Image.open(io.BytesIO(image_data))

            st.image(original_image, caption='Original Image', use_column_width=True)

            with st.spinner('Removing background...'):
                result_image = remove_bg(image_data)
                img = Image.open(io.BytesIO(result_image))

            col1, col2 = st.columns(2)

            with col1:
                st.image(original_image, caption='Original Image', use_column_width=True)

            with col2:
                st.image(img, caption='Image with Background Removed', use_column_width=True)

            # Download button
            # st.markdown(
            #     get_image_download_link(img, "background_removed.png", 'Download Image with Background Removed'),
            #     unsafe_allow_html=True)
            st.download_button(label="Download Output Image", data=result_image, mime="image/png")
        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
