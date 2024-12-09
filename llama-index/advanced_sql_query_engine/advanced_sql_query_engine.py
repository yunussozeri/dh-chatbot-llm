from sqlalchemy import create_engine, MetaData, inspect

from llama_index.llms.ollama import Ollama
from llama_index.core.objects import (
    SQLTableNodeMapping,
    ObjectIndex,
    SQLTableSchema,
)
from llama_index.core import SQLDatabase, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding

from llama_index.core.retrievers import SQLRetriever

from llama_index.core.retrievers import SQLRetriever
from typing import List
from llama_index.core.query_pipeline import FnComponent

from llama_index.core.objects import (
    SQLTableSchema
)

from llama_index.core.prompts.default_prompts import DEFAULT_TEXT_TO_SQL_PROMPT
from llama_index.core import PromptTemplate
from llama_index.core.query_pipeline import FnComponent
from llama_index.core.llms import ChatResponse

from IPython.display import display, HTML

from pyvis.network import Network


llm_synth = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="dolphin-llama3:latest", request_timeout=30.0)

llm_sql = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="dolphin-llama3:latest", request_timeout=30.0)
#llm_sql = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="mistral:latest", request_timeout=60.0)


llm_summary = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="dolphin-llama3:latest", request_timeout=30.0)

#init embedding
ollama_embedding = OllamaEmbedding(
    #model_name="mxbai-embed-large",
    model_name="nomic-embed-text",
    base_url="http://benedikt-home-server.duckdns.org:11434",
    #ollama_additional_kwargs={"mirostat": 0},
)

#create database engine
database_url = 'postgresql://didex:didex@localhost:5432/didex'
engine = create_engine(database_url)

# Get the inspector
inspector = inspect(engine)

# Get the table names
table_names = inspector.get_table_names()
print(table_names)

table_names.remove('app_user_groups')
table_names.remove('django_content_type')
table_names.remove('django_migrations')
table_names.remove('django_session')
table_names.remove('auth_group')
table_names.remove('auth_group_permissions')

print('after cleanup:')
print(table_names)

#create databse
sql_database = SQLDatabase(engine)

#create sql retriever
sql_retriever = SQLRetriever(sql_database)

table_infos = {
    'datalayers_datalayer':'',
    'secondary_unit_lookup':'',
    'state_lookup':'',
    'street_type_lookup':'',
    'spatial_ref_sys':'',
    'geocode_settings':'',
    'geocode_settings_default':'',
    'direction_lookup':'',
    'place_lookup':'',
    'county_lookup':'',
    'countysub_lookup':'',
    'zip_lookup_all':'',
    'zip_lookup_base':'',
    'zip_lookup':'',
    'county':'',
    'state':'',
    'place':'',
    'zip_state':'',
    'zip_state_loc':'',
    'cousub':'',
    'edges':'',
    'addrfeat':'',
    'featnames':'',
    'addr':'',
    'zcta5':'',
    'tabblock20':'',
    'faces':'',
    'loader_platform':'',
    'loader_variables':'',
    'loader_lookuptables':'',
    'tract':'',
    'tabblock':'',
    'bg':'',
    'pagc_gaz':'',
    'pagc_lex':'',
    'pagc_rules':'',
    'topology':'',
    'layer':'',
    'auth_permission':'',
    'chirps_prcp':'This table provides precipitation data for Ghana',
    'chirps_tprecit':'',
    'chirts_maxt':'',
    'chirts_tmax':'',
    'copernicus_built':'',
    'copernicus_crop':'',
    'copernicus_forest':'',
    'copernicus_herbveg':'',
    'copernicus_herbwet':'',
    'copernicus_moss':'',
    'copernicus_schrub':'',
    'copernicus_shrub':'',
    'copernicus_sparse':'',
    'copernicus_water':'',
    'custom_covreflab':'',
    'data_custom_covreflab':'',
    'data_healthsitesio_facilities':'',
    'data_osm_river':'',
    'app_user':'',
    'app_user_user_permissions':'',
    'datalayers_datalayerlogentry':'',
    'datalayers_datalayersource':'',
    'datalayers_datalayer_related_to':'',
    'dhs_drinkwater':'',
    'era5_t2m':'',
    'healthsitesio_facilities':'',
    'koeppen_a':'',
    'koeppen_af':'',
    'koeppen_am':'',
    'koeppen_aw':'',
    'koeppen_b':'',
    'koeppen_bs':'',
    'koeppen_bw':'',
    'koeppen_c':'',
    'koeppen_cf':'',
    'datalayers_category':'',
    'django_admin_log':'',
    'koeppen_cs':'',
    'koeppen_cw':'',
    'koeppen_d':'',
    'koeppen_df':'',
    'koeppen_ds':'',
    'koeppen_dw':'',
    'koeppen_e':'',
    'koeppen_ef':'',
    'koeppen_et':'',
    'malariaatlas_traveltimehc':'',
    'meteo_maxt':'',
    'meteo_mint':'',
    'meteo_prcp':'This table provides precipitation data for Ghana',
    'meteo_tavg':'',
    'meteo_tmax':'',
    'meteo_tmin':'',
    'meteo_tprecit':'',
    'meteostat_daily':'',
    'meteostat_hourly':'',
    'meteostat_stations':'',
    'shapes_shape':'',
    'worldpop_popc':'',
    'worldpop_popd':'',
    'shapes_type':'',
    'taggit_taggeditem':'',
    'taggit_tag':''
}



