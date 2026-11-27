from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

#temporary sample data from example schools
#will replace until real database is ready
#using GeoJSON as it uses [longitude, latitude] order

SAMPLE_SCHOOLS = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"name": "Sample Primary school A"},
            "geometry": {"type": "Point", "coordinates": [35.26, -14.48]},

        },
        {
            "type": "Feature",
            "properties": {"name": "Sample Primary School B"},
            "geometry": {"type": "Point", "coordinates": [35.20, -14.40]}
        },
        {
            "type": "Feature",
            "properties": {"name": "Sample primary school C"},
            "geometry": {"type": "Point", "coordinates": [35.35, -14.55]},
        },
    ],
}
@app.route("/api/test")
def test():
    return jsonify({"message": "Backend is working..."})

@app.route("/api/schools")
def get_schools():
    return jsonify(SAMPLE_SCHOOLS)

if __name__ == "__main__":
    app.run(debug=True)