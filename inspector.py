import pandas as pd
import joblib
import warnings
import skops.io as sio
import pickle
import os
import numpy as np
HOME = os.path.expanduser('~')
modelName = 'ANN'
filename = HOME + '/MITM-Detection/Models/' + modelName
classifier = joblib.load(filename)
dt_realtime = pd.read_csv('realtime.csv')
result = classifier.predict(dt_realtime)

with open('result.txt', 'w') as f:
    f.write(str(result[0]))
