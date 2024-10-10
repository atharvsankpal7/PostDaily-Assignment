# summarizer.py

import google.generativeai as genai
from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")


def summarize_and_get_precautions(text):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    prompt = f"""
    Summarize the following news in 4 sentences and provide 3 precautionary steps based on the summary:

    {text}

    Format:
    Summary:
    1. 
    2. 
    3. 
    4. 

    Precautionary Steps:
    1. 
    2. 
    3. 
    """

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)

    return response.text