def get_table_context_str(table_schema_objs: List[SQLTableSchema]):
    """Get table context string."""
    context_strs = []
    for table_schema_obj in table_schema_objs:
        table_info = sql_database.get_single_table_info(
            table_schema_obj.table_name
        )
        if table_schema_obj.context_str:
            table_opt_context = " The table description is: "
            table_opt_context += table_schema_obj.context_str
            table_info += table_opt_context

        context_strs.append(table_info)
    return "\n\n".join(context_strs)

table_parser_component = FnComponent(fn=get_table_context_str)


table_node_mapping = SQLTableNodeMapping(sql_database)

table_schema_objs = [
    SQLTableSchema(table_name=table_name, context_str=table_infos.get(table_name))
    for table_name in table_names
]  # add a SQLTableSchema for each table

obj_index = ObjectIndex.from_objects(
    table_schema_objs,
    table_node_mapping,
    VectorStoreIndex,
    embed_model=ollama_embedding
)
obj_retriever = obj_index.as_retriever(similarity_top_k=3)


table_context_string = get_table_context_str(table_schema_objs)

print(table_context_string)


def parse_response_to_sql(response: ChatResponse) -> str:
    """Parse response to SQL."""
    response = response.message.content
    sql_query_start = response.find("SQLQuery:")
    if sql_query_start != -1:
        response = response[sql_query_start:]
        # TODO: move to removeprefix after Python 3.9+
        if response.startswith("SQLQuery:"):
            response = response[len("SQLQuery:") :]
    sql_result_start = response.find("SQLResult:")
    if sql_result_start != -1:
        response = response[:sql_result_start]
    return response.strip().strip("```").strip()


sql_parser_component = FnComponent(fn=parse_response_to_sql)

text2sql_prompt = DEFAULT_TEXT_TO_SQL_PROMPT.partial_format(
    dialect=engine.dialect.name
)
print(text2sql_prompt.template)



response_synthesis_prompt_str = (
    "Given an input question, synthesize a response from the query results.\n"
    "Query: {query_str}\n"
    "SQL: {sql_query}\n"
    "SQL Response: {context_str}\n"
    "Response: "
)
response_synthesis_prompt = PromptTemplate(
    response_synthesis_prompt_str,
)


from llama_index.core.query_pipeline import (
    QueryPipeline as QP,
    Link,
    InputComponent,
    CustomQueryComponent,
)

qp = QP(
    modules={
        "input": InputComponent(),
        "table_retriever": obj_retriever,
        "table_output_parser": table_parser_component,
        "text2sql_prompt": text2sql_prompt,
        "text2sql_llm": llm_sql,
        "sql_output_parser": sql_parser_component,
        "sql_retriever": sql_retriever,
        "response_synthesis_prompt": response_synthesis_prompt,
        "response_synthesis_llm": llm_synth,
    },
    verbose=True,
)


qp.add_chain(["input", "table_retriever", "table_output_parser"])
qp.add_link("input", "text2sql_prompt", dest_key="query_str")
qp.add_link("table_output_parser", "text2sql_prompt", dest_key="schema")
qp.add_chain(
    ["text2sql_prompt", "text2sql_llm", "sql_output_parser", "sql_retriever"]
)
qp.add_link(
    "sql_output_parser", "response_synthesis_prompt", dest_key="sql_query"
)
qp.add_link(
    "sql_retriever", "response_synthesis_prompt", dest_key="context_str"
)
qp.add_link("input", "response_synthesis_prompt", dest_key="query_str")
qp.add_link("response_synthesis_prompt", "response_synthesis_llm")




net = Network(notebook=True, cdn_resources="in_line", directed=True)
net.from_nx(qp.dag)


# Save the network as "text2sql_dag.html"
net.write_html("text2sql_dag.html")


# Read the contents of the HTML file
with open("text2sql_dag.html", "r") as file:
    html_content = file.read()

# Display the HTML content
display(HTML(html_content))


response = qp.run(
    #query="I need a quick overview of the Ada East district, Ghana. How large is this district, how many people live there, and what is the most recent urbanization rate?"
    #query="I need the location of all schools in Kumasi district, Ghana. Is this dataset available?"
    query="For my research project on malaria, I need precipitation data for the period from January 2020 to December 2023. Are these data available, and in what resolution?"
)
print(str(response))