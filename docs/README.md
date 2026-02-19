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

   **For local development:**
   - Create a `.streamlit/secrets.toml` file in the project root
   - Add your API key:
   ```toml
   OPENROUTER_KEY = "your-openrouter-api-key-here"
   ```
   
   **For Streamlit Cloud deployment:**
   - Deploy your app to Streamlit Cloud
   - Go to your app settings
   - Navigate to the Secrets section
   - Add:
   ```toml
   OPENROUTER_KEY = "your-openrouter-api-key-here"
   ```

## Getting an OpenRouter API Key

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up for a free account or log in
3. Navigate to the API Keys section in your dashboard
4. Create a new API key
5. Copy the key and add it to your secrets configuration (see Installation above)

## Usage

### Running Locally

1. Ensure you've set up `.streamlit/secrets.toml` with your API key

2. Start the application:
```bash
streamlit run app.py
# or
python -m streamlit run app.py
```

3. Open your web browser (it should open automatically) and navigate to `http://localhost:8501`

4. Enter or paste the text you want to summarize in the input area

5. Adjust the summary length using the slider (30-150 words)

6. Click the "Summarize" button

7. View your AI-generated summary in the output area

### Deploying to Streamlit Cloud

1. Push your code to a GitHub repository
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your repository and branch
5. Set the main file path to `app.py`
6. In the Advanced settings, add your secret:
   ```toml
   OPENROUTER_KEY = "your-api-key-here"
   ```
7. Click "Deploy"

## Project Structure

```
ai-integracija-pvz/
├── app.py              # Main application file
├── .streamlit/
│   └── secrets.toml    # API key configuration (not committed to git)
├── docs/               # Documentation folder
│   ├── README.md       # This file
│   └── USAGE.md        # Detailed usage guide
├── .gitignore          # Git ignore file
├── requirements.txt    # Python dependencies
└── program_requirements.txt
```

## Configuration

The application uses the following configuration:

- **Model**: `stepfun/step-3.5-flash:free`
- **API Endpoint**: `https://openrouter.ai/api/v1/chat/completions`
- **API Key Location**: Streamlit Secrets (`st.secrets["OPENROUTER_KEY"]`)
- **Summary Length**: Adjustable via slider (30-150 words)

## Security Notes

- The `.streamlit/secrets.toml` file is included in `.gitignore` to prevent accidental commits
- Never share your API key publicly or commit it to version control
- Streamlit Cloud manages secrets securely in their infrastructure
- API keys are never exposed in the application UI

## Troubleshooting

### API Key Not Found
If you see an error about the API key not being configured:

**Local Development:**
1. Ensure `.streamlit/secrets.toml` exists in the project root
2. Verify the file contains: `OPENROUTER_KEY = "your-key-here"`
3. Restart the Streamlit app after creating/modifying secrets

**Streamlit Cloud:**
1. Go to your app settings on Streamlit Cloud
2. Click on the Secrets section
3. Add your API key in TOML format
4. Save and reboot the app

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
