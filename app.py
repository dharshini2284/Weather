from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "beb6ae1a9367bec7eb4a8e8d9a300a91"  # Replace with your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.json.get("city")
    if not city:
        return jsonify({"error": "City name is required"}), 400   
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code != 200:
        return jsonify({"error": data.get("message", "Failed to fetch weather data")})
    
    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"].capitalize()
    }
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run()
