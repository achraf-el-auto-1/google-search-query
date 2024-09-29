from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_webhook():
    data = request.json
    keyword = data.get('keyword', '')

    if not keyword:
        return jsonify({"error": "No keyword provided"}), 400

    # Perform Google search
    search_results = google_search(keyword)

    return jsonify(search_results)

def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': 'YOUR_API_KEY',  # Replace with your actual API key
        'cx': 'YOUR_CUSTOM_SEARCH_ENGINE_ID',  # Replace with your actual Custom Search Engine ID
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return {"error": "Failed to fetch search results"}

    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
