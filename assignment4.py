import pandas as pd
df = pd.read_csv('month_temperature.csv')
for i in df.columns:
  df[i].fillna((df[i].mean()),inplace=True)

month_min=999999999
month_max=-999999999
month_sum=0

print('\n\nDay wise Min, Man And Average Temperature:-\n')
for i in df.columns:
  print(f'{i}:- Min:{df[i].min()},  Max: {df[i].max()}, Average: {round(df[i].mean(),2)}')
  month_sum += round(df[i].mean(),2)
  if df[i].min() < month_min:
    month_min = df[i].min()
  if df[i].max() > month_max:
    month_max = df[i].max()
    
month_avg = month_sum/df.shape[1]

print('\n\nMin, Man And Average Temperature of the month:-')
print(f'Min: {month_min}\nMax: {month_max}\nAverage: {round(month_avg,2)}')
