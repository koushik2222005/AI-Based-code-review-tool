# AI-Powered Automated Code Reviewer
An intelligent, full-stack web application designed to automate the code review process. By leveraging State-of-the-Art (SOTA) Large Language Models, this tool identifies logical bugs, security vulnerabilities, 
and provides optimized refactoring suggestions in real-time.

# Key Features
Intelligent Analysis: Uses specialized "Coder" LLMs to perform deep logic audits.

Multi-Language Support: Handles Python, JavaScript, Java, C++, and more.

Chain-of-Thought (CoT) Prompting: Ensures the AI explains the "why" behind every suggestion.

Modern UI: Features a professional code editor interface powered by CodeMirror.

Low Latency: Optimized backend with the Hugging Face Router API for fast inference.

# Technical Architecture
This project follows a decoupled Client-Server Architecture:

Frontend: Single Page Application (SPA) using HTML5, CSS3, and Vanilla JavaScript.

Backend: RESTful API built with Flask (Python).

Intelligence: Integrated Qwen2.5-Coder-7B and Gemini 1.5 Flash via the Hugging Face Router API.

Security: Implemented CORS middleware and Environment Variable management for API safety.

#  Tech StackLayerTechnology
Frontend: HTML5, CSS3, JavaScript, CodeMirror
Backend: Python, Flask, Flask-CORS
AI/ML: Hugging Face InferenceClient, Qwen2.5-Coder, Gemini 1.5 Flash
DevOps: Dotenv (Secret Management), Pip

# Installation & Setup
# Clone the repository:
Bash
git clone https://github.com/yourusername/ai-code-reviewer.git
cd ai-code-reviewer

# Set up a Virtual Environment:
Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Dependencies:
Bash
pip install -r requirements.txt

# Environment Variables:
Create a .env file in the root directory and add your API keys:
# Code snippet
HF_TOKEN=your_hugging_face_token_here
GEMINI_API_KEY=your_gemini_key_here

# Run the Application:
Bash
# Start the Flask backend
python app.py
Open index.html in your browser to start reviewing code
