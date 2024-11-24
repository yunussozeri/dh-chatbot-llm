from sqlalchemy import create_engine

from llama_index.core import SQLDatabase
from llama_index.llms.ollama import Ollama

from llama_index.core.query_engine import NLSQLTableQueryEngine






database_url = 'postgresql://didex:didex@localhost:5432/didex'
engine = create_engine(database_url)


#llm = Ollama(base_url='http://home-server.home.arpa:11434', model="dolphin-llama3:latest", request_timeout=30.0)
llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="dolphin-llama3:latest", request_timeout=30.0)
#service_context = ServiceContext.from_defaults(llm=llm)

sql_database = SQLDatabase(
    engine, include_tables=["datalayers_datalayer"]
)

query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database, tables=["city_stats"], llm=llm
)

query_str = "Wich district is the largest in Ghana?"
response = query_engine.query(query_str)