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
st.title("🔍 Support Assistan Agent")
st.header("Header of AI Agent")

sample_query = """
Please show me blalalll
2.
3.
  
"""

with st.expander("Example query (read-only)"):
    st.text_area("Sample Query", value=sample_query, height=200, disabled=True)

#input_mode = st.radio("See example:", ["Enter full query text"])

input_mode == "Enter full query text"
user_query = st.text_area("Enter your full query here", height=250)
analyze_btn = st.sidebar.button("Run Signal Analysis")
#else:
    # Sidebar parameters
 #   st.sidebar.header("Signal Simulation Parameters")
  #  duration = st.sidebar.slider("Duration (s)", 1, 10, 2)
   # sampling_rate = st.sidebar.slider("Sampling Rate (Hz)", 500, 10000, 2000)
    #frequencies = st.sidebar.text_input("Frequencies (comma-separated)", "50,150,300")
    #amplitudes = st.sidebar.text_input("Amplitudes (comma-separated)", "1,0.5,0.2")
    #analyze_btn = st.sidebar.button("Run Signal Analysis")

if analyze_btn:
   with st.spinner("Generating and analyzing signal..."):
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
            query = "capital city of australia?"
            response = agent.run(query)
            st.markdown(response.final_answer, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.info("👈 Set parameters or enter query and click 'Run Signal Analysis' to begin.")

#def main():
 #   col1, col2 = st.columns([1,5])
  #  with col1:
   #     st.markdown(" Hi")
    #with col2:
     #   st.markdown(" Hi Again")

    #st.markdown(" Processing ")

    #with st.container():
     #   st.markdown("""
      #  <div style="background-color: white">
       # <h3> Input your query here </h3>
        #</div>
        #""" , unsafe_allow_html=True)

#Input section
    #query = st.text_area("", height=100, placeholder="Smaple question here")

#Button area
    #coll, col2, col3 = st. columns ([1, 1, 1])
    #with col2:
     #   run_button = st.button("Run Agent", use_container_width=True)
        
        
#return response
#print(f"\nFinal Answer: {response.final_answer}")
#response = agent.run(query)

