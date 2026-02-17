from flask import Flask, request, jsonify
from flask_cors import CORS 
# Removed: from dotenv import load_dotenv # No longer needed
from ai_reviewer import get_code_review
import os # Kept for potential future use, but not strictly needed for the key

# Removed: load_dotenv() # No longer needed

# --- FLASK APPLICATION SETUP ---
app = Flask(__name__)

# Configure CORS: Allow requests from the frontend origin
CORS(app) 

# --- Health Check Endpoint ---
@app.route('/health', methods=['GET'])
def health_check():
    """Simple check to ensure the server is running."""
    return jsonify({"status": "ok", "message": "AI Code Reviewer Backend is running."})

# --- Main Review Endpoint ---
@app.route('/review', methods=['POST'])
def review_code():
    """Receives code input and returns the AI-generated review."""
    
    # 1. Input Validation and Parsing
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request."}), 400
        
    data = request.get_json()
    code = data.get('code')
    language = data.get('language', 'Unknown Language')

    if not code:
        return jsonify({"error": "No code provided for review."}), 400

    print(f"-> Received {language} code for review (length: {len(code)})")
    
    # 2. Execute AI Review Logic
    # This function now uses the hardcoded key inside ai_reviewer.py
    ai_review_result = get_code_review(code, language)
    
    # 3. Return Structured Response
    return jsonify({
        "status": "success",
        "review_markdown": ai_review_result
    })

if __name__ == '__main__':
    # No environment variable check needed here since the key is hardcoded in ai_reviewer.py
    
    # Run the application on the default Flask port
    app.run(debug=True, port=5000)