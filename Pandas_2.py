import pandas as pd

df = pd.read_csv('weight-height (1).csv')
print(df)
print(type(df))

print(df.head(15))
print(df.Gender.value_counts())
df.Height *= 2.542
df.Weight /= 2.2
print(df)
print(df.describe())
print(df.describe().T.to_string())
df = pd.get_dummies(df)
print(df)
df['new'] = df.Weight - 100
df['new2'] = 5
print(df)
del (df['Gender_Male'])
print(df)
df.rename(columns={'Gender_Female': 'Gender'}, inplace=True)
print(df)
df.to_csv('new.csv')