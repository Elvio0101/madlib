
import os
import re
import streamlit as st
from datetime import datetime

# ======================
# Directories
# ======================
TEMPLATE_DIR = "templates"
SAVE_DIR = "saved_stories"

# ======================
# Helper Functions
# ======================
def load_template(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()

def extract_placeholders(template: str):
    return list(dict.fromkeys(re.findall(r"<([^>]+)>", template)))

def fill_template(template: str, user_inputs: dict):
    return re.sub(r"<([^>]+)>", lambda m: user_inputs.get(m.group(1), m.group(0)), template)

def save_story(story: str, template_name: str):
    os.makedirs(SAVE_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.splitext(template_name)[0]
    file_path = os.path.join(SAVE_DIR, f"{base_name}_{timestamp}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(story)
    return file_path

# ======================
# Page Styling
# ======================
st.set_page_config(page_title="MadLib Generator", page_icon="📖", layout="centered")

st.markdown(
    """
    <style>
    /* General Page */
    body {
        background-color: #f9f9f9;
        font-family: 'Segoe UI', sans-serif;
        color: #333;
    }
    /* Title */
    .title {
        text-align: center;
        font-size: 2.2em;
        color: #2c3e50;
        font-weight: 600;
        margin-bottom: 20px;
    }
    /* Subtitle */
    .subtitle {
        font-size: 1.2em;
        color: #34495e;
        margin-bottom: 12px;
    }
    /* Inputs */
    .stTextInput > div > div > input {
        border: 1px solid #d0d7de;
        border-radius: 6px;
        padding: 8px;
        font-size: 1em;
    }
    /* Story box */
    .story-box {
        background-color: #ffffff;
        border: 1px solid #e1e4e8;
        border-radius: 8px;
        padding: 16px;
        margin-top: 15px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
        font-size: 1.05em;
        line-height: 1.6;
    }
    /* Success message */
    .stSuccess {
        font-weight: 500;
        color: #2c7a7b !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ======================
# App Title
# ======================
st.markdown("<div class='title'>📖 MadLib Generator</div>", unsafe_allow_html=True)

# ======================
# Template Selection
# ======================
templates = [f for f in os.listdir(TEMPLATE_DIR) if f.endswith(".txt")]
template_name = st.selectbox("Choose a Template", templates)

if template_name:
    template_path = os.path.join(TEMPLATE_DIR, template_name)
    template = load_template(template_path)
    placeholders = extract_placeholders(template)

    st.markdown("<div class='subtitle'>📝 Fill in the blanks</div>", unsafe_allow_html=True)
    user_inputs = {}
    for ph in placeholders:
        user_inputs[ph] = st.text_input(f"Enter a {ph}")

    if st.button("✨ Generate Story"):
        story = fill_template(template, user_inputs)
        st.session_state["story"] = story
        st.session_state["template_name"] = template_name
        st.markdown("<div class='subtitle'>📖 Your Story</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='story-box'>{story}</div>", unsafe_allow_html=True)

if "story" in st.session_state:
    if st.button("💾 Save Story"):
        file_path = save_story(st.session_state["story"], st.session_state["template_name"])
        st.success(f"✅ Story saved to: {file_path}")