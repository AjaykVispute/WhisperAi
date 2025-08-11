# Whisper AI Model Tester

A **Streamlit app** to benchmark OpenAI Whisper models (`tiny`, `base`, `small`, `medium`, `large`) by transcribing a 20-second audio clip and comparing **speed** and **accuracy**.

---

## Features

* Upload `.mp3`, `.wav`, or `.m4a` files
* Extract first 20 seconds for testing
* Transcribe with multiple Whisper models
* Show transcription + time taken
* Recommend the fastest model

---

## Installation

```bash
git clone https://github.com/yourusername/whisper-model-tester.git
cd whisper-model-tester
pip install -r requirements.txt
```

**requirements.txt**

```
streamlit
openai-whisper
pydub
jiwer
```

Install **FFmpeg**:

```bash
sudo apt install ffmpeg
```

---

## Usage

```bash
streamlit run app.py
```

1. Upload an audio file
2. View transcriptions for each model
3. See speed comparisons and recommendation

---

## Tech Stack

* **Streamlit** – Web UI
* **Whisper** – Speech-to-text
* **Pydub** – Audio processing
* **Jiwer** – WER calculation (optional)




