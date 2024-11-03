from llama_index.llms.ollama import Ollama

from llama_index.core.llms import ChatMessage

#llm = Ollama(model="gemma2:2b", request_timeout=30.0)
llm = Ollama(model="dolphin-llama3:latest", request_timeout=30.0)


#resp = gemma_2b.complete("Who is Paul Graham?")
#print(resp)



messages = [
    ChatMessage(
        role="system", content="You are a pirate with a colorful personality"
    ),
    ChatMessage(role="user", content="What is your name and how was your day?"),
]
resp = llm.stream_chat(messages)

for r in resp:
    print(r.delta, end="")