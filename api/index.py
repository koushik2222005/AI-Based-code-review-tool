from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "AI Code Review Backend Running"
    })

@app.route("/review", methods=["POST"])
def review():
    data = request.get_json()

    code = data.get("code", "")
    language = data.get("language", "")

    review_markdown = f"""
## AI Review Result

### Language
{language}

### Code Analysis
Your code was received successfully.

### Submitted Code
```{language}
{code}
```
"""
    return jsonify({"review": review_markdown})
