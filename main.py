from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather_data(city):
    # Replace 'YOUR_API_KEY' with your actual weather API key
    url = f'http://api.weatherapi.com/v1/current.json?key=12498a5c18ea416ca1162348230807&q={city}'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        if 'error' in weather_data:
            error_message = weather_data['error']['message']
            return render_template('index.html', error=error_message)
        else:
            location = weather_data['location']['name']
            temperature = weather_data['current']['temp_c']
            humidity = weather_data['current']['humidity']
            condition = weather_data['current']['condition']['text']
            return render_template('index.html', location=location, temperature=temperature, humidity=humidity, condition=condition)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False , host='0.0.0.0')
