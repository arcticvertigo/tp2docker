from flask import request, jsonify, Flask
import os, requests
from requests import Request, Session, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def api_weather():
    LAT = request.args.get('lat')
    LONG = request.args.get('lon')

    uri = f"http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid=6f29b20e132befc91999eee96ac0cbc2&units=metric"

    res = requests.get(uri)
    if res.status_code == 200:
        data = res.json()
        
        lat = data['coord']['lat']
        long = data['coord']['lon']
        weather = data['weather'][0]['main']
        more_details = data['weather'][0]['description']
        temp = data['main']['temp']
        temp_feel = data['main']['feels_like']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
 
        result = {
            'latitude': lat,
            'longitude': long,
            'weather': weather,
            'detailed': more_details,
            'actual temperature': temp,
            'feeling': temp_feel,
            'pressure': pressure,
            'humidity': humidity            
        }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
