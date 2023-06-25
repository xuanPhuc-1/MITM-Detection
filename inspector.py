import pandas as pd
import joblib
import warnings

filename = 'MitM_nn'
classifier = joblib.load(filename)
dt_realtime = pd.read_csv('realtime.csv')
result = classifier.predict(dt_realtime)

with open('result.txt', 'w') as f:
    f.write(str(result[0]))