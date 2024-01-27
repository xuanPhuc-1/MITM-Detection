import pandas as pd
# import joblib
# import warnings
import csv
import pickle
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
import warnings
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning, module="tensorflow")


sc = StandardScaler()
HOME = os.path.expanduser('~')
modelName = 'GRU'
filename = HOME + '/MITM-Detection/Models/' + modelName


with open(filename, 'rb') as file:
    classifier = pickle.load(file)

sample = pd.read_csv('realtime.csv')
result = classifier.predict(sample)

print(result[0])


threshold = 0.5
binary_prediction = 1 if result[0] > threshold else 0
with open('result.csv', 'w') as f:
    # write binary_prediction to result.csv
    writer = csv.writer(f)
    writer.writerow([binary_prediction])
    f.close()


# import pandas as pd
# import joblib
# import warnings
# import skops.io as sio
# import pickle
# import os
# import numpy as np
# HOME = os.path.expanduser('~')
# modelName = 'ANN'
# filename = HOME + '/MITM-Detection/Models/' + modelName
# classifier = joblib.load(filename)
# dt_realtime = pd.read_csv('realtime.csv')
# result = classifier.predict(dt_realtime)
# print(result[0])
# with open('result.txt', 'w') as f:
#     f.write(str(result[0]))
