from datetime import datetime
import json
import copy
import board
import neopixel


#example = [[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[228,26,74],[0,0,0],[0,0,0],[228,26,74],[0,0,0],[0,0,0],[0,0,0],[67,183,110],[67,183,110],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[18,104,129],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[114,29,71],[114,29,71],[114,29,71],[0,0,0],[0,0,0]],[[0,0,0],[228,26,74],[0,0,0],[228,26,74],[228,26,74],[0,0,0],[0,0,0],[0,0,0],[67,183,110],[0,0,0],[67,183,110],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[18,104,129],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[114,29,71],[0,0,0],[0,0,0],[0,0,0],[114,29,71],[0,0,0]],[[0,0,0],[228,26,74],[228,26,74],[228,26,74],[228,26,74],[0,0,0],[0,0,0],[0,0,0],[67,183,110],[0,0,0],[0,0,0],[67,183,110],[0,0,0],[0,0,0],[0,0,0],[18,104,129],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[243,117,33],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[114,29,71],[0,0,0],[0,0,0],[0,0,0],[114,29,71],[0,0,0]],[[0,0,0],[228,26,74],[0,0,0],[0,0,0],[228,26,74],[0,0,0],[0,0,0],[67,183,110],[67,183,110],[67,183,110],[67,183,110],[67,183,110],[0,0,0],[0,0,0],[0,0,0],[18,104,129],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[243,117,33],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[114,29,71],[0,0,0],[0,0,0],[0,0,0],[114,29,71],[0,0,0]],[[0,0,0],[228,26,74],[0,0,0],[0,0,0],[228,26,74],[0,0,0],[0,0,0],[67,183,110],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[67,183,110],[0,0,0],[0,0,0],[18,104,129],[18,104,129],[18,104,129],[18,104,129],[0,0,0],[243,117,33],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[114,29,71],[114,29,71],[0,0,0],[0,0,0],[0,0,0],[114,29,71],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[243,117,33],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[114,29,71],[0,0,0],[0,0,0],[114,29,71],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[243,117,33],[243,117,33],[243,117,33],[243,117,33],[243,117,33],[0,0,0],[0,0,0],[114,29,71],[114,29,71],[0,0,0],[0,0,0],[0,0,0]]]

# function to render display
def render_display(matrix, clock, brightness, fontcolor_var):
    fontcolor = copy.deepcopy(fontcolor_var)
    
    matrix_string = []
    
    if clock == True:
        current_time = datetime.now().strftime("%H%M")
        
        v1, v2, v4, v5 = current_time
        
        #load .json font required to display time
        first = f"font/{v1}.json"
        second = f"font/{v2}.json"
        colon = "font/colon.json"
        third = f"font/{v4}.json"
        fourth = f"font/{v5}.json"

        with open(first, 'r') as file:
                first = json.load(file)
        with open(second, 'r') as file:
                second = json.load(file)
        with open(colon, 'r') as file:
                colon = json.load(file)
        with open(third, 'r') as file:
                third = json.load(file)
        with open(fourth, 'r') as file:
                fourth = json.load(file)

        #overwrite pixel meant to display the clock
        
        #check wether there's a different color chosen
        if isinstance(fontcolor, list) and (len(fontcolor) == 3):
            for i in range (1, 7):      
                for j in range (4, 9):
                    if (first[i])[(j-4)] == [255,255,255]:
                        (matrix[i])[j] = copy.deepcopy(fontcolor_var)
                    else:
                        (matrix[i])[j] = (first[i])[(j-4)]
                for j in range (9, 14):
                    if (second[i])[(j-9)] == [255,255,255]:
                        (matrix[i])[j] = copy.deepcopy(fontcolor_var)
                    else:
                         (matrix[i])[j] = (second[i])[(j-9)]     
                for j in range (14, 17):
                    if (colon[i])[(j-14)] == [255,255,255]:
                        (matrix[i])[j] = copy.deepcopy(fontcolor_var)
                    else:
                        (matrix[i])[j] = (colon[i])[(j-14)]     
                for j in range (17, 22):
                    if (third[i])[(j-17)] == [255,255,255]:
                        (matrix[i])[j] = copy.deepcopy(fontcolor_var)
                    else:
                        (matrix[i])[j] = (third[i])[(j-17)]     
                for j in range (22, 27):
                    if (fourth[i])[(j-22)]  == [255,255,255]:
                        (matrix[i])[j] = copy.deepcopy(fontcolor_var)
                    else:
                         (matrix[i])[j] = (fourth[i])[(j-22)]

        #if no other color is chosen
        else:
            for i in range (1, 7):
                for j in range (4, 9):
                    (matrix[i])[j] = (first[i])[(j-4)]     
                for j in range (9, 14):
                    (matrix[i])[j] = (second[i])[(j-9)]     
                for j in range (14, 17):
                    (matrix[i])[j] = (colon[i])[(j-14)]     
                for j in range (17, 22):
                    (matrix[i])[j] = (third[i])[(j-17)]     
                for j in range (22, 27):
                    (matrix[i])[j] = (fourth[i])[(j-22)]
    
    if isinstance(brightness, int):
        #automatic brightness
        #turns brightness to 50% from 06:00 until 23:00. Brightness is set to 2% for the night.
        if brightness == 101:
            if (datetime.now().strftime("%H:%M:%S") >= "06:00:00") and (datetime.now().strftime("%H:%M:%S") <= "23:00:00"):
                  brightness = 50
            else:
                 brightness = 2

        #brightness
        if (brightness >= 0) and (brightness <= 100):
            for i in range (0, 8):      
                for j in range(0, 32):
                    for k in range(0, 3):
                        matrix[i][j][k] = round((matrix[i][j][k])*brightness/100)
    
    #render matrix into serpentine strip for neopixel display
    for k in range(0, 32):    
        if k%2==0:
            for i in range(0, 8):
                submatrix = matrix[i]
                matrix_string.append(submatrix[k])
        else:
            for i in range (7, -1, -1):
                submatrix = matrix[i]
                matrix_string.append(submatrix[k])  
    send_display(matrix_string)

    return

#Drive neopixel display

def send_display(matrix):
    print(matrix)
    #setup
    pixel_pin = board.D18
    num_pixels = 256
    ORDER = neopixel.GRB
    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER)
    #set color for each pixel
    for i in range (num_pixels):
         pixels[i]=matrix[i]
    #show pixels
    pixels.show()
    return()