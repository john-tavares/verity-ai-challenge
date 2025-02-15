import streamlit as st
from dotenv import load_dotenv
from langgraph.graph import Graph, START, END
from agent.sql_agent import sql_agent_node

load_dotenv()

workflow = Graph()
workflow.add_node("sql_agent_node", sql_agent_node)
workflow.add_edge(START, "sql_agent_node")
workflow.add_edge("sql_agent_node", END)
app = workflow.compile()

st.title("SQL Agent - Verity Challenge")
st.write("Faça uma pergunta relacionada aos dados.")

question = st.text_input("Digite sua pergunta:")

if question:
    response = app.invoke(question)
    st.write("**Resposta:**", response['output'])