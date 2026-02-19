import streamlit as st
import requests
import json
from pathlib import Path

# Configuration
API_KEY_FILE = "api_key.txt"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "stepfun/step-3.5-flash:free"

def load_api_key():
    """Load the OpenRouter API key from api_key.txt file."""
    try:
        key_path = Path(API_KEY_FILE)
        if not key_path.exists():
            return None
        with open(key_path, 'r') as f:
            api_key = f.read().strip()
            return api_key if api_key else None
    except Exception as e:
        st.error(f"Error reading API key file: {str(e)}")
        return None

def summarize_text(text, api_key, word_limit=100):
    """
    Summarize the provided text using OpenRouter API with stepfun/step-3.5-flash:free model.
    
    Args:
        text (str): The text to summarize
        api_key (str): OpenRouter API key
        word_limit (int): Maximum number of words for the summary (default: 100)
        
    Returns:
        str: Summarized text or error message
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "Text Summarizer"
    }
    
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": f"You are a helpful assistant that creates concise and accurate summaries of text. Provide clear, well-structured summaries that capture the main points. Keep your summary to approximately {word_limit} words."
            },
            {
                "role": "user",
                "content": f"Please summarize the following text in approximately {word_limit} words:\n\n{text}"
            }
        ]
    }
    
    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            summary = result['choices'][0]['message']['content']
            return summary
        else:
            return "Error: Unexpected response format from API"
            
    except requests.exceptions.RequestException as e:
        return f"Error making API request: {str(e)}"
    except json.JSONDecodeError:
        return "Error: Could not parse API response"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def main():
    """Main application function."""
    # Page configuration
    st.set_page_config(
        page_title="AI Text Summarizer",
        page_icon="📝",
        layout="wide"
    )
    
    # Application header
    st.title("📝 AI Text Summarizer")
    st.markdown("Summarize your text using AI powered by OpenRouter")
    
    # Check for API key
    api_key = load_api_key()
    
    if not api_key:
        st.error("⚠️ API key not found!")
        st.info(f"Please create a file named `{API_KEY_FILE}` in the project root directory and paste your OpenRouter API key into it.")
        st.markdown("""
        ### How to get an API key:
        1. Go to [OpenRouter](https://openrouter.ai/)
        2. Sign up or log in
        3. Navigate to the API Keys section
        4. Create a new API key
        5. Copy the key and paste it into `api_key.txt`
        """)
        return
    
    # Sidebar with information
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown(f"""
        This application uses the **{MODEL}** model to summarize text.
        
        **Features:**
        - Fast and free summarization
        - Simple and intuitive interface
        - Powered by OpenRouter API
        """)
        
        st.header("📚 Instructions")
        st.markdown("""
        1. Enter or paste your text in the text area
        2. Adjust the summary length using the slider (30-150 words)
        3. Click the "Summarize" button
        4. Get your AI-generated summary
        """)
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Input Text")
        user_text = st.text_area(
            "Enter the text you want to summarize:",
            height=350,
            placeholder="Paste or type your text here..."
        )
        
        word_limit = st.slider(
            "Summary length (words):",
            min_value=30,
            max_value=150,
            value=100,
            step=10,
            help="Adjust the approximate length of the summary"
        )
        
        summarize_button = st.button("✨ Summarize", type="primary", use_container_width=True)
    
    with col2:
        st.subheader("Summary")
        summary_placeholder = st.empty()
        
        if summarize_button:
            if not user_text or not user_text.strip():
                summary_placeholder.warning("⚠️ Please enter some text to summarize.")
            else:
                with st.spinner("Generating summary..."):
                    summary = summarize_text(user_text, api_key, word_limit)
                    summary_placeholder.markdown(summary)
        else:
            summary_placeholder.info("👈 Enter text and click 'Summarize' to see the result here.")
    
    # Footer
    st.divider()
    st.markdown(
        "<div style='text-align: center; color: gray;'>Built with Streamlit and OpenRouter API</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
