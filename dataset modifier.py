import pandas as pd
import math
import random

data = []

# Generate 5000 samples
for _ in range(5000):
    length = random.randint(4, 25)
    
    size = random.choice([
        26, 36, 52, 62, 72, 94
    ])

    entropy = length * math.log2(size)

    data.append([length, size, entropy])

# Create DataFrame
df = pd.DataFrame(data, columns=["length", "size", "entropy"])

# Add scaled entropy
min_e = df["entropy"].min()
max_e = df["entropy"].max()

df["entropy_scaled"] = (df["entropy"] - min_e) / (max_e - min_e) * 100

# Save dataset
df.to_csv("entropy_dataset_5000.csv", index=False)

print("Dataset created successfully ✅")
print(df.head())