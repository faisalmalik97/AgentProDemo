import streamlit as st
from agentpro import create_model, ReactAgent
from agentpro.tools import AresInternetTool, CalculateTool, SlideGenerationTool, TraversaalProRAGTool
import os
from agentpro import create_model
from openai import OpenAI
import time


# API keys from Streamlit secrets
api_key = st.secrets["OPENAI_API_KEY"]
ares_key = st.secrets["ARES_API_KEY"]

st.set_page_config(
page_title="Support Assistant Agent", layout="wide"
)
st.title(" 🇦🇺 Citizenship Test Assistant Agent")
st.header("Quick answers from test booklet and web")


#Sample Questions for suggestion
sample_query = """
1. What is national flower of Australia?
2. What is australian national anthem called and show it here?
3. Tell me about number of seats in lower house and upper house?
4. How many states and territories in Australia?
5. Which city is capital of Queensland?
  
"""

#dropdown list of sample questons
with st.expander("You can ask questions like..... (click here ! )"):
    st.text_area("Sample Questions", value=sample_query, height=200, disabled=True)


#Query input area  
user_query = st.text_area("Enter your question here ⬇️ ", height=150)


#answer_btn = st.button("ANSWER 🔲 ", use_container_width=True)
st.sidebar.link_button('🇦🇺 HomeAffair Website ', 'https://immi.homeaffairs.gov.au', use_container_width=True)
st.sidebar.link_button('Test & Interview Info ', 'https://immi.homeaffairs.gov.au/citizenship/test-and-interview/our-common-bond', use_container_width=True)
st.sidebar.link_button('Download Testbooklet', 'https://immi.homeaffairs.gov.au/citizenship-subsite/files/our-common-bond-testable.pdf', use_container_width=True)
st.sidebar.info('This is for purely informational purposes', icon="ℹ️", width="stretch")
st.sidebar.markdown('''Press button below to get answer of your question! :balloon:  ''')
answer_btn = st.sidebar.button(" ANSWER 🔲 ", use_container_width=True)

if answer_btn:
  time.sleep(2)
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
            
            response = agent.run(query)
            st.markdown(response.final_answer, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.info("👈 Press ANSWER 🔲 button on left side to begin.")


