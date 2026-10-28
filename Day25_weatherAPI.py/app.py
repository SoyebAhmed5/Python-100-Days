from flask import Flask, jsonify

app = Flask(__name__)

# Mock Weather Data
weather_data = {
    "Dhaka": {"temperature": 29, "condition": "cloudy"},
    "Chittagong": {"temperature": 27, "condition": "rainy"},
    "Sylhet": {"temperature": 24, "condition": "windy"},
    "Khulna": {"temperature": 31, "condition": "sunny"},
    "Rajshahi": {"temperature": 30, "condition": "clear"}
}

# Root Endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Mini Weather API"})

# Get Weather for All Cities
@app.route('/weather', methods=['GET'])
def get_weather():
    return jsonify(weather_data)

# Get Weather for One City
@app.route('/weather/<city>', methods=['GET'])
def get_city_weather(city):
    city_name = city.title()

    if city_name in weather_data:
        return jsonify({"city": city_name, "weather": weather_data[city_name]})
    return jsonify({"error": "City not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)