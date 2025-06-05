import streamlit as st
from agentpro import create_model, ReactAgent
from agentpro.tools import AresInternetTool, CalculateTool, SlideGenerationTool, TraversaalProRAGTool
import os
from agentpro import create_model
from openai import OpenAI


# Set your API keys here or use Streamlit secrets
#openai.api_key = st.secrets["OPENAI_API_KEY"]
#ares_key = st.secrets["ARES_KEY"]

st.set_page_config(page_title="Agent Assistant", layout="wide")
st.title("🔍 AI Agent")
st.header("AI Agent")
