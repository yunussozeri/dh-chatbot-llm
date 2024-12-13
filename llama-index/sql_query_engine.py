
from sqlalchemy import create_engine, MetaData, inspect

from llama_index.core import SQLDatabase, Settings
from llama_index.core.query_engine import NLSQLTableQueryEngine, RetrieverQueryEngine
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

from llama_index.core.retrievers import NLSQLRetriever

from rich.console import Console


#init rich console
console = Console()


#create database engine
database_url = 'postgresql://didex:didex@localhost:5432/didex'
engine = create_engine(database_url)

# Get the inspector
inspector = inspect(engine)

# Get the table names
table_names = inspector.get_table_names()
print(table_names)


#init llm
#llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="phi3:3.8b-mini-4k-instruct-q8_0", request_timeout=30.0)
llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="dolphin-llama3:latest", request_timeout=30.0)
#llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="gemma2:9b", request_timeout=30.0)
#llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="mistral:latest", request_timeout=30.0)
#llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="sqlcoder:7b", request_timeout=60.0)
#llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="sqlcoder:15b", request_timeout=60.0)
#llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="gemma2:9b", request_timeout=30.0)


#init embedding
ollama_embedding = OllamaEmbedding(
    #model_name="mxbai-embed-large",
    model_name="nomic-embed-text",
    base_url="http://benedikt-home-server.duckdns.org:11434",
    #ollama_additional_kwargs={"mirostat": 0},
)


#service_context = Settings.from_defaults(llm=llm, embed_model="local:BAAI/bge-base-en-v1.5")
#hf_embedding = HuggingFaceEmbedding(
#    model_name="BAAI/bge-small-en-v1.5"
#)


#create db object
sql_database = SQLDatabase(
    engine, include_tables=["datalayers_datalayer"]
)

#init retriever
nl_sql_retriever = NLSQLRetriever(
    sql_database, tables=table_names, return_raw=True, embed_model=ollama_embedding, llm=llm
)

#retrieved results
query_str = "What is the name of the shape with the smallest area and how big is it?"
results = nl_sql_retriever.retrieve(
    query_str
)
console.print(f'[bold]{results}[/bold]')



query_engine = RetrieverQueryEngine.from_args(nl_sql_retriever, llm=llm, embed_model=ollama_embedding)

response = query_engine.query(
    query_str
)

console.print(f'[bold]{response}[/bold]')

#init query engine
# query_engine = NLSQLTableQueryEngine(
#     sql_database=sql_database, tables=table_names, verbose=True, embed_model=ollama_embedding, llm=llm, 
# )

#execute query

console.print(f'[bold]{query_str}[/bold]')


response = query_engine.query(query_str)

