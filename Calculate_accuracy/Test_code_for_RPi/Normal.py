#Imort the packages
import tensorflow as tf
from tensorflow import keras
print(tf.__version__)
print(tf.keras.__version__)    
#Output must be 
#2.3.0
#2.4.0
import numpy as np
import cv2
import time, os
from sklearn.preprocessing import OneHotEncoder
print('All packages are imported')


#Import Test Dataset
time0 = time.time()
def read_data(direc, im_type):
  x_test, y_test = [], []
  list_folder=os.listdir(path = data_path)
  if im_type == 'dwt':
    for i in list_folder:
      new_path=os.path.join(data_path,i) 
      pic_list=os.listdir(new_path)                                              
      for img in pic_list:  
        pic=os.path.join(new_path,img)   
        arr=cv2.imread(pic,0)
        arr = cv2.resize(arr,(240,240))
        cA, _ = pywt.dwt2(arr,'db2')    #Performing DWT operation
        if i == 'flair':
          label = 0
        elif i == 't1':
          label = 1
        elif i == 't1ce':
          label = 2
        elif i == 't2':
          label = 3
        x_test.append(cA) 
        y_test.append(label)
    
    X_test = np.array(x_test).reshape(-1,121,121,1)
    X_test = X_test/255
    y_test = np.array(y_test).reshape(-1,1)
    encoder = OneHotEncoder()
    y_test = encoder.fit_transform(y_test)
    Y_test = y_test.toarray()
  
  elif im_type == 'normal':
    for i in list_folder:
      new_path=os.path.join(data_path,i) 
      pic_list=os.listdir(new_path)                                              
      for img in pic_list:  
        pic=os.path.join(new_path,img)   
        arr=cv2.imread(pic)
        arr = cv2.resize(arr,(240,240))
        if i == 'flair':
          label = 0
        elif i == 't1':
          label = 1
        elif i == 't1ce':
          label = 2
        elif i == 't2':
          label = 3
        x_test.append(arr) 
        y_test.append(label)
    
    X_test = np.array(x_test).reshape(-1,240,240,3)
    X_test = X_test/255
    y_test = np.array(y_test).reshape(-1,1)
    encoder = OneHotEncoder()
    y_test = encoder.fit_transform(y_test)
    Y_test = y_test.toarray()

  return X_test, Y_test
    
data_path=os.getcwd()+'/Test_Data_for_RPi'
X_test, Y_test = read_data(data_path,'normal')     
time1 = time.time()
print("Time for reading all test images: ",time1-time0)

#Read the model in
tflite_model = os.getcwd()+'/v2/Normal_TFLite.tflite'
tflite_model_quantized = os.getcwd()+'/v2/Normal_Quantized_TFLite.tflite'

# Initialize TFLite interpreter using the model.
# Load TFLite model and allocate tensors.
time2 = time.time()
#normal
interpreter = tf.lite.Interpreter(model_path=tflite_model)
interpreter.allocate_tensors()
#quantized
interpreter_q = tf.lite.Interpreter(model_path=tflite_model_quantized)
interpreter_q.allocate_tensors()
time3 = time.time()
print("Time for Loading 2 models: ",time3-time2)
# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_details_q = interpreter_q.get_input_details()
output_details_q = interpreter_q.get_output_details()
time3 = time.time()
print("Required time for loading 2 models and allocating tensors, :", time3-time2)


time4 = time.time()
n = 0  #count for accuracy
normal = []
# Test model on input data.
for i in range(1, len(X_test)):
  test_image = np.expand_dims(X_test[i], axis=0).astype(np.float32)
  interpreter.set_tensor(input_details[0]['index'], test_image)
  interpreter_q.set_tensor(input_details_q[0]['index'], test_image)
  interpreter.invoke()
  interpreter_q.invoke()

  # The function `get_tensor()` returns a copy of the tensor data.
  # Use `tensor()` in order to get a pointer to the tensor.
  output_data = interpreter.get_tensor(output_details[0]['index'])
  
  if np.argmax(output_data)==np.argmax(Y_test[i]):
    n+=1
  else:
    normal.append(i)


time5 = time.time()
print('\n\nAccuracy of normal model= ', n/len(X_test))
print("Time to predict all " , len(X_test), " images is: ", time5-time4)
print("Average time to predict a image is: ", (time5-time4)/len(X_test))


time6 = time.time()
q = 0
quantized = []
# Test model on input data.
for i in range(1, len(X_test)):
  test_image = np.expand_dims(X_test[i], axis=0).astype(np.float32)
  interpreter.set_tensor(input_details[0]['index'], test_image)
  interpreter_q.set_tensor(input_details_q[0]['index'], test_image)
  interpreter.invoke()
  interpreter_q.invoke()

  # The function `get_tensor()` returns a copy of the tensor data.
  # Use `tensor()` in order to get a pointer to the tensor.
  output_data_q = interpreter_q.get_tensor(output_details_q[0]['index'])


  if np.argmax(output_data_q)==np.argmax(Y_test[i]):
    q+=1
  else:
    quantized.append(i)

time7 = time.time()
print('\n\nAccuracy of quantized model= ', q/len(X_test))
print("Time to predict all ", len(X_test), " images is: ", time7-time6)
print("Average time to predict a image is: ", (time7-time6)/len(X_test))

