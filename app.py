import requests

from flask import Flask, render_template, request
from flask_restful import Resource, Api


#generate app/api variables
app = Flask(__name__)
api = Api(app)


# Routes

@app.route('/', methods=['GET', 'POST'])
def index():
    city = 'Las Vegas'
    if request.method == 'POST':
        if request.form.get('city'):
            city = request.form.get('city')
    URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=14ca98ddeb3b5cba1bba4695d6a92225'

    weather = {}
    req = requests.get(URL.format(city)).json()
    try:
        weather = {
            'city': city,
            'country': req['sys']['country'],
            'temp': round(req['main']['temp']),
            'desc': req['weather'][0]['description'],
            'icon': req['weather'][0]['icon']
        }
    except:
        pass
    
    return render_template('index.html', weather=weather)





# Start the api
if __name__ == '__main__':
    app.run()
