import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader

# Set your API key as an environment variable
os.environ["GOOGLE_API_KEY"] = 'PUT your gemini api key here '

# Configure the API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

# CSS styling
css = '''
<style>
.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
}
.chat-message.user {
    background-color: #2b313e;
}
.chat-message.bot {
    background-color: #475063;
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
.bold-heading {
    font-weight: bold;
    font-size: 24px;
    margin-bottom: 20px;
}
.torchlight-sticker {
    width: 24px;
    height: 24px;
    margin-left: 10px;
}
.history {
    margin-top: 20px;
    padding: 10px;
    background-color: #f0f0f0;
    border-radius: 5px;
}
</style>
'''

# HTML template
message_template = '''
<div class="chat-message {}">
    <div class="avatar">
        <img src="{}" style="max-width: 50px; max-height: 50px;">
    </div>
    <div class="message">{}</div>
</div>
'''

def extract_text_from_pdf(file):
    try:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return ""

def generate_response(pdf_text, user_input):
    input_text = pdf_text + user_input
    response = model.generate_content(input_text)
    return message_template.format("bot",
                                  "https://tse2.mm.bing.net/th?id=OIP.C5v0eJ_tW4UiG9zYK6OWcAHaHa&pid=Api&P=0&h=180",
                                  response.text)

def download_pdf(history):
    content = ""
    for question, answer in history:
        content += f"User: {question}\nBot: {answer}\n\n"
    return content.encode('utf-8')

def chat_with_pdf():
    st.title("Chat with PDF")
    pdf_file = st.file_uploader("Upload PDF file", type=["pdf"])
    if pdf_file is not None:
        text_from_pdf = extract_text_from_pdf(pdf_file)
        if 'history' not in st.session_state:
            st.session_state.history = []
        user_input = st.text_input("Ask a question:")
        if user_input:
            bot_response = generate_response(text_from_pdf, user_input)
            st.session_state.history.append((user_input, bot_response))
            st.markdown("<div class='history'>", unsafe_allow_html=True)
            for question, answer in reversed(st.session_state.history):
                st.markdown(message_template.format("user",
                                                    "https://png.pngtree.com/png-vector/20190710/ourlarge/pngtree-user-vector-avatar-png-image_1541962.jpg",
                                                    question), unsafe_allow_html=True)
                st.markdown(answer, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            download_content = download_pdf(st.session_state.history)
            st.download_button(label="Download Chat History", data=download_content, file_name="chat_history.pdf", mime="application/pdf")

def chat_bot(pdf_path):
    st.title("Chat Bot")
    if pdf_path:
        text_from_pdf = extract_text_from_pdf(pdf_path)
        if 'history' not in st.session_state:
            st.session_state.history = []
        user_input = st.text_input("Ask a question:")
        if user_input:
            bot_response = generate_response(text_from_pdf, user_input)
            st.session_state.history.append((user_input, bot_response))
            st.markdown("<div class='history'>", unsafe_allow_html=True)
            for question, answer in reversed(st.session_state.history):
                st.markdown(message_template.format("user",
                                                    "https://png.pngtree.com/png-vector/20190710/ourlarge/pngtree-user-vector-avatar-png-image_1541962.jpg",
                                                    question), unsafe_allow_html=True)
                st.markdown(answer, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

def home_page():
    st.title("Welcome to the Chat Application")
    st.write("Please select an option from the sidebar to continue.")

def main():
    st.sidebar.title("Choose Option")
    option = st.sidebar.radio("Select an option:", ("Home", "Chat with PDF", "Chat Bot"))
    if option == "Home":
        home_page()
    elif option == "Chat with PDF":
        chat_with_pdf()
    elif option == "Chat Bot":
        pdf_path = "C:\\Users\\user\\OneDrive\\Desktop\\praniprojectzip\\praniproject\\datamain.pdf"
        if pdf_path:
            chat_bot(pdf_path)

if __name__ == "__main__":
    main()
