# -*- coding: utf-8 -*-
"""tpot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LJ1qfrs3lX_Geih3scXnPnoHLo9g7uJo
"""

# Commented out IPython magic to ensure Python compatibility.
pip install tpot
from google.colab import drive
import pandas as pd
import numpy as np
import requests
import io
drive.mount('/gdrive')
# %cd /gdrive/MyDrive/Tpot-deneme
!ls
df = pd.read_csv('/gdrive/MyDrive/Tpot/data.csv', encoding= 'unicode_escape')
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
data = load_data()
data[0:5], data.target
df.shape
df.head(5)
df.shape
X_train, X_test, y_train, y_test = train_test_split(data, data.target,
                                                    train_size=0.75, test_size=0.25)
X_train.shape, X_test.shape, y_train.shape, y_test.shape
tpot = TPOTClassifier(verbosity=2, max_time_mins=2)
tpot.fit(X_train, y_train)
print(tpot.score(X_test, y_test))
tpot = TPOTClassifier(generations=8, population_size=50, verbosity=2)
tpot.fit(X_train, y_train)
print("Accuracy is {}%".format(tpot.score(X_test, y_test)*100))
tpot.export('tpot_data_pipeline.py')