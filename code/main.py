import pandas as pd
df = pd.read_csv("../support_issues/support_issues.csv")
print(df.head())
print("Total tickets:", len(df))
