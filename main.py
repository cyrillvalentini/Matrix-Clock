from flask import Flask, render_template, request, jsonify
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from display import render_display

executor = ThreadPoolExecutor(max_workers=1)

matrix = None
clock = None
brightness = None
current_matrix = None
current_clock = None
current_brightness = None


#Clock

def control_display():
    global matrix
    global clock
    global brightness

    current_matrix = None
    current_clock = None
    current_brightness = None
    current_time = None
    x = ""

    while True:
        #Check wether there was a change in matrix or brightness
        
        time.sleep(1)
        x = current_time == datetime.now().strftime("%H%M")
        #print("Aktueller Zustand", x)
        
        if (matrix is not None) or (brightness is not None):
            if (matrix is not None):
                current_matrix = matrix
            if (brightness is not None):
                current_brightness = brightness
            matrix = None
            brightness = None
            current_time = datetime.now().strftime("%H%M")
            #print(current_matrix)
            render_display(current_matrix, clock, current_brightness)
            #print(current_brightness)        
        #If there weren't any changes in matrix or brightness, check if the time has changed.
        
        if x is False:
            if current_matrix is not None:
                current_time = datetime.now().strftime("%H%M")
                render_display(current_matrix, clock, current_brightness)              

#Flask-Server   


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/rgb-image', methods=['POST'])
def get_rgb_image():
    global matrix
    global clock
    data = request.get_json()
    matrix = data
    clock = False
    return jsonify({"message": "Daten für ganzes Bild erfolgreich empfangen"}), 200

@app.route('/api/rgb-clock', methods=['POST'])
def get_rgb_clock():
    global matrix
    global clock
    data = request.get_json()
    matrix = data
    clock = True
    return jsonify({"message": "Daten für Uhr erfolgreich empfangen"}), 200

@app.route('/api/brightness', methods=['POST'])
def set_brightness():
    global brightness
    brightness_new = request.json.get('brightness')
    brightness = brightness_new

    return jsonify({'message': 'Helligkeit erfolgreich eingestellt'})


if __name__ == '__main__':
    
    executor.submit(control_display)
    
    app.run(debug=True, use_reloader=False)

