# flask_backend.py
from flask import Flask, request, jsonify, send_file
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Load model and scheduler once when the API starts
model_id = "stabilityai/stable-diffusion-2"
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, scheduler=scheduler, torch_dtype=torch.float16
)
pipe = pipe.to("cuda")

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # Generate image
    image = pipe(prompt).images[0]
    buf = BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
