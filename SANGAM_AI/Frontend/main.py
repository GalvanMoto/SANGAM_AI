from io import BytesIO
import streamlit as st
import requests
from PIL import Image
from pydub import AudioSegment
from pydub.playback import play

# Function to display the home page
def home_page():
    st.title("SANGAM AI")
    st.write("AI INTEGRATED TOOLKIT.")
    st.write("Select from Navigation")

# Function to display the text generation page
def text_generation_page():
    # Streamlit UI
    st.title("Text Generation AI Chatbot")

    # Flask server URL
    FLASK_URL = "http://localhost:5000/generate-text"

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    prompt = st.chat_input("Ask your question here:")
    if prompt:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in the chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Make a request to the Flask server
    response = requests.post(FLASK_URL, json={"prompt": prompt})

    # Parse the response
    if response.status_code == 200:
        data = response.json()
        generated_text = data.get("output")

        # Add AI message to chat history
        st.session_state.messages.append({"role": "assistant", "content": generated_text})

        # Display AI message in the chat
        with st.chat_message("assistant"):
            st.markdown(generated_text)
    else:
        st.error("Failed to generate text. Please try again.")
            
def tti():
   # URL for the Flask backend
    backend_url = "http://127.0.0.1:5000/generate-image"

    st.title("Text-to-Image AI with Stable Diffusion")

    prompt = st.text_input("Enter your prompt:")

    if "image" not in st.session_state:
        st.session_state.image = None

    def generate_image_from_prompt(prompt):
        try:
            response = requests.post(backend_url, json={"prompt": prompt})
            if response.status_code == 200:
                # Try to open the image from the response
                image = Image.open(BytesIO(response.content))
                return image
            else:
                st.error("Error generating image: " + response.json().get("error", "Unknown error"))
                return None
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return None

    if st.button("Generate Image"):
        if prompt:
            with st.spinner("Generating image..."):
                st.session_state.image = generate_image_from_prompt(prompt)
                if st.session_state.image:
                    st.image(st.session_state.image)
        else:
            st.warning("Please enter a prompt.")

    if st.session_state.image is not None:
        if st.button("Regenerate Image"):
            if prompt:
                with st.spinner("Regenerating image..."):
                    st.session_state.image = generate_image_from_prompt(prompt)
                    if st.session_state.image:
                        st.image(st.session_state.image)
            else:
                st.warning("Please enter a prompt.")

    # Add a check before saving to ensure image exists
    if st.session_state.image:
        buf = BytesIO()
        st.session_state.image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(
            label="Download Image",
            data=byte_im,
            file_name="generated_image.png",
            mime="image/png",
        )
    else:
        st.warning("No image to save.")
   
def tts():

    # URL of the Flask API
    FLASK_API_URL = "http://localhost:5000/generate-audio"

    # Available voices
    available_voices = {
        "Voice 1": "v2/en_speaker_0",
        "Voice 2": "v2/en_speaker_1",
        "Voice 3": "v2/en_speaker_2",
        "Voice 4": "v2/en_speaker_3",
        "Voice 5": "v2/en_speaker_4",
    }

    # Streamlit app layout
    st.title("Text-to-Speech App with Bark")
    text_prompt = st.text_area("Enter text to convert to speech", "")
    selected_voice = st.selectbox("Select Voice", list(available_voices.keys()))

    if st.button("Generate Audio"):
        if not text_prompt:
            st.error("Please enter some text.")
        else:
            # Prepare data for POST request
            payload = {
                "text": text_prompt,
                "speaker": available_voices[selected_voice]
            }

        # Send request to Flask API
        response = requests.post(FLASK_API_URL, json=payload)

        if response.status_code == 200:
            # Load audio data from the response
            audio_data = BytesIO(response.content)
            st.audio(audio_data, format="audio/wav")
            st.success("Audio generated successfully!")
        else:
            st.error("Failed to generate audio.")

def ttv():
    st.title("Text to Video")
    # Streamlit UI
    st.title("AI Video Generator")
    st.write("Generate a video using AI and a text prompt.")

    # Input prompt
    prompt = st.text_input("Enter your prompt:", "Darth Vader surfing a wave")

    # Generate video button
    if st.button("Generate Video"):
        with st.spinner("Generating video... This might take a while."):
            try:
                # Send a request to the Flask backend
                backend_url = "http://localhost:5000/generate-video"
                response = requests.post(backend_url, json={"prompt": prompt})

                # Check for errors
                if response.status_code == 200:
                    # Save the received video
                    with open("generated_video.mp4", "wb") as f:
                        f.write(response.content)

                # Display the video
                    st.success("Video generated successfully!")
                    st.video("generated_video.mp4")
                else:
                    st.error(f"Error from backend: {response.json().get('error')}")
            except Exception as e:
                st.error(f"An error occurred: {e}")


# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.selectbox("Choose a page", ["Home", "Ask a Question","Text to Speech","Text to Image","Text to Video"])

# Render selected page
if selection == "Home":
    home_page()
elif selection == "Ask a Question":
    text_generation_page()
elif selection == "Text to Speech":
    tts()
elif selection == "Text to Image":
    tti()
elif selection == "Text to Video": 
    ttv()