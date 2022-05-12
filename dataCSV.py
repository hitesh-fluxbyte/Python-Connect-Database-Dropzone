import pandas as pd

data = pd.read_csv(r"C:\Users\fluxb\OneDrive\Desktop\Hitesh\Python-Task\data\sample.csv")

print(data)

head = data.head()
print(head)

tail = data.tail()
print(tail)

print(data.dtypes)
print(data.info)
