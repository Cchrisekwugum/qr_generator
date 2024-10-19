import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

def generate_qr_code(data, size=10, color="black", bg_color="white"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,  # Size of each box in the QR code
        border=4  # The white border around the QR code
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)  # Make sure the data fits
    
    # Create the image of the QR code
    img = qr.make_image(fill_color=color, back_color=bg_color)
    
    return img

# Streamlit UI
st.title("QR Code Generator")

# Input field for the URL or text to encode
url = st.text_input("Enter the file URL or text to encode in the QR Code:")

# Input sliders for customizing the QR code
size = st.slider("Select the QR code size (box size):", min_value=1, max_value=20, value=10)
color = st.color_picker("Pick the QR code color:", value="#000000")
bg_color = st.color_picker("Pick the background color:", value="#FFFFFF")

# Generate the QR code when the button is clicked
if st.button("Generate QR Code"):
    if url:
        qr_img = generate_qr_code(url, size=size, color=color, bg_color=bg_color)
        
         # Convert to downloadable PNG
        buffer = BytesIO()
        qr_img.save(buffer, format="PNG")
        buffer.seek(0)
        
        # Display the QR code
        st.image(buffer, caption="Your QR Code", use_column_width=True)

       
        # Provide download link
        st.download_button(
            label="Download QR Code as PNG",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.error("Please enter a valid URL or text.")
