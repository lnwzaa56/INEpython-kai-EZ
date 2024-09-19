import pandas as pd

data = {"name": ["Alice", "Bob", "Chicago"],
        "Age": [25,30,35],
        "city": ["New york", " Los Angeles", "Chicago"]}

df = pd.DataFrame(data)
print("Dataframe:\n", df)

average_age = df["Age"].mean()
print("\nAverage Age:", average_age)

filtered_df = df[df["Age"] > 28]
print("\nfiltered DataFrame (Age > 28):\n", filtered_df)

df["salary"] = [50000, 60000, 70000]
print("\ndataFrame with Salary column:\n", df)