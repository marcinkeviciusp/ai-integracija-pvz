# AI Text Summarizer

A simple web application that uses AI to summarize text using the OpenRouter API.

## Overview

This application provides a user-friendly interface for summarizing text using the `stepfun/step-3.5-flash:free` model via OpenRouter. The application is built with Streamlit and contained in a single Python file for simplicity.

## Features

- **Simple Interface**: Clean and intuitive web interface powered by Streamlit
- **Fast Summarization**: Uses the stepfun/step-3.5-flash:free model for quick results
- **Free to Use**: Utilizes a free model tier from OpenRouter
- **Single File**: Entire application contained in one Python file for easy deployment

## Requirements

- Python 3.7 or higher
- streamlit
- requests

## Installation

1. Clone or download this project

2. Install the required dependencies:
```bash
pip install streamlit requests
```

3. Set up your OpenRouter API key:
   - Create a file named `api_key.txt` in the project root
   - Paste your OpenRouter API key into this file
   - Save the file

## Getting an OpenRouter API Key

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up for a free account or log in
3. Navigate to the API Keys section in your dashboard
4. Create a new API key
5. Copy the key and paste it into `api_key.txt`

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser (it should open automatically) and navigate to `http://localhost:8501`

3. Enter or paste the text you want to summarize in the input area

4. Click the "Summarize" button

5. View your AI-generated summary in the output area

## Project Structure

```
ai-integracija-pvz/
├── app.py              # Main application file
├── api_key.txt         # OpenRouter API key (not committed to git)
├── docs/               # Documentation folder
│   ├── README.md       # This file
│   └── USAGE.md        # Detailed usage guide
├── .gitignore          # Git ignore file
└── program_requirements.txt
```

## Configuration

The application uses the following configuration:

- **Model**: `stepfun/step-3.5-flash:free`
- **API Endpoint**: `https://openrouter.ai/api/v1/chat/completions`
- **API Key Location**: `api_key.txt`

## Security Notes

- The `api_key.txt` file is included in `.gitignore` to prevent accidental commits
- Never share your API key publicly
- Keep your API key file secure and backed up separately

## Troubleshooting

### API Key Not Found
If you see an error about the API key not being found:
1. Ensure `api_key.txt` exists in the project root directory
2. Verify the file contains your API key with no extra spaces or newlines
3. Check file permissions to ensure the application can read it

### API Request Errors
If you encounter API request errors:
1. Verify your API key is valid and active
2. Check your internet connection
3. Ensure OpenRouter service is operational
4. Verify you haven't exceeded any rate limits

### Installation Issues
If you have trouble installing dependencies:
```bash
# Try installing in a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
pip install streamlit requests
```

## Support

For issues related to:
- **OpenRouter API**: Visit [OpenRouter Documentation](https://openrouter.ai/docs)
- **Streamlit**: Visit [Streamlit Documentation](https://docs.streamlit.io/)

## License

This project is provided as-is for educational and personal use.
