# Chat Application with PDF Integration

This Streamlit application allows users to chat with a bot that can extract and understand content from uploaded PDF files. The bot can answer questions based on the PDF content and maintain a history of the conversation, which can be downloaded as a PDF.

## Features

1. **PDF Upload**: Users can upload a PDF file and extract text content from it.
2. **Interactive Chat**: Ask questions based on the content of the uploaded PDF and receive responses from a Generative AI model.
3. **Chat History**: Maintain and display a history of the conversation.
4. **Download Chat History**: Download the chat history as a PDF file.

## Requirements

- Python 3.7+
- Streamlit
- PyPDF2
- google.generativeai (Generative AI Model)

## Installation

1. Clone the repository or download the code.
2. Install the required packages using pip:
    ```bash
    pip install streamlit PyPDF2 google-generativeai
    ```

## Configuration

1. Set your Google API key as an environment variable:
    ```bash
    export GOOGLE_API_KEY='YOUR_GOOGLE_API_KEY'
    ```
    Or set it directly in the code:
    ```python
    os.environ["GOOGLE_API_KEY"] = 'YOUR_GOOGLE_API_KEY'
    ```

## Usage

1. Navigate to the directory containing the code.
2. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
3. Open the provided URL in a web browser.
4. Use the sidebar to select the desired option (Home, Chat with PDF, or Chat Bot).

### Home Page

The home page provides a welcome message and instructions to select an option from the sidebar.

### Chat with PDF

1. Upload a PDF file using the "Upload PDF file" button.
2. Enter a question based on the PDF content.
3. View the bot's response and the conversation history.
4. Download the chat history as a PDF file if needed.

### Chat Bot

1. The chat bot will load a default PDF file (path specified in the code).
2. Enter a question based on the PDF content.
3. View the bot's response and the conversation history.

## Code Overview

### Functions

- **extract_text_from_pdf(file)**: Extracts text content from an uploaded PDF file.
- **generate_response(pdf_text, user_input)**: Generates a response from the Generative AI model based on the PDF text and user input.
- **download_pdf(history)**: Converts the chat history into a downloadable PDF format.
- **chat_with_pdf()**: Manages the "Chat with PDF" functionality.
- **chat_bot(pdf_path)**: Manages the "Chat Bot" functionality with a default PDF file.
- **home_page()**: Displays the home page with a welcome message.
- **main()**: The main function that ties all components together and runs the Streamlit application.

### CSS Styling

Custom CSS is used to style the chat messages and the layout of the application. The styles include formatting for user and bot messages, avatars, and the overall chat history display.

## Example

1. Start the application:
    ```bash
    streamlit run app.py
    ```
2. Use the sidebar to navigate to "Chat with PDF" or "Chat Bot".
3. Upload a PDF file (if using "Chat with PDF") or use the default PDF file (if using "Chat Bot").
4. Enter questions and interact with the bot.
5. View and download the chat history.

