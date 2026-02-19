# AI Text Summarizer

A Streamlit web application that uses AI to summarize text using OpenRouter's API.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API key:**
   - Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`
   - Add your OpenRouter API key

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```
   or
   ```bash
   python -m streamlit run app.py
   ```

## Features

- ✨ AI-powered text summarization using stepfun/step-3.5-flash:free model
- 📏 Adjustable summary length (30-150 words)
- 🎨 Clean and intuitive interface
- 🚀 Ready for Streamlit Cloud deployment
- 🔒 Secure API key management with Streamlit secrets

## Documentation

- [Full Documentation](docs/README.md)
- [Usage Guide](docs/USAGE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## Get an OpenRouter API Key

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up or log in
3. Create a new API key
4. Add it to `.streamlit/secrets.toml`

## Deploy to Streamlit Cloud

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed instructions on deploying to Streamlit Cloud.

## License

This project is provided as-is for educational and personal use.
