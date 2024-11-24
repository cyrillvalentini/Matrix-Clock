from flask import Flask, render_template, request, jsonify
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from display import render_display
import copy

executor = ThreadPoolExecutor(max_workers=1)

matrix = None
clock = None
brightness = None
fontcolor = None
current_matrix = None
current_clock = None
current_brightness = None
current_fontcolor = None


#Clock

def control_display():
    global matrix
    global clock
    global brightness
    global fontcolor

    current_matrix = None
    current_clock = None
    current_brightness = None
    current_time = None
    current_fontcolor = None

    while True:
        #Check wether there was a change in matrix or brightness
        #print("Current Fontcolor: ", current_fontcolor)
        #print("Current Brightness: ", current_brightness)
        #print("Fontcolor", fontcolor)
        #print("Brightness", brightness)
        time.sleep(1)
 
        if (matrix is not None) or (brightness is not None) or (fontcolor is not None):
            if (matrix is not None):
                current_matrix = matrix
                matrix = None
            if (brightness is not None):
                current_brightness = brightness
                brightness = None
            if (fontcolor is not None):
                
                current_fontcolor = fontcolor
                fontcolor = None
            current_time = datetime.now().strftime("%H%M")      
            render_display(current_matrix, clock, current_brightness, current_fontcolor)        
        #If there weren't any changes in matrix or brightness, check if the time has changed.
        if current_time != datetime.now().strftime("%H%M"):
            if current_matrix is not None:
                current_time = datetime.now().strftime("%H%M")
                render_display(current_matrix, clock, current_brightness, current_fontcolor)            


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

    return jsonify({'message': 'Helligkeit erfolgreich eingestellt'}), 200

@app.route('/api/fontcolor', methods=['POST'])
def set_fontcolor():
    global fontcolor
    fontcolor_new = request.json.get('fontcolor')
    fontcolor = fontcolor_new
    return jsonify({'message': 'Helligkeit erfolgreich eingestellt'}), 200



if __name__ == '__main__':
    
    executor.submit(control_display)
    
    app.run(port='0.0.0.0', port='80', use_reloader=False)

