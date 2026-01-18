from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel, Part

# Configuration 

PROJECT_ID = "neat-shell-483606-d3"
LOCATION = "us-central1"
MODEL_NAME = "gemini-2.5-flash"

# Initialize Vertex AI

aiplatform.init(
    project=PROJECT_ID,
    location=LOCATION
)

model = GenerativeModel(MODEL_NAME)


# Gemini prompt

BASE_PROMPT = """
You are a study assistant.

Given the input, return:
1. A concise summary
2. 3-5 key definitions
3. 3 self-test quiz questions

Respond STRICTLY in this JSON format:

{
  "summary": "...",
  "definitions": ["...", "..."],
  "quiz": ["...", "..."]
}
"""


# Text processing

def process_text(text: str) -> dict:
   response = model.generate_content(
    BASE_PROMPT + "\n\nTEXT INPUT:\n" + text,
    generation_config={
        "response_mime_type": "application/json"
    }
    )
   return _parse_response(response.text)


# Image processing

def process_image(image_bytes: bytes) -> dict:
    image_part = Part.from_data(
        data=image_bytes,
        mime_type="image/jpeg" 
    )

    response = model.generate_content(
    [
        BASE_PROMPT + "\n\nThe image contains study material.",
        image_part
    ],
    generation_config={
        "response_mime_type": "application/json"
    }
)


    return _parse_response(response.text)


# Response parsing

def _parse_response(text: str) -> dict:
    """
    Converts Gemini's JSON string into a Python dictionary.
    """
    import json

    try:
        return json.loads(text)
    except json.JSONDecodeError:

        return {
            "summary": text,
            "definitions": [],
            "quiz": []
        }
