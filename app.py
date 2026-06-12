import streamlit as st
from src.chatbot import generate_answer

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Nineleaps HR Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------
# SESSION MEMORY
# ---------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------
# CUSTOM CSS
# ---------------------------------

st.markdown("""
<style>

/* Main Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        135deg,
        #0A192F,
        #112240,
        #1B263B
    );
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #081120;
}

/* Header */
.hero {
    text-align: center;
    padding: 20px;
}

.hero h1 {
    color: white;
    font-size: 48px;
    font-weight: bold;
}

.hero p {
    color: #B8C1CC;
    font-size: 18px;
}

/* Answer Card */
.answer-box {
    background: #16213E;
    color: white;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #00C8FF;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

/* Source Card */
.source-box {
    background: #0F172A;
    color: white;
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
    border: 1px solid #1E293B;
}

/* Buttons */
.stButton button {
    width: 100%;
    border-radius: 10px;
    background-color: #1E3A8A;
    color: white;
    border: none;
}

.stButton button:hover {
    background-color: #2563EB;
    color: white;
}

/* Text Colors */
h1, h2, h3, h4, h5, h6,
p, div, span, label {
    color: white !important;
}

/* Chat Input */
[data-testid="stChatInput"] {
    background-color: #16213E !important;
    border-radius: 15px;
}

[data-testid="stChatInput"] textarea {
    color: white !important;
    -webkit-text-fill-color: white !important;
    caret-color: white !important;
    font-size: 16px !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #CBD5E1 !important;
    opacity: 1 !important;
}

[data-testid="stChatInput"] * {
    color: white !important;
}

textarea {
    color: white !important;
}

input {
    color: white !important;
}

/* Chat Messages */
[data-testid="stChatMessage"] {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------
# HEADER
# ---------------------------------

st.markdown("""
<div class="hero">
    <h1>🤖 Nineleaps HR Knowledge Assistant</h1>
    <p>
        AI-powered HR Policy Search using RAG 
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------
# SIDEBAR
# ---------------------------------

st.sidebar.title("💡 Suggested Questions")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

sample_questions = [
    "What is the leave policy?",
    "What are the employee benefits?",
    "What is the attendance policy?",
    "What is the reimbursement policy?",
    "What is the absence policy?"
]

selected_question = None

for q in sample_questions:
    if st.sidebar.button(q):
        selected_question = q

# ---------------------------------
# DISPLAY OLD CHAT
# ---------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"],
            unsafe_allow_html=True
        )

# ---------------------------------
# CHAT INPUT
# ---------------------------------

question = st.chat_input(
    "Ask a question about Nineleaps HR Policies..."
)

if selected_question:
    question = selected_question

# ---------------------------------
# PROCESS QUESTION
# ---------------------------------

if question:

    # Show user message

    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Build recent conversation history

    history = ""

    for msg in st.session_state.messages[-6:]:

        history += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    with st.spinner("🔍 Searching HR Knowledge Base..."):

        answer, sources = generate_answer(
            question,
            history
        )

    assistant_response = f"""
<div class="answer-box">
{answer}
</div>

<br>

### 📚 Sources
"""

    for source in sorted(set(sources)):

        assistant_response += f"""
<div class="source-box">
{source}
</div>
"""

    with st.chat_message("assistant"):

        st.markdown(
            assistant_response,
            unsafe_allow_html=True
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )