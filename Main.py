import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#print(df.columns)
#print(df[['Name', 'Type 1', 'HP']][0:10])

#print(df.iloc[1])

#for index, row in df.iterrows():
#    print(row[['Name', 'Type 1']])




df['Total'] = df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] + df['HP']

df = df.drop(columns=['Total'])

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

poisontypes = df.loc[(df['Type 1'] == 'Poison') | (df['Type 2'] == 'Poison')]
print(poisontypes)


##poisontypes.to_csv('poisontypes.csv')



