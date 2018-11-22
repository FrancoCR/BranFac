import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd

class predicter():
    #Called when creating the object. You can change the name of the class if needed.
    def __init__(self, modelLink):#modelLink = path to model
        tf.enable_eager_execution()
        self.model = tf.keras.models.load_model(modelLink)

    #Returns 0 or 1 for its prediction where 1 is malicious.
    def predict(self, data):
        formatedData = tf.convert_to_tensor([data])
        predictions = self.model(formatedData)

        for i, logits in enumerate(predictions):
              class_idx = tf.argmax(logits).numpy()
              #p = tf.nn.softmax(logits)[class_idx]
              return class_idx


#Example usage of class to make predictions.

prediction = predicter("C:/Users/Franco/Desktop/UTD/Fall18/CS6332/MaliciousIdentifier.h5")

def obtainLogInfo(textFile):
    AppLogs=[]

    with open(textFile) as f:
        f.seek(0)
        AppLogs=f.read()

    return AppLogs

def frequencyAnalysis(logs):

    frequency=np.ones((1,len(headers)))

    logLine = logs.split("\n")
    totalCount=0
    callCount = np.zeros(len(headers))
    for l in logLine:
        if "(" in l:
            totalCount+=1
            callCount[headers.index(l.split("(")[0])] += 1

    for i in range(len(headers)):
        frequency[0][i] = callCount[i] / totalCount

    return frequency[0]

sample3 = [0.00000000e+00, 0.00000000e+00, 4.57338129e-01, 5.75539568e-04,
 3.30935252e-03, 8.63309353e-04, 7.91366906e-04, 5.78417266e-02,
 1.43884892e-04, 7.19424460e-05, 8.63309353e-04, 0.00000000e+00,
 6.25899281e-03, 7.91366906e-04, 7.19424460e-05, 0.00000000e+00,
 5.58992806e-02, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
 7.19424460e-05, 1.36690647e-03, 3.57553957e-02, 1.09280576e-01,
 0.00000000e+00, 2.15827338e-03, 7.76978417e-03, 1.15107914e-03,
 5.25179856e-03, 1.43884892e-03, 2.58992806e-03, 8.63309353e-03,
 0.00000000e+00, 0.00000000e+00, 2.16546763e-02, 0.00000000e+00,
 1.20143885e-01, 7.19424460e-05, 6.40287770e-03, 0.00000000e+00,
 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 2.12949640e-02,
 0.00000000e+00, 7.19424460e-05, 6.92805755e-02, 7.91366906e-04,]

print(prediction.predict(sample3))
