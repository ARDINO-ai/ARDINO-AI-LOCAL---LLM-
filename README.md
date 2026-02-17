# 🤖 ARDINO AI (Qwen Model)

ARDINO AI is a simple AI Chatbot built using:

- Streamlit (Frontend UI)
- Hugging Face Transformers
- Qwen2.5-Coder-1.5B Model
- PyTorch

It can:
- Answer questions
- Generate Arduino code
- Explain programming concepts
- Act as a coding assistant

---

## 🚀 Demo Preview

Chat interface built with Streamlit  
Clean UI + Adjustable settings

---

## 🧠 Model Used

Qwen/Qwen2.5-Coder-1.5B from Hugging Face

---

## 📂 Project Structure

project-folder/
│
├── app.py
├── model.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME

2️⃣ Create Virtual Environment (Recommended)
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run The App
streamlit run app.py


App will open at:

http://localhost:8501

🎛 Features

Adjustable Max Tokens

Adjustable Temperature

Cached Model Loading

Clean UI Design

💻 Requirements

Python 3.9+

8GB+ RAM recommended

GPU optional (for faster response)

📌 Notes

First run will download model (~3GB)

CPU mode may be slow

GPU recommended for better performance

👨‍💻 Author

Made with ❤️ by RAJAT KAPOOR