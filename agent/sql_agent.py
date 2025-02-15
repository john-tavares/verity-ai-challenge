from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
import os

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