import pandas as pd

data = pd.read_csv('test.csv')
# print(data)
# print(data,type(data))
# print(data.columns.values)
# print(data['Student ID'])
# print(data,'\n','-'*100)
# print(data[['Student ID','Chemistry','Physics']])
data['Total'] = data['Maths']+data['Physics']+data['Chemistry']
# print(data)
data = data.dropna()
# data = data.fillna(99999)
# print(data)
# print(data[data['Total'] > 200])
# total_more_than_200 = data[data['Total'] > 200]
# print(data[(data['Maths']>80) & (data['Physics']>80)])
# print(total_more_than_200)

# print(data['Student ID'].tolist())
# print(data['Branch'])
data = data.drop(['Physics','Maths'],axis=1)
print(data)
# print(data['Chemistry'].sum/())
# data = data.dropna()
# # print(data)

# # # # data['Total'] = data['Maths']+data['Physics']+data['Chemistry']
data['Chemistry_result'] = data['Chemistry'].apply(lambda x: 'Pass' if x>35 else 'Fail')
print(data)
data.to_csv('abc.csv')


# # # print(data[data['Maths']<80])
# print(data[(data['Chemistry']>40) & (data['Branch'] == 'IT')])
# print(data[(data['Maths']>40) | (data['Physics']>40)])
# # print('-'*100)
# # print(data[data['Maths'] > 90])

print(data[data['Branch'] == 'IT']['Total'].sum())

# print(data[data['Branch'] == 'IT']['Total'].sum())

# test_data['Physics'] = test_data['Physics'].apply(lambda x: 'A' if x>0 and x<=20 else x)
# test_data['Physics'] = test_data['Physics'].apply(lambda x: 'B' if x>10 and x<=30 else x)
# print test_data

# def slab_ranges(df,column):
# 	df[column] = np.where((df[column] > 0) & (df[column] <= 50),1000,df[column])
# 	df[column] = np.where((df[column] > 50) & (df[column] <= 100),2000,df[column])
# 	return df


# test_data = pd.read_csv('test.csv')


# test_data['OG_branch'] = test_data['Branch']
# test_data['Branch'] = np.where((test_data['Branch'] == 'IT') | (test_data['Branch'] == 'CSE'),'Computers',test_data['Branch'])

# print test_data['Chemistry']
# print '-'*100
# print slab_ranges(test_data,'Chemistry')
