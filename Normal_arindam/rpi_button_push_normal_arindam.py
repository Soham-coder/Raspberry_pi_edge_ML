####################IMPORT_PACKAGE######################
import time
import RPi.GPIO as GPIO
import sys
#Imort the packages
import tensorflow as tf
print(tf.__version__)
print(tf.keras.__version__)    
#Output must be 
#1.14.0
#2.2.4-tf
import numpy as np
import cv2
import time
import os
print('All packages are imported')

####################LOAD_MODEL######################
time1 = time.time()
tflite_model = './weights/lite_flowers_model.tflite'
# Initialize TFLite interpreter using the model.
# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path=tflite_model)
interpreter.allocate_tensors()
time2 = time.time()
print('Time for Loading the model', time2-time1, 'Seconds')
print("Press pushbutton for predicting images")

####################READ_SINGLE_IMAGE_AND_PREDICT######################
def arindam_code_read_image_and_predict(input_image):
    print("Image to be predicted is : ", input_image)
    time0 = time.time()
    test = cv2.imread(input_image)
    test = cv2.resize(test,(240,240))
    time1 = time.time()
    print('Time for Reading the image', time1-time0, 'Seconds')
    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    # Test model on input data.
    test_image = np.expand_dims(test, axis=0).astype(np.float32)
    interpreter.set_tensor(input_details[0]['index'], test_image)
    interpreter.invoke()
    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
    output_data = interpreter.get_tensor(output_details[0]['index'])
    time3 = time.time()
    print('Prediction: ',output_data)
    print('Time for Predicting the result', time3-time1, 'Seconds')
    print('=======================================')




    
####################MAIN_RPI_CODE######################
#Pin definitions
btn_pin = 10 # Pin 10 GPIO 15

#Setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Our counter
counter = 0

# Remember the current and previous button states

current_state = False
prev_state = False

# If button is pushed, execute script
try:
    while True:
        current_state = GPIO.input(btn_pin)
        if(current_state == True) and (prev_state == False):
            counter = counter + 1
            input_image_dir = input("Enter path of image directory where images are present:")
            print("Entered image directory is : ", input_image_dir)
            pic_list=os.listdir(path = input_image_dir)
            for image in pic_list:
                input_image = input_image_dir + "/" + image
                arindam_code_read_image_and_predict(input_image)  
        prev_state = current_state

# Only when you press ctrl+c , this will be called
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)
