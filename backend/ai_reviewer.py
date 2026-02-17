import os
from huggingface_hub import InferenceClient

# Configuration
# Choose a model that supports Chat Completion
MODEL_ID = "Qwen/Qwen2.5-Coder-7B-Instruct"

# Get HF token from environment variable
HF_TOKEN = os.getenv("HF_TOKEN")

# Initialize the client (it uses router.huggingface.co internally)
client = InferenceClient(api_key=HF_TOKEN)

def get_code_review(code_input, language):
    """
    Sends code to Hugging Face via the new Router API structure.
    """
    try:
        # Use chat completion for structured coding tasks
        messages = [
            {
                "role": "system",
                "content": "You are an expert code reviewer. Analyze the following code for bugs and provide a refactored version."
            },
            {
                "role": "user",
                "content": f"Language: {language}\nCode:\n{code_input}"
            }
        ]

        # The client handles the new 'router.huggingface.co' endpoint automatically
        completion = client.chat.completions.create(
            model=MODEL_ID,
            messages=messages,
            max_tokens=2048
        )

        return completion.choices[0].message.content

    except Exception as e:
        # Handle loading states (503) or quota issues
        error_msg = str(e)
        if "503" in error_msg:
            return "### ⏳ Model Loading\nThe model is currently starting up on Hugging Face. Please try again in 1 minute."
        return f"### ❌ API Error\n{error_msg}"