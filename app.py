from flask import Flask, jsonify

app = Flask(__name__)

# Sample data to be returned by the API
locations = ["Lalapet", "Tarnaka", "Mettuguda", "Alugadda Bhavi", "Secunderabad"]

@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True)
