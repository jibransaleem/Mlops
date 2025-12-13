import numpy as np 
import pandas as pd
import os

dir = "Data"
os.makedirs(dir ,exist_ok=True)

path  = os.path.join(dir , "sample_data.csv")
df = pd.DataFrame({
    
    'A': np.random.rand(5),
    'B': np.random.rand(5),
})
df['C'] = df['A'] + df['B']
df['D'] = df['A'] * df['B']

df['E']= df['A'] / (df['B'] + 1e-5)
df['F'] = df['A'] ** 2 + df['B'] ** 2
df['K'] = np.sqrt(df['A']**2 + df['B']**2)
df.to_csv(path , index = False)
print(f"Data saved to {path}")