# 🐍 Online Code Editor - Flask Backend

This is the Flask backend for the Online Code Editor project. It connects to the Piston API to execute code in multiple programming languages and serves as the API layer for the React frontend.

## 🚀 Features

- Execute Python, JavaScript, and C++ code
- CORS-enabled for frontend integration
- Hosted on Render 

## 📁 Project Structure

```
.
├── app.py
├── requirements.txt
└── README.md
```

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/abaiml/CodeEditor-Flask-Backend.git
cd online-editor-backend
```

### 2. Create a Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Locally

```bash
python app.py
```

Server runs on: `http://127.0.0.1:5000`

### 4. Deployment (Render)

- Create a new web service on [https://render.com](https://render.com)
- Set `app.py` as the entry point
- Add CORS for your frontend domain:
  ```python
  CORS(app, origins=["https://your-frontend.netlify.app"])
  ```

## 🧪 Example API Request

```http
POST /run
Content-Type: application/json

{
  "language": "python",
  "code": "print('Hello World')"
}
```

## 📄 License

MIT License
