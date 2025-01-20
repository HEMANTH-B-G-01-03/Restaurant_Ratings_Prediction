import pandas as pd
from sklearn.model_selection import train_test_split

a=pd.read_csv('Dataset.csv')
b=a.head()
print(b)
c=a.describe()
print(c)

for col in df.select_dtypes(include=['float64', 'int64']).columns:
    df[col].fillna(df[col].median(), inplace=True)


for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)


train, test = train_test_split(df, test_size=0.20, random_state=42)

print("Training Set:")
print(train.head())
print("\nTesting Set:")
print(test.head())

