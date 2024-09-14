from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace this with your OpenWeatherMap API key
API_KEY = "b5ef1883af5a53434b536b0d231ac89a"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')  # Get city name from form input
    if city:
        # API URL with the city name and API key
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(weather_url)  # Send a GET request to the API
        data = response.json()  # Convert the response to a Python dictionary

        if data["cod"] == 200:  # Check if the response is successful
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            return render_template('index.html', weather=weather_data)
        else:
            return render_template('index.html', error="City not found!")
    else:
        return render_template('index.html', error="Please enter a city name.")

if __name__ == "__main__":
    app.run(debug=True)
