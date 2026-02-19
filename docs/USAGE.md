# Usage Guide

## Running the Application

### Step 1: Install Dependencies

First, ensure you have Python installed on your system. Then install the required packages:

```bash
pip install streamlit requests
```

### Step 2: Configure API Key

Create a file named `api_key.txt` in the project root directory and add your OpenRouter API key:

```
sk-or-v1-your-actual-api-key-here
```

### Step 3: Start the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`.

## Using the Interface

### Main Components

1. **Input Text Area (Left Column)**
   - Enter or paste the text you want to summarize
   - Supports text of various lengths
   - Clear and simple interface

2. **Summary Output (Right Column)**
   - Displays the AI-generated summary
   - Shows loading spinner during processing
   - Presents summary in markdown format

3. **Sidebar**
   - Provides information about the application
   - Shows instructions for use
   - Displays model information

### Step-by-Step Process

1. **Enter Your Text**
   - Click in the text area on the left
   - Type or paste the text you want to summarize
   - You can summarize articles, documents, emails, or any text content

2. **Generate Summary**
   - Click the "✨ Summarize" button
   - Wait for the AI to process your text (usually takes a few seconds)
   - The summary will appear on the right side

3. **Review and Use**
   - Read the generated summary
   - Copy it for use in other applications
   - Enter new text to create another summary

## Examples

### Example 1: Summarizing an Article

**Input:**
```
Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to 
natural intelligence displayed by animals including humans. Leading AI textbooks define 
the field as the study of "intelligent agents": any system that perceives its environment 
and takes actions that maximize its chance of achieving its goals. Some popular accounts 
use the term "artificial intelligence" to describe machines that mimic "cognitive" 
functions that humans associate with the human mind, such as "learning" and "problem solving".
```

**Output:**
```
Artificial intelligence (AI) refers to intelligence exhibited by machines, contrasting 
with natural intelligence in animals and humans. It involves the study of intelligent 
agents that interact with their environment to maximize goal achievement. AI systems are 
designed to replicate cognitive functions like learning and problem-solving.
```

### Example 2: Summarizing Meeting Notes

**Input:**
```
Today's meeting covered project progress, budget allocation, and timeline adjustments. 
The team reported 75% completion on Phase 1. Budget review showed $5,000 remaining for 
Q1 activities. Timeline was extended by two weeks to accommodate additional testing. 
Next meeting scheduled for March 1st.
```

**Output:**
```
Meeting highlights: Project 75% complete for Phase 1, $5,000 budget remaining in Q1, 
timeline extended two weeks for testing, next meeting on March 1st.
```

## Tips for Best Results

1. **Text Length**
   - The model works well with text of various lengths
   - Very short texts might not need summarization
   - Very long texts (multiple pages) work but may take longer

2. **Clear Input**
   - Ensure your text is readable and properly formatted
   - Remove unnecessary formatting or special characters
   - Use proper punctuation for better results

3. **Multiple Summaries**
   - You can generate multiple summaries from the same text
   - Each summary might vary slightly
   - Try different runs if you want alternative phrasings

## Error Messages

### "API key not found!"
**Solution**: Create the `api_key.txt` file with your valid OpenRouter API key.

### "Please enter some text to summarize"
**Solution**: Enter text in the input area before clicking the Summarize button.

### "Error making API request"
**Solution**: Check your internet connection and verify your API key is valid.

## Advanced Usage

### Custom Model Parameters

The application is configured with default parameters, but you can modify the `app.py` file to adjust:

- Model temperature (for more creative or conservative summaries)
- Maximum tokens (for longer or shorter summaries)
- System prompt (to change summarization style)

### Integration with Other Tools

You can integrate this summarization tool with:
- Document processing pipelines
- Content management systems
- Note-taking applications
- Research workflows

## Performance Notes

- **Response Time**: Typically 2-5 seconds per summary
- **Rate Limits**: Depends on your OpenRouter account tier
- **Text Length**: Longer texts take more time to process
- **Concurrent Users**: Single instance supports multiple simultaneous users

## Keyboard Shortcuts

When using Streamlit:
- `Ctrl + R` or `R`: Rerun the application
- `Ctrl + C` (in terminal): Stop the server
- `Ctrl + Shift + C`: Open command menu

## Frequently Asked Questions

**Q: Can I use this offline?**
A: No, the application requires an internet connection to access the OpenRouter API.

**Q: Is my data stored anywhere?**
A: The application doesn't store your text. Check OpenRouter's privacy policy for their data handling.

**Q: Can I change the AI model?**
A: Yes, modify the `MODEL` variable in `app.py` to use a different OpenRouter model.

**Q: How much does it cost?**
A: The `stepfun/step-3.5-flash:free` model is free to use, but rate limits may apply.

**Q: Can I deploy this online?**
A: Yes! You can deploy to Streamlit Cloud, Heroku, or other platforms that support Python.
