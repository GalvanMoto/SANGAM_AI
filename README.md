
# SANGAM AI

SANGAM AI is an integrated AI platform that provides tools for text-to-text, text-to-image, text-to-speech, text-to-video, and speech-to-speech functionalities. This project combines pre-trained models from Hugging Face and other sources, presenting a streamlined interface for diverse AI-powered tasks.

---

## **Features**

- **Text-to-Text**: Generate text-based responses using advanced language models.
- **Text-to-Image**: Create images from textual descriptions.
- **Text-to-Speech**: Convert text into realistic voice outputs.
- **Text-to-Video**: Generate short video content from text prompts.
- **Speech-to-Speech**: Transform voice inputs into modified voice outputs or translations.

---

## **Technologies Used**

### **Frontend**
- **Streamlit**: Web-based user interface for seamless interaction.

### **Backend**
- **Flask**: API and middleware for handling application logic.
- **Python**: Core language used for integrating AI tools.

### **Database**
- **SQLite**: Manages chat history and file storage.

### **AI Models**
- Pre-trained models from Hugging Face for text, speech, and image processing.

### **Deployment Plans**
- Future deployment on **AWS** or **Azure** with auto-scaling capabilities.

---

## **Project Structure**

- **frontend/**: Contains Streamlit UI files.
- **backend/**: Flask-based backend logic.
- **models/**: Pre-trained models for inference.
- **database/**: SQLite schema and chat history.
- **scripts/**: Utilities and helpers for handling prompts and file parsing.

---

## **Installation Guide**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sangam-ai.git
   ```

2. Navigate to the project directory:
   ```bash
   cd sangam-ai
   ```

3. Set up virtual environments for each AI tool:
   ```bash
   python -m venv venv_text
   python -m venv venv_image
   # Repeat for all tools.
   ```

4. Activate the environment and install dependencies:
   ```bash
   source venv_text/bin/activate
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   streamlit run frontend/app.py
   ```

---

## **Usage**

1. Open the app in your browser.
2. Select the desired tool from the dashboard.
3. Provide the input (text, speech, or files).
4. Get results and download or save them as required.

---

## **License**

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 Gautam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## **Contributing**

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## **Contact**

For any queries or suggestions, feel free to reach out:
- **Email**: [galvanmoto@gmail.com](mailto:galvanmoto@gmail.com.com)
- **GitHub**: [galvanmoto](https://github.com/galvanmoto)

---

## **Acknowledgments**

- **Hugging Face** for providing pre-trained AI models.
- **Streamlit** and **Flask** for creating interactive and responsive applications.
- Open-source contributors for valuable libraries and tools.
