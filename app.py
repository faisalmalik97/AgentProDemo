import streamlit as st
from agentpro import create_model, ReactAgent
from agentpro.tools import AresInternetTool, CalculateTool, SlideGenerationTool, TraversaalProRAGTool
import os
from agentpro import create_model
from openai import OpenAI


# Set your API keys here or use Streamlit secrets
#openai.api_key = st.secrets["OPENAI_API_KEY"]
#ares_key = st.secrets["ARES_KEY"]

st.set_page_config(page_title="Support Assistant Agent", layout="wide")
st.title("🔍 Support Assistan Agent")
st.header("Header of AI Agent")

# Example query 
sample_query = """
THIS IS AN EXAMPLE QUERY TO TEST AREA OF INPUT
"""

with st.expander("Example query (read-only)"):
    st.text_area("Sample Query", value=sample_query, height=200, disabled=True)

input_mode = st.radio("Choose input mode:", ["Enter full query text", "Set parameters"])

if input_mode == "Enter full query text":
    user_query = st.text_area("Enter your full query here", height=250)
    analyze_btn = st.sidebar.button("Run AGENT")
else:
    # Sidebar parameters
    st.sidebar.header("Signal Simulation Parameters")
    duration = st.sidebar.slider("Duration (s)", 1, 10, 2)
    sampling_rate = st.sidebar.slider("Sampling Rate (Hz)", 500, 10000, 2000)
    frequencies = st.sidebar.text_input("Frequencies (comma-separated)", "50,150,300")
    amplitudes = st.sidebar.text_input("Amplitudes (comma-separated)", "1,0.5,0.2")
    analyze_btn = st.sidebar.button("Run AGENT")
