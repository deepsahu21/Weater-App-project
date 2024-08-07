from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)
byCoordinates = False


@app.route('/', methods =['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        try:
            state = request.form['stateName']
            country = request.form['countryName']
            city = request.form['cityName'] 
            data = get_weather(city, state, country)
        except:
            return render_template('index.html')
    return render_template('index.html', data = data)


@app.route('/get_coordinates',  methods =['GET', 'POST'])
def byCoordinates():
     if request.method == 'POST':
        data = None
        lat = float(request.form['latitude'])
        lon = float(request.form['longitude'])
        data = get_weather(lat = lat, lon = lon)
        return render_template('index.html', data=data)




if __name__ == '__main__':
    app.run(debug = True)