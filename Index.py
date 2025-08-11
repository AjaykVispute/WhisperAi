import streamlit as st
import whisper
import time
from pydub import AudioSegment
import os
from jiwer import wer

# Function to extract 20 seconds of audio
def extract_clip(file_path, start_time=0, duration=20):
    audio = AudioSegment.from_file(file_path)
    clip = audio[start_time * 1000 : (start_time + duration) * 1000]
    clip_path = "temp_clip.wav"
    clip.export(clip_path, format="wav")
    return clip_path

# Function to transcribe audio and measure time
def transcribe_audio(model_name, audio_path):
    model = whisper.load_model(model_name)
    start_time = time.time()
    result = model.transcribe(audio_path)
    end_time = time.time()
    return result["text"], end_time - start_time

# Main Streamlit app
def main():
    st.title("Whisper AI Model Tester with WER")
    st.write("Upload a large audio file to test Whisper AI models for transcription.")

    # File upload
    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file:
        st.audio(uploaded_file, format="audio/wav")
        file_extension = uploaded_file.name.split(".")[-1]
        file_path = f"uploaded_audio.{file_extension}"
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.write("Extracting 20-second audio clip...")
        clip_path = extract_clip(file_path)
        st.audio(clip_path, format="audio/wav")
        
        st.write("Testing models...")
    
        models = ["tiny", "base", "small", "medium", "large"]
        results = []
        
        for model_name in models:
            with st.spinner(f"Testing {model_name} model..."):
                text, time_taken = transcribe_audio(model_name, clip_path)
                st.success(f"**Model:** {model_name} | **Time Taken:** {time_taken:.2f}s")
                st.text_area(f"Transcription for {model_name}:", value=text, height=200)

                # Assume no reference transcription, so calculate WER as None
                error_rate = None
                results.append((model_name, time_taken, text, error_rate))
        
        # Suggesting the fastest and most accurate model (based on time and transcription)
        if results:
            best_model = min(results, key=lambda x: x[1])  # Select the fastest model
            st.markdown("### **Recommendation:**")
            st.write(f"The fastest model is **`{best_model[0]}`**, taking **{best_model[1]:.2f} seconds** for transcription.")
        
        # Clean up temporary files
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(clip_path):
            os.remove(clip_path)

if __name__ == "__main__":
    main()
