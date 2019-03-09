import pandas as pd


data = pd.read_csv('Berkeley.csv')

# data['Freq'] = data['Freq'].apply(lambda row: row*100)
# print(data)

total = data['Freq'].sum()
total_admitted = data[data['Admit'] == 'Admitted']['Freq'].sum()
total_rejected = data[data['Admit'] == 'Rejected']['Freq'].sum()
male_admitted = data[(data['Admit']=='Admitted') & (data['Gender']=='Male')]['Freq'].sum()
# print 'Male admitted:',male_admitted
# male_rejected = data[(data['Admit']=='Rejected') & (data['Gender']=='Male')]['Freq'].sum()
# print 'Male rejected:',male_rejected
female_admitted = data[(data['Admit']=='Admitted') & (data['Gender']=='Female')]['Freq'].sum()
female_rejected = data[(data['Admit']=='Rejected') & (data['Gender']=='Female')]['Freq'].sum()
# print 'Female admitted:',female_admitted,'Female rejected:',female_rejected

admitted_percentage = (float(data[data['Admit'] == 'Admitted']['Freq'].sum())/(data['Freq'].sum()))*100
rejected_percentage = 100 - admitted_percentage

# print 'Admitted percentage:',admitted_percentage,'Rejected percentage:',rejected_percentage

male_admitted_percentage = (float(male_admitted)/(total_admitted))*100
male_rejected_percentage = (float(male_rejected)/(total_rejected))*100
female_admitted_percentage = (float(female_admitted)/(total_admitted))*100
female_rejected_percentage = (float(female_rejected)/(total_rejected))*100

# print male_admitted_percentage,male_rejected_percentage,female_admitted_percentage,female_rejected_percentage