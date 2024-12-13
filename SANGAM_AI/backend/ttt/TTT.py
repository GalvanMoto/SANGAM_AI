from flask import Flask, request, jsonify
from langchain.llms import LlamaCpp

# Initialize the Flask app
app = Flask(__name__)

# Initialize LlamaCpp model
model_path = "./mistral-7b-instruct-v0.2.Q4_K_M.gguf"

llm = LlamaCpp(
    model_path=model_path,
    verbose=True
)

# Route to generate text based on the user's prompt
@app.route('/generate-text', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data['prompt']

    # Enhanced prompt with instructions for more detailed responses
    full_prompt = f"<s>[INST] Provide a detailed, engaging, and informative answer: {prompt} [/INST]"

    # Perform inference with the enhanced prompt
    output = llm(
        full_prompt,
        max_tokens=300,  # Increase max tokens for longer responses
        stop=["</s>"]
    )

    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
