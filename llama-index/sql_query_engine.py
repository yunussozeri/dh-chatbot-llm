from sqlalchemy import create_engine , MetaData, inspect, Engine, Inspector

from llama_index.core import SQLDatabase, Settings, Response
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from typing import Optional
from rich.console import Console


#init rich console
console = Console()

'''
#create database engine
database_url = 'postgresql://didex:didex@localhost:5432/didex'
engine = create_engine(database_url)

# Get the inspector
inspector = inspect(engine)

# Get the table names
table_names = inspector.get_table_names()
print(table_names)


#init llm
llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="dolphin-llama3:latest", request_timeout=30.0)
#llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="gemma2:9b", request_timeout=30.0)
#llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="mistral:latest", request_timeout=30.0)
#llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="sqlcoder:7b", request_timeout=60.0)
#llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="sqlcoder:15b", request_timeout=60.0)
#llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="gemma2:9b", request_timeout=30.0)


#init embedding
ollama_embedding = OllamaEmbedding(
    model_name="mx-bai-embed-large",
    base_url="http://benedikt-home-server.duckdns.org:11434",
    #ollama_additional_kwargs={"mirostat": 0},
)

#service_context = Settings.from_defaults(llm=llm, embed_model="local:BAAI/bge-base-en-v1.5")
#hf_embedding = HuggingFaceEmbedding(
#    model_name="BAAI/bge-small-en-v1.5"
#)


#create db object
sql_database = SQLDatabase(
    engine, include_tables=table_names
)

#init query engine
query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database, tables=table_names, verbose=True, embed_model=ollama_embedding, llm=llm
)

#execute query
query_str = "What is the name of the shape with the smallest area and how big is it?"
console.print(f'[bold]{query_str}[/bold]')

response = query_engine.query(query_str)
console.print(f'[bold]{response}[/bold]')

'''

class LLMQueryEngine:
    _instance: Optional["LLMQueryEngine"] = None  # Singleton instance holder

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, DB_URL: str = 'postgresql://didex:didex@localhost:5432/didex',
                LLM_BASE_URL: str = 'http://benedikt-home-server.duckdns.org:11434',
                MODEL="dolphin-llama3:latest",
                EMBEDDING_MODEL="nomic-embed-text"):
        if not hasattr(self, "initialized"):  # Prevent reinitialization
            self.initialized = True
            self.database_url = DB_URL
            self.engine = create_engine(self.database_url)
            self.inspector = inspect(self.engine)
            self.table_names = self.inspector.get_table_names()

            self.LLM = Ollama(base_url=LLM_BASE_URL,
                              model=MODEL,
                              request_timeout=30.0)
            self.embedding = OllamaEmbedding(model_name=EMBEDDING_MODEL,
                                             base_url=LLM_BASE_URL)
            self.sql_database = SQLDatabase(self.engine,
                                            include_tables=self.table_names)

            self.query_engine = NLSQLTableQueryEngine(sql_database=self.sql_database,
                                                      tables=self.table_names,
                                                      verbose=True,
                                                      embed_model=self.embedding,
                                                      llm=self.LLM)

    def submit_query(self, query_string: str) -> Response:
        response: Response = self.query_engine.query(query_string)
        return response
    
    def test_import(self, test_input):
        
        return test_input+" HOORAY"


llm_engine = LLMQueryEngine()

print(llm_engine.test_import("asjidnasdas"))
        
        
        
        