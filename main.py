from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
from langgraph.graph import Graph, START, END
import os

load_dotenv()

questions = [
    "Quais clientes compraram um Notebook?",        
    "Quanto cada cliente gastou no total?",
    "Quem tem saldo suficiente para comprar um Smartphone?",
    "Quem é você?"
]

def sql_agent_node(question):
    db_uri = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:"
        f"{os.getenv('POSTGRES_PORT')}/"
        f"{os.getenv('POSTGRES_DATABASE')}"
    )

    db = SQLDatabase.from_uri(db_uri)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, verbose=os.getenv("VERBOSE", False))

    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=SQLDatabaseToolkit(db=db, llm=llm),
        verbose=os.getenv("VERBOSE", False),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )

    try:
        result = agent_executor.invoke(question)
    except ValueError:
        result = {"input": question, "output": "Não entendi a pergunta, ou não posso falar sobre isso."}
    return result

workflow = Graph()
workflow.add_node("sql_agent_node", sql_agent_node)

workflow.add_edge(START, "sql_agent_node")
workflow.add_edge("sql_agent_node", END)

app = workflow.compile()

for question in questions:
    response = app.invoke(question)
    print(f"{response['input']} -> {response['output']}")