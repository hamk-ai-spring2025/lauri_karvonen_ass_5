# Assignment 5: Image-to-Text and Text-to-Image with OpenAI API

This project demonstrates the use of OpenAI's Vision API and DALL-E 3 to process images and generate new ones. The workflow involves:
1. Converting an image to text using OpenAI's Vision API.
2. Using the generated text description to create a new image with DALL-E 3.

---

## Features

- **Image-to-Text Conversion**: Extracts a textual description of an image using OpenAI's Vision API.
- **Text-to-Image Generation**: Generates a new image based on the textual description using DALL-E 3.
- **Error Handling**: Handles API errors and invalid responses gracefully.
- **Environment Variable Support**: Uses a `.env` file to securely store the OpenAI API key.

---

## Prerequisites

1. Python 3.7 or higher
2. Required Python libraries:
   - `requests`
   - `python-dotenv`
   - `openai`
   - `Pillow`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Lauri221/assignment-5.git
   cd assignment-5
   ```

2. install dependencies
   ```bash
   pip install pillow openai python-dotenv requests
   ```

---

## Environment Variables

Create a `.env` file in the root directory of the project and add the following line:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage
Place the input image in the project directory (e.g., pikatchu_0.png).
Run the script:
```bash
python ass_5.py
```
## The script will:
- Generate a textual description of the input image.
- Use the description to create a new image.
- Save the generated image in the project directory.

## Project Structure

```plaintext
assignment-5/
├── ass_5.py          # Main script for image-to-text and text-to-image processing
├── file_util.py      # Utility functions for file handling
├── .env              # Environment variables (not included in the repository)
├── README.md         # Project documentation
├── requirements.txt  # Python dependencies
└── pikatchu_0.png    # Example input image
```

## Example Workflow
Input Image: pikatchu_0.png (replace with your own image and file name.)
Run in console: ```bash
python ass_5.py
```
- The script will process the input image by:
    - Converting the image to a textual description using OpenAI's Vision API.
    - Utilizing the description to generate a new image with DALL-E 3.
    - Saving the resulting image as dall_generated.png in the project directory.

## Troubleshooting
**API Key Error:** Ensure your .env file contains the correct API key.
**Invalid Response:** Check the API response by uncommenting the debug lines in ass_5.py.

## License
This project is licensed under the MIT License. See the LICENSE file for details.