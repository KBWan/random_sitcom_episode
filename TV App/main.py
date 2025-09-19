from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

from moviedb import get_random_episode
app = Flask(__name__)
CORS(app)

@app.route('/get_episode', methods=['GET'])
def handle_get():
    response_data = get_random_episode()
    print(response_data)
    return make_response(jsonify(response_data), 200)

if __name__ == '__main__':
    app.run(debug=True)