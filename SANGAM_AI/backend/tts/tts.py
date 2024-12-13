from flask import Flask, request, jsonify, send_file
from bark import generate_audio, preload_models, SAMPLE_RATE
import soundfile as sf
import io

# Initialize Flask app
app = Flask(__name__)

# Preload Bark models
preload_models()

# Define available voices
available_voices = {
    "v2/en_speaker_0": "[en_speaker_0]",
    "v2/en_speaker_1": "[en_speaker_1]",
    "v2/en_speaker_2": "[en_speaker_2]",
    "v2/en_speaker_3": "[en_speaker_3]",
    "v2/en_speaker_4": "[en_speaker_4]"
}

@app.route("/generate-audio", methods=["POST"])
def generate_audio_endpoint():
    data = request.get_json()
    text_prompt = data.get("text")
    speaker = data.get("speaker", "v2/en_speaker_0")  # Default to "v2/en_speaker_0"

    if not text_prompt:
        return jsonify({"error": "No text provided"}), 400
    if speaker not in available_voices:
        return jsonify({"error": "Invalid speaker"}), 400

    # Embed speaker preset in text prompt
    formatted_text_prompt = f" {text_prompt}"

    # Generate audio with Bark
    audio_array = generate_audio(formatted_text_prompt)

    # Save audio to a buffer as a WAV file
    buf = io.BytesIO()
    sf.write(buf, audio_array, SAMPLE_RATE, format="WAV")
    buf.seek(0)

    # Send the audio as a file response
    return send_file(buf, mimetype="audio/wav", as_attachment=True, download_name="output.wav")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
