import base64          # For encoding image data to base64 format
import requests        # For making HTTP requests to APIs
import os              # For accessing environment variables
from dotenv import load_dotenv  # For loading environment variables from a .env file
from openai import OpenAI  # The official OpenAI Python client
from file_util import fetch_url, save_binary_file, find_new_file_name  # Custom utility functions for file operations

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.environ.get("OPENAI_API_KEY")

# If api_key is None, it means it wasn't found in the environment variables
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables or .env file")

# Create the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Function to convert an image file to base64 encoding
# This is necessary for sending images to OpenAI's Vision API
def encode_image(image_path):
    with open(image_path, "rb") as image_file:  # Opens file in binary read mode
        return base64.b64encode(image_file.read()).decode("utf-8")  # Encodes binary data to base64 string

# Path to your image
image_path = "pikatchu_0.png"

# Getting the base64 string
base64_image = encode_image(image_path)

# HTTP headers required for API authentication and specifying content type
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

# Request payload with model specification and prompt with image
payload = {
    "model": "gpt-4o-mini",  # Using GPT-4o mini model (vision-capable model)
    "messages": [
        {
            "role": "user",  # Message is from the user
            "content": [
                {"type": "text", "text": "Please describe the contents of the image?"},  # Text prompt
                {
                    "type": "image_url",  # Including the image
                    # Embedding base64 image data directly in the URL using data URI scheme
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
    "max_tokens": 200,  # Limits response length to 200 tokens
}

print("Sending request to OpenAI Vision API...")
# POST request to the OpenAI API endpoint
response = requests.post(
    "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
)

if response.status_code != 200:
    print(f"Error: API call failed with status code {response.status_code}")
    print(response.text)  # Print the error details from the API
    exit(1)

# Debug line (commented out) that would print the full API response
#print(response.json())

data = response.json()
if not data.get("choices"):
    print("Error: 'choices' not found in the API response:")
    print(data)
    exit(1)

text_description = data["choices"][0].get("message", {}).get("content")
if not text_description:
    print("Error: No text description found in the API response.")
    exit(1)

print(text_description)  # Displays what the AI "sees" in the image

print(response.text)

print("Generating image...")

# Request to generate a new image based on the text description
response = client.images.generate(
  model="dall-e-3",  # Model selection for image generation, options include "dall-e-2" and "dall-e-3"
  prompt=text_description,  # Using the description from Vision API as the prompt
  size="1024x1024",  # #size="1792x1024" #widescreen, #size="1024x1792" #portrait,
  quality="hd",  # High definition quality (alternative: "standard")
  style="vivid",  # Vibrant, colorful style (alternative: "natural" for more photorealistic)
  n=1,  # Number of images to generate - DALL-E 3 only supports generating 1 at a time
)

# Extracting the URL of the generated image
image_url = response.data[0].url
print(image_url)  # Displays the URL where the generated image can be accessed

print("Downloading image...")
# Fetch the image data from the URL
image_data = fetch_url(image_url)  # Custom function from file_util module

# Save the image to a file if download was successful
if image_data is not None:
    # Generate a unique filename to avoid overwriting existing files
    file_name = find_new_file_name("dall.png")  # Custom function from file_util
    # Save the binary image data to the file
    if save_binary_file(data=image_data, filename=file_name):  # Custom function from file_util
      print(f"Image saved to {file_name}")  # Confirmation message with saved filename