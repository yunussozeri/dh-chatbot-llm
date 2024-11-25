from llama_index.llms.ollama import Ollama

from llama_index.core.llms import ChatMessage

from import_dh_data import get_json_data

import logging
import sys
from IPython.display import Markdown, display

from llama_index.core.query_engine import JSONalyzeQueryEngine



logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))



json_data = get_json_data()



#llm = Ollama(model="gemma2:2b", request_timeout=30.0)
#llm = Ollama(base_url='http://localhost:11434', model="dolphin-llama3:latest", request_timeout=220.0)
#llm = Ollama(base_url='http://localhost:8001', model="dolphin-llama3:latest", request_timeout=220.0)
llm = Ollama(base_url='http://benedikt-home-server.duckdns.org:11434', model="dolphin-llama3:latest", request_timeout=220.0)
#llm = Ollama(base_url='http://localhost:8001/api/v1/namespaces/wem133-default/services/ollama:http/proxy/', model="dolphin-llama3:latest", request_timeout=220.0)
#llm = Ollama(base_url='http://home-server.home.arpa:11434', model="dolphin-llama3:latest", request_timeout=30.0)
#llm = Ollama(base_url='http://home-server.home.arpa:11434', model="phi3:mini", request_timeout=30.0)
#llm = Ollama(base_url='http://localhost:11434', model="phi3:mini", request_timeout=120.0)



nl_query_engine = JSONalyzeQueryEngine(
    list_of_dict=json_data,
    llm=llm,
    verbose=True,
)
#raw_query_engine = JSONalyzeQueryEngine(
#    list_of_dict=json_data,
#    llm=llm,
#    synthesize_response=False,
#)

#nl_response = nl_query_engine.query("What years are covered in the data? ")
#raw_response = raw_query_engine.query(
#    "What years are covered?",
#)


#display(Markdown(f"<h1>Natural language Response</h1><br><b>{nl_response}</b>"))
#display(Markdown(f"<h1>Raw Response</h1><br><b>{raw_response}</b>"))


resp = llm.complete("Who is Paul Graham?")
print(resp)



# messages = [
#     ChatMessage(
#         role="system", content="You are a pirate with a colorful personality"
#     ),
#     ChatMessage(role="user", content="What is your name and how was your day?"),
# ]
# resp = llm.stream_chat(messages)

# for r in resp:
#     print(r.delta, end="")