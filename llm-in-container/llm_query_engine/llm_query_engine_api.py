from flask import Flask, request, jsonify, Response
from llm_query_engine.query_engine import LLMQueryEngine
from flask_cors import CORS
# Initialize the Flask application and the LLMQueryEngine instance
app = Flask(__name__)
CORS(app,resources={r"/query": {"origins": "http://localhost:8000"}}, methods=["POST", "GET"])
llm = LLMQueryEngine()
@app.route('/query', methods=['GET'])
def query_get():
    # Access the query parameter from the URL
    query_string = request.args.get("query")

    if not query_string:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    # Create a response using the query string
    response = f'You just submitted the query: {query_string}'

    # Return the JSON response
    return jsonify({
        "query": query_string,
        "response": response
    })

@app.route('/query', methods=['POST'])
def query_post():
    data = request.json
    query_string = data.get("query")
    
    if not query_string:
        return jsonify({"error": "Missing 'query' parameter"}), 400
    
    response = llm.submit_query(query_string)
    return jsonify({
        "query": query_string,
        "response": response.response,
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
