import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#print(df.columns)
#print(df[['Name', 'Type 1', 'HP']][0:10])

#print(df.iloc[1])

#for index, row in df.iterrows():
#    print(row[['Name', 'Type 1']])

print(df.loc[(df['Type 1'] == 'Fire') & (df['Type 2'] == 'Dark')])

