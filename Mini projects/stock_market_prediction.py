import math
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from nsepy import get_history
from datetime import date


df = get_history(symbol='INFY',start=date(2018,12,25),end=date(2019,2,28))
# # print(df.columns.values)
# df['PCT_CHANGE'] = ((df['Open'] - df['Close'])/(df['Close']))*100
# df['HL_PCT'] = ((df['High']-df['Low'])/(df['Low']))*100.0
# df = df[['Close','PCT_CHANGE','HL_PCT']]
df = df[['Close','Open','High','Low']]

forecast_col = 'Close'
# df.fillna(value=-99999, inplace=True)
# # # forecast_out = int(math.ceil(0.01 * len(df)))
forecast_out = 3
df['label'] = df[forecast_col].shift(-forecast_out)

# print(df[['Close','label']])

X = np.array(df.drop(['Close','label'], 1))
# X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

y = np.array(df['label'])
y = y[:-forecast_out]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = LinearRegression()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)   # coefficient of determination
forecast_set = clf.predict(X_lately)

# # print(df)
print(forecast_set)