from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# @traceable(
#     run_type="chain",
#     name="OpenAI Assistant",
# )
def assistant():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a balance sheet standardiser. Please make the line items standardised"),
        ("user", "Question: {question}")
    ])

    ##streamlit framework

    st.title('Jasim API')
    input_text = st.text_input("Search the topic you want")
    llm = ChatOpenAI(model='gpt-3.5-turbo')


    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser

    if input_text:
        st.write(chain.invoke({'question':input_text}))

assistant()