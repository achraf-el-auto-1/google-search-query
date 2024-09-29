from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/your_endpoint', methods=['POST'])
def handle_post():
    data = request.get_json()
    variable1 = data.get('variable1')
    variable2 = data.get('variable2')
    # Process the variables as needed
    return jsonify({'message': 'Variables received successfully'})

if __name__ == '__main__':
    app.run()
