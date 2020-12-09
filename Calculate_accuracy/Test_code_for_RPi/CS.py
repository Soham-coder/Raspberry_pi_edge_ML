import tensorflow as tf
print(tf.__version__)
print(tf.keras.__version__)



from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


import numpy as np
import os, cv2
import random

import scipy

n = 240
m = 100
rng = np.random.default_rng(seed=42)
Phi = rng.random((m,n));
from scipy.fftpack import dct, idct

def dct2(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

def idct2(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')

def compress(img):
    R = dct2(img);
    shape_R = np.shape(R)
    X = R.reshape(shape_R[0]*shape_R[1]) # This is a row vector
    B = np.sort(abs(X))
    B =  B[::-1]
    B = B.reshape(B.shape[0],1)
    coeffs = 0
    
    while np.linalg.norm(B[0:coeffs,0])/np.linalg.norm(X) < 0.9998:
      coeffs =  coeffs + 1;

    R[abs(R) < B[coeffs,0]] = 0;
    #x = R.reshape(shape_R[0]*shape_R[1],1)
    y = np.zeros((m,n))
    for i in range(0,shape_R[1]):
      y[:,i] = np.dot(Phi,R[:,i])
   
    
    return y 
	
data_path= os.getcwd()+'/../Test_Data_for_RPi/old_dataset'
list_folder=os.listdir(path = data_path)
data=[]
im_size =240
for i in list_folder:
    new_path=os.path.join(data_path,i)
    pic_list=os.listdir(new_path)
    for img in pic_list:
        pic=os.path.join(new_path,img)
        #arr=cv2.imread(pic, cv2.IMREAD_GRAYSCALE)
        data.append([pic,list_folder.index(i)])

random.shuffle(data)

x_train,y_train=[],[]
import time
time1 = time.time()
k = 0
for i,j in data:
    k = k+1
    im = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(im,(240,240))
    y = compress(img)
    if(k%100 == 0):
      time2 = time.time()
      print("Required time is", time2 - time1, "Processed image no is: ",k)
    x_train.append(y)
    y_train.append(j)


x_train=np.array(x_train).reshape(-1,100,240,1)
y_train=np.array(y_train).reshape(len(y_train),1)

encoder = OneHotEncoder()
y_train = encoder.fit_transform(y_train)
y_train = y_train.toarray()
x_train = x_train/np.max(x_train)


X_train, X_test, Y_train, Y_test = train_test_split(x_train,y_train, test_size=0.20)
print('Dimensions of images:',X_train.shape[1:])
print('Number of images in training set :',X_train.shape[0])
print('Number of images in testing set :',X_test.shape[0])

import time

#Read the model in (you can change the model and tflite model but keep in mind that the dwt compressed data should be used for the dwt model and the normal images to be used for the normal model)
tflite_model = os.getcwd()+'/../v2/cs_TFLite.tflite'
tflite_model_quantized = os.getcwd()+'/../v2/cs_Quantized_TFLite.tflite'

# Initialize TFLite interpreter using the model.
# Load TFLite model and allocate tensors.


def normal_prediction_single(x):
  interpreter = tf.lite.Interpreter(model_path=tflite_model)
  interpreter.allocate_tensors()

  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()

  data_path = X_test[x]
  test_image = np.expand_dims(data_path, axis=0).astype(np.float32)
  t1 = time.time()
  interpreter.set_tensor(input_details[0]['index'], test_image)
  interpreter.invoke()

  output_data = interpreter.get_tensor(output_details[0]['index'])
  t2 = time.time()
  print(np.argmax(output_data))
  print('time taken : ', t2-t1)


def quantized_prediction_single(x):
  
  interpreter_q = tf.lite.Interpreter(model_path=tflite_model_quantized)
  interpreter_q.allocate_tensors()

  input_details_q = interpreter_q.get_input_details()
  output_details_q = interpreter_q.get_output_details()

  data_path = X_test[x]
  test_image = np.expand_dims(data_path, axis=0).astype(np.float32)
  t1 = time.time()
  interpreter_q.set_tensor(input_details_q[0]['index'], test_image)
  interpreter_q.invoke()

  output_data_q = interpreter_q.get_tensor(output_details_q[0]['index'])
  t2 = time.time()
  print(np.argmax(output_data_q))
  print('Time taken is :', t2-t1)

def get_accuracy_normal():
  interpreter = tf.lite.Interpreter(model_path=tflite_model)
  interpreter.allocate_tensors()

  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()

  n = 0
  normal = []
  for i in range(1, len(X_test)):
    test_image = np.expand_dims(X_test[i], axis=0).astype(np.float32)
    interpreter.set_tensor(input_details[0]['index'], test_image)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    if np.argmax(output_data)==np.argmax(Y_test[i]):
      n+=1
    else:
      normal.append(i)
    
  print('Accuracy of normal model= ', n/len(X_test))
  print('Wrongly classified images of normal model :', normal)
  print('No of right classifications : ', n)


def get_accuracy_quantized():
  interpreter = tf.lite.Interpreter(model_path=tflite_model_quantized)
  interpreter.allocate_tensors()

  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()

  n = 0
  quantized = []
  for i in range(1, len(X_test)):
    test_image = np.expand_dims(X_test[i], axis=0).astype(np.float32)
    interpreter.set_tensor(input_details[0]['index'], test_image)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    if np.argmax(output_data)==np.argmax(Y_test[i]):
      n+=1
    else:
      quantized.append(i)
    
  print('Accuracy of quantized model= ', n/len(X_test))
  print('Wrongly classified images of normal model :', quantized)
  print('No of right classifications : ', n)
