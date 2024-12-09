from flask import Flask, request, jsonify
from llm_query_engine.query_engine import LLMQueryEngine

# Initialize the Flask application and the LLMQueryEngine instance
app = Flask(__name__)
llm = LLMQueryEngine()

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query_string = data.get("query")
    
    if not query_string:
        return jsonify({"error": "Missing 'query' parameter"}), 400
    
    response = llm.submit_query(query_string)
    return jsonify({
        "query": query_string,
        "response": response.response,
        "graph": str(llm.graph.nodes)  # You can choose to return the graph or parts of it
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
