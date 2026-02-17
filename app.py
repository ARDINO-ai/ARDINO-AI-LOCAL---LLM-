import streamlit as st
from model import load_model, generate_response

# ================= PAGE CONFIG =================
st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 ARDINO AI (Qwen Model)")

# ================= STYLE =================
st.markdown("""
<style>
.stApp { background:#f7f7f8; }
.block-container { max-width:900px; }
.chat-box {
    background:white;
    border-radius:12px;
    padding:16px;
    border:1px solid #e5e5e5;
}
.stButton > button {
    background:#10a37f;
    color:white;
    border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

# ================= LOAD MODEL =================
@st.cache_resource
def load_ai():
    return load_model()

tokenizer, model = load_ai()

# ================= SIDEBAR =================
st.sidebar.header("Settings")
max_tokens = st.sidebar.slider("Max Tokens", 200, 2000, 800, 100)
temperature = st.sidebar.slider("Creativity", 0.1, 1.0, 0.3)

# ================= INPUT =================
user_input = st.text_area(
    "Message",
    placeholder="Ask anything... (chat, Arduino code, explanation)",
    height=120
)

send = st.button("Send ➤")

# ================= RESPONSE =================
if send:
    if user_input.strip() == "":
        st.warning("Please enter a message")
    else:
        with st.spinner("AI is thinking..."):
            system_prompt = (
                "You are a helpful AI assistant. "
                "You answer questions, generate Arduino code, "
                "and explain concepts in simple language.\n\n"
            )

            prompt = system_prompt + "User:\n" + user_input + "\nAssistant:"
            reply = generate_response(
                tokenizer, model, prompt, max_tokens, temperature
            )

        st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
        st.markdown("**You:**")
        st.write(user_input)
        st.markdown("---")
        st.markdown("**AI:**")
        st.write(reply)
        st.markdown("</div>", unsafe_allow_html=True)
