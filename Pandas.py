import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)
print(type(df))
print(df.head(15)) #15 pierwszych
print(df.Gender.value_counts()) #ile jest różnych wartości w gender, czy klasy zrównoważnone
df.Height *= 2.54
df.Weight /= 2.2
print(df)

print(df.describe().T.to_string()) #wiersze zamienione z kolumnami i zamiana na string
df = pd.get_dummies(df)
print(df)
df['new'] = df.Weight - 100 #nowa kolumna o naziwe new
df['new2'] = 5
print(df)
del (df['Gender_Male'])
print(df)
df.rename(columns={'Gender_Female': 'Gender'}, inplace=True) #inplace zapisuje zmianę
print(df)
df.to_csv('new.csv')
