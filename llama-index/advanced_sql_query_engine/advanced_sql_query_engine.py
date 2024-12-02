from llama_index.llms.ollama import Ollama
from llama_index.core.objects import (
    SQLTableNodeMapping,
    ObjectIndex,
    SQLTableSchema,
)
from llama_index.core import SQLDatabase, VectorStoreIndex

from summerize_tables import generate_summary


table_summary_llm = llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="dolphin-llama3:latest", request_timeout=30.0)


#create database engine
database_url = 'postgresql://didex:didex@localhost:5432/didex'
engine = create_engine(database_url)

# Get the inspector
inspector = inspect(engine)

# Get the table names
table_names = inspector.get_table_names()
print(table_names)

#create databse
sql_database = SQLDatabase(engine)


table_node_mapping = SQLTableNodeMapping(sql_database)
table_schema_objs = [
    (SQLTableSchema(table_name=table_name))
    for table_name in table_names
]  # add a SQLTableSchema for each table

obj_index = ObjectIndex.from_objects(
    table_schema_objs,
    table_node_mapping,
    VectorStoreIndex,
)
obj_retriever = obj_index.as_retriever(similarity_top_k=3)


table_context_string = get_table_context_str(obj_retriever)