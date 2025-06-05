import streamlit as st
from agentpro import create_model, ReactAgent
from agentpro.tools import AresInternetTool, CalculateTool, SlideGenerationTool, TraversaalProRAGTool
import os
from agentpro import create_model
from openai import OpenAI


# API keys from Streamlit secrets
api_key = st.secrets["OPENAI_API_KEY"]
ares_key = st.secrets["ARES_API_KEY"]

st.set_page_config(
page_title="Support Assistant Agent", layout="wide"
)
st.title(" 🇦🇺 Citizenship Test Assistant Agent")
st.header("Quick answers from test booklet and web")

sample_query = """
Please show me sample questions
1. What is national flower of Australia?
2. What is australian national anthem called and show it here?
3. Tell me about number of seats in lower house and upper house?
4. How many states and territories in Australia?
5. Which city is capital of Queensland?
  
"""

with st.expander("Example query (read-only)"):
    st.text_area("Sample Query", value=sample_query, height=200, disabled=True)

input_mode = st.radio("See Available Options:", ["Enter full query text"])

input_mode == "Enter full query text"
user_query = st.text_area("Enter your full query here", height=250)
answer_btn = st.sidebar.button("ANSWER", use_container_width=True))


if answer_btn:
   with st.spinner(" Please wait..................Aalyzing query and generating answer..."):
        try:
            # Create a model with OpenAI
            model = create_model(provider="openai", model_name="gpt-4o", api_key=os.getenv("OPENAI_API_KEY", None))
            #input_mode = st.radio("Choose input mode:", ["Enter full query text", "Set parameters"])

            # Initialize tools
            traversaal_rag_tool = TraversaalProRAGTool(api_key=os.getenv("TRAVERSAAL_PRO_API_KEY", None), document_names="australian_citizenship_testbook")
            tools = [AresInternetTool(os.getenv("ARES_API_KEY", None)), CalculateTool(), SlideGenerationTool(), traversaal_rag_tool]

            # Initialize agent
            agent = ReactAgent(model=model, tools=tools)

            # Run a query
            query = user_query
            #query = "capital city of Jordan??"
            response = agent.run(query)
            st.markdown(response.final_answer, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.info("👈 Press ANSWER button to begin.")


