from flask import Flask, request, jsonify, send_file
import torch
from diffusers import DiffusionPipeline
from diffusers.utils import export_to_video
import os

app = Flask(__name__)

# Initialize the model pipeline globally
pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_576w", torch_dtype=torch.float16)
pipe.enable_model_cpu_offload()
pipe.unet.enable_forward_chunking(chunk_size=1, dim=1)
pipe.enable_vae_slicing()

@app.route("/generate-video", methods=["POST"])
def generate_video():
    try:
        # Get the prompt from the request
        data = request.json
        prompt = data.get("prompt", "A default prompt")
        
        # Generate video frames
        video_frames = pipe(prompt, num_frames=24).frames[0]

        # Save video
        video_path = "generated_video.mp4"
        export_to_video(video_frames, video_path)

        # Send the video file to the client
        return send_file(video_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
