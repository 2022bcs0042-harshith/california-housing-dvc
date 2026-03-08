# src/create_v1.py

import pandas as pd

df = pd.read_csv("housing.csv")   # original full dataset

df_v1 = df.head(5000)

df_v1.to_csv("data/housing.csv", index=False)

print("Dataset Version 1 created")