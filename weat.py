from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,

    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_info = None

    if request.method == 'POST':
        city_name = request.form['city']
        api_key = "YOUR_API_KEY"  # Замените на свой API-ключ OpenWeatherMap
        weather_info = get_weather(api_key, city_name)

    return render_template('index_weather.html', weather_info=weather_info)

if __name__ == '__main__':
    app.run(debug=True)
